import cv2
import miney
import numpy as np
import time
import sys

# --- CONFIGURATION ---
VIDEO_PATH = "video.mp4"
W, H = 64, 36         
X_O, Y_O, Z_O = 0, 100, 20  
FPS = 24              
RESET_INTERVAL = 120   # Refresh screen cache every 120 frames

def play_cinema():
    try:
        lt = miney.Luanti()
        print("Connected to Minetest.")
    except Exception as e:
        print(f"Error: {e}")
        return

    cap = cv2.VideoCapture(VIDEO_PATH)
    
    # 2x2 spatial dithering setup (4 palettes)
    b_types = np.zeros((H, W), dtype=np.int32)
    for r in range(H):
        for c in range(W):
            b_types[r, c] = (r % 2) * 2 + (c % 2)

    prev_p2 = np.zeros((H, W), dtype=np.int32) - 1
    delay = 1.0 / FPS
    frame_count = 0

    try:
        while cap.isOpened():
            start_time = time.time()
            ret, frame = cap.read()
            if not ret: break

            frame_count += 1
            if frame_count % RESET_INTERVAL == 0:
                prev_p2.fill(-1)

            # Processing frame
            img = cv2.resize(frame, (W, H), interpolation=cv2.INTER_NEAREST)
            b, g, r = [img[:,:,i].astype(np.int32) for i in range(3)]
            p2_map = (r * 5 // 255) * 36 + (g * 5 // 255) * 6 + (b * 5 // 255)

            # Detect changed pixels
            mask = p2_map != prev_p2
            r_idx, c_idx = np.where(mask)

            if len(r_idx) > 0:
                updates = [f"{{{c},{r},{p2_map[r,c]},{b_types[r,c]}}}" 
                           for r, c in zip(r_idx, c_idx)]
                
                # Send data in chunks via Lua
                for i in range(0, len(updates), 500):
                    chunk = ",".join(updates[i:i+500])
                    lua = (f"local u,x,y,z,h={{{chunk}}},{X_O},{Y_O},{Z_O},{H} "
                           f"for i=1,#u do local v=u[i] "
                           f"minetest.set_node({{x=x+v[1],y=y+h-v[2],z=z}},"
                           f"{{name='colorfull:pixel_'..v[4],param2=v[3]}}) end")
                    lt.lua.run(lua)

            prev_p2[mask] = p2_map[mask]

            # Sync and preview
            elapsed = time.time() - start_time
            if elapsed < delay:
                time.sleep(delay - elapsed)

            sys.stdout.write(f"\rFrame: {frame_count} | Blocks: {len(r_idx)}   ")
            sys.stdout.flush()

            cv2.imshow("Preview", cv2.resize(img, (320, 180)))
            if cv2.waitKey(1) & 0xFF == ord('q'): break

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("\nDisconnected.")
        del lt

if __name__ == "__main__":
    play_cinema()
