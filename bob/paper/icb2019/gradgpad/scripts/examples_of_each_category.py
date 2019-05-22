#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2017 Gradiant, Vigo, Spain

import argparse
import os

from bob.gradiant.face.databases import AggregateDatabase, get_database_from_key, export_database_paths_from_file


def has_args(args):
    is_active = False
    for arg in vars(args):
        is_active = is_active or getattr(args, arg)
    return is_active


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-o', '--output-path',
                        type=str,
                        dest='output_path',
                        help='output path folder where the examples will be stored', required=True)
    parser.add_argument('--json-file',
                        type=str,
                        dest='json_file',
                        help='json file where the ROOT_PATH of each dataset is defined', required=True)

    args = parser.parse_args()

    if not has_args(args):
        parser.print_help()
    else:

        os.makedirs(args.output_path, exist_ok=True)

        export_database_paths_from_file(args.json_file)  # temporary
        aggregate_database = get_database_from_key('aggregate-database')  # returns an object of AggregateDatabase class

        accesses = aggregate_database.get_all_accesses()

        import pdb; pdb.set_trace()


if __name__ == '__main__':
    main()
