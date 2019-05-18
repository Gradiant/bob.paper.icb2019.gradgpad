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


def write_dict_to_file(filename, d):
    with open(filename, 'w') as f:
        for k in d.keys():
            f.write('{}\n'.format(k))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--json-file',
                        type=str,
                        dest='json_file',
                        help='json file where the ROOT_PATH of each dataset is defined', required=True)

    args = parser.parse_args()

    if not has_args(args):
        parser.print_help()
    else:

        base_output_path = 'gradgpad_protocols'
        os.makedirs(base_output_path, exist_ok=True)

        export_database_paths_from_file(args.json_file)  # temporary
        aggregate_database = get_database_from_key('aggregate-database')  # returns an object of AggregateDatabase class

        available_protocols = list(AggregateDatabase.get_available_protocols().keys())

        for protocol in available_protocols:

            protocol_output_path = '{}/{}'.format(base_output_path, protocol)
            os.makedirs(protocol_output_path, exist_ok=True)

            content = aggregate_database.get_ground_truth_list(protocol)
            for subset, accesses in content.items():
                filename = '{}/protocol_{}_{}.txt'.format(protocol_output_path, protocol, subset.lower())
                write_dict_to_file(filename, accesses)


if __name__ == '__main__':
    main()
