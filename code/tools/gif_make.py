#!/usr/bin/env python3
"""
Quick script to build a gif
"""

import argparse
import glob
import imageio
import os

def main():
    parser = argparse.ArgumentParser(
        description='Script to build a gif from images')
    parser.add_argument('--img_dir', '-i', help="input file directory")
    parser.add_argument('--vid', '-v', help="input video file")
    parser.add_argument('--out', '-o', help="output gif filename")
    args = parser.parse_args()

    out = "output.gif"
    if args.out:
        out = args.out

    images = []

    if args.img_dir:
        dirname = args.file_dir

        files = glob.glob(os.path.join(dirname, '*.jpg'))
        files = sorted(files)

        for filename in files:
            images.append(imageio.imread(filename))
        imageio.mimsave(out, images)

    if args.vid:
        reader = imageio.get_reader(args.vid)
        writer = imageio.get_writer(out)
        for idx, img in enumerate(reader):
            writer.append_data(img)
            if idx == 30:
                break
        reader.close()
        writer.close()


if __name__ == '__main__':
    main()
