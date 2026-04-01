"""Convert App_Logo.png to AppIcon.ico for Windows build."""
from PIL import Image
import os

src = os.path.join("assets", "logo", "App_Logo.png")
dst = os.path.join("assets", "logo", "AppIcon.ico")

img = Image.open(src).convert("RGBA")
sizes = [(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)]
img.save(dst, format="ICO", sizes=sizes)
print(f"Created {dst}")
