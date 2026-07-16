from PIL import Image
import numpy as np

path = "C:/BunkerSite/logo.png"
img = Image.open(path).convert("RGBA")
data = np.array(img)

# Sample corner pixels (top-left 5x5) to get background color
corner = data[:5, :5, :3]
bg_color = np.median(corner.reshape(-1, 3), axis=0).astype(int)
print(f"Detected background color (RGB): {bg_color}")

# Build a mask: pixels close to bg_color get alpha=0
tolerance = 30
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
mask = (
    (np.abs(r.astype(int) - bg_color[0]) < tolerance) &
    (np.abs(g.astype(int) - bg_color[1]) < tolerance) &
    (np.abs(b.astype(int) - bg_color[2]) < tolerance)
)

data[mask, 3] = 0  # set matching pixels to fully transparent
result = Image.fromarray(data)
result.save(path)

# Verify
verify = Image.open(path)
print(f"Mode: {verify.mode}")
print(f"Has alpha channel: {'A' in verify.mode}")
arr = np.array(verify)
transparent_pixels = np.sum(arr[:,:,3] == 0)
total_pixels = arr.shape[0] * arr.shape[1]
print(f"Transparent pixels: {transparent_pixels} / {total_pixels} ({100*transparent_pixels/total_pixels:.1f}%)")
print("DONE")
