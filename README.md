# zine.py

generate a simple photobook as a pdf

each image is roughly A5 (aspect ratio is preserved, area is maximized)

it's intended to be printed on a printer that can print both sides and then folded in the middle of the longest edge

# deps

- (weasyprint)[https://weasyprint.org/]
- (jinja2)[http://jinja.pocoo.org/docs/2.10/]
- (pillow)[https://pillow.readthedocs.io/en/5.3.x/]

```sh
pip install WeasyPrint Jinja2 Pillow
```

# Use

have a file that's called `cover.jpg` and `back.jpg` that are A5 portrait, 300DPI (1748x2480 pixels)

export your images in roughly 3:2 format, 300DPI. the order of the images is
always the alphabetical sort, numbering with leading zeros works well.

```sh
zine.py
open output.pdf
```
