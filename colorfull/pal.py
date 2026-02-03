import cv2
import numpy as np
import os

MOD_PATH = os.path.expanduser("~/.minetest/mods/colorfull/textures/")
os.makedirs(MOD_PATH, exist_ok=True)

def generate():
    vals = [0, 51, 102, 153, 204, 255]
    shifts = [[0,0,0], [13,0,0], [0,13,0], [0,0,13]]
    for p_idx, s in enumerate(shifts):
        palette = np.zeros((256, 1, 3), dtype=np.uint8)
        idx = 0
        for r in vals:
            for g in vals:
                for b in vals:
                    palette[idx, 0] = [np.clip(b+s[2],0,255), np.clip(g+s[1],0,255), np.clip(r+s[0],0,255)]
                    idx += 1
        grays = np.linspace(0, 255, 40).astype(np.int32)
        for gray in grays:
            if idx < 256:
                v = np.clip(gray + (p_idx * 3), 0, 255)
                palette[idx, 0] = [v, v, v]
                idx += 1
        cv2.imwrite(os.path.join(MOD_PATH, f"pal_{p_idx}.png"), palette)
    print("Палитры готовы.")

if __name__ == "__main__": generate()