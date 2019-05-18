#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2019+ Gradiant, Vigo, Spain
import argparse


def parser():
    parser_item = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser_item.add_argument('-v', '--verbose', dest='verbose', action='store_true')
    parser_item.set_defaults(verbose=False)
    args = parser_item.parse_args()
    return args
