# Luanti (Minetest) Video Player
A high-performance real-time video player for **Luanti** (formerly Minetest) using Python and OpenCV.

- **Author:** mindys390 (YT: @pro100temich)

- **AI Collaborator:** Developed with the assistance of **Gemini 2.5 Flash** (architecture, optimization, and troubleshooting).

- **Engine:** Luanti (Minetest)

- **Library:** Miney

# Bad Apple in Minetest (Luanti)
Watch the demo here: [https://youtu.be/E7NJm5yWVso](https://youtu.be/E7NJm5yWVso)

## Features
- **1024 Virtual Colors:** Uses 4 dynamic palettes with spatial dithering (2x2 block grid) to overcome the standard 256-color limit.
- **Real-time Streaming:** Processes video frames on the fly and sends updates to the game via the `miney` library.
- **Delta Updates:** Only changed pixels are sent to the game engine to optimize network traffic.
- **Self-Healing Screen:** The screen is made of breakable blocks. If you punch a hole in the screen, the script will automatically "repair" it within seconds.

## Requirements
### Python Side:
- Python 3.x
- `opencv-python`
- `numpy`
- `miney` (The bridge between Python and Luanti)

Install dependencies:
```bash
pip install opencv-python numpy miney
