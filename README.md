# Image Watermarking Script

A Python script to add a watermark to images in a specified folder.

## Features
- **Automatic watermark resizing**: Scales the watermark based on the image's total pixel area.
- **Transparency preservation**: Maintains existing transparency while adjusting overall opacity.
- **Custom positioning**: Places the watermark at the bottom-right corner.

## Requirements
- Python 3.x
- Pillow library (install with `pip install Pillow`)

## Usage

### Prepare Folders
1. Place your images in the `input` folder.
2. Ensure your watermark image is a PNG with transparency (e.g., `watermark.png`).

### Configure Parameters in the Script
Edit the following parameters in the script:

```python
input_folder = r'path\to\input'
output_folder = r'path\to\output'
watermark_image_path = r'path\to\watermark.png'
area_percent = 5  # Watermark area as a percentage of the image area
transparency = 182  # Watermark transparency (0 to 255)
```

## Made with Chatgpt1o-preview
