#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2019+ Gradiant, Vigo, Spain

import os
import shutil
import glob


def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        print(" - file {} is not a file or dir.".format(path))


def main():
    print("Cleaning auto-generated files and folders...")
    remove(".mr.developer.cfg")
    remove(".installed.cfg")
    remove("bin")
    remove("develop-eggs")
    remove("eggs")
    remove("parts")
    remove("src")
    remove("doc/output")
    remove(".cache")
    remove("src/test/__pycache__")
    for folder in glob.glob('*.egg-info'):
        remove(folder)


if __name__ == '__main__':
    main()
