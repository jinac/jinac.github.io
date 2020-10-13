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
    parser.add_argument('file_dir', help="input file directory")
    args = parser.parse_args()

    dirname = args.file_dir

    files = glob.glob(os.path.join(dirname, '*.jpg'))
    files = sorted(files)

    print(files)

    images = []
    for filename in files:
        images.append(imageio.imread(filename))
    imageio.mimsave(os.path.join(dirname, 'output.gif'), images)


if __name__ == '__main__':
    main()
