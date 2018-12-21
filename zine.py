#!/usr/bin/env python3

from jinja2 import Template
from weasyprint import HTML, CSS
from PIL import Image
import glob
import sys
import os
import argparse
import random

base_path = os.path.dirname(os.path.realpath(__file__))

def remove_rotated():
    rotated = glob.glob("rotated*")
    for i in rotated:
        os.remove(i)

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--count", metavar='N', help="number of photos in the zine",
                    type=int)
parser.add_argument("-o", "--output", help="destination file")
args = parser.parse_args()

remove_rotated()

names = glob.glob('*.jpg')

output_file = "output.pdf"
photo_count = len(names)

if args.output:
    output_file = args.output

names.sort()

if "cover.jpg" not in names:
    print("Missing cover.jpg in cwd. Exiting.")
    sys.exit(1)

names.remove("cover.jpg")

if "back.jpg" not in names:
    print("Missing back.jpg in cwd. Exiting.")
    sys.exit(1)

names.remove("back.jpg")

if args.count:
    if len(names) < args.count:
        print("not enough photos for the specificed count")
        sys.exit(1)
    while len(names) != args.count:
        names.pop(random.randrange(len(names)))

# mangle for printing a booklet
uturn = list()

for i in range(int(len(names) / 2)):
    uturn.append(names[i])
    uturn.append(names[-i - 1])

mangled = list()

# every other pair is reversed

for idx, p in enumerate(zip(uturn[::2], uturn[1::2])):
    if idx % 2 == 0:
        mangled.append(p[0])
        mangled.append(p[1])
    else:
        mangled.append(p[1])
        mangled.append(p[0])

# rotate appropriately portraits images
for idx, f in enumerate(mangled):
    im = Image.open(f)
    if im.size[0] < im.size[1]:
        if idx % 2 == 1:
            out = im.transpose(Image.ROTATE_270)
        else:
            out = im.transpose(Image.ROTATE_90)
        outname = "rotated-" + f
        mangled[idx] = outname
        out.save(outname)

with open(base_path+'/template.html.jinja2') as file_:
    template = Template(file_.read())
    source = template.render(photos=mangled)
    with open(base_path+'/style.css') as style_:
        html = HTML(string=source, base_url=os.getcwd())
        css = CSS(string=style_.read())
        html.write_pdf('output.pdf', stylesheets=[css])

remove_rotated()
