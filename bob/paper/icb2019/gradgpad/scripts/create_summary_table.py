#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2017 Gradiant, Vigo, Spain

import argparse
import os
import pandas as pd


def recursive_glob(base_path, pattern):
    list_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(pattern):
                list_files.append(os.path.join(root, file))
    return list_files


def has_args(args):
    is_active = False
    for arg in vars(args):
        is_active = is_active or getattr(args, arg)
    return is_active


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-bp', '--base_path',
                        type=str,
                        dest='base_path',
                        help='From this base path, this scripy seeks recursively', required=True)
    parser.add_argument('-rp', '--result_path',
                        type=str,
                        dest='result_path',
                        help='result path', required=True)

    args = parser.parse_args()

    if not has_args(args):
        parser.print_help()
    else:

        list_summary_table_filename = recursive_glob(args.base_path, 'all_attacks_summary_table.csv')

        if len(list_summary_table_filename) == 0:
            raise IOError('There is no summary_tables here [{}]'.format(args.base_path))

        list_data_frame = []
        for summary_table_filename in list_summary_table_filename:
            data_frame = pd.DataFrame.from_csv(summary_table_filename)
            list_data_frame.append(data_frame)

        all_data_frame = pd.concat(list_data_frame)
        all_data_frame = all_data_frame.sort_values('Database')

        result_path = os.path.join(args.result_path, 'summary_tables')
        if not os.path.isdir(result_path):
            os.makedirs(result_path)

        all_data_frame.to_html(os.path.join(result_path, 'all_summary_table.html'))
        all_data_frame.to_latex(os.path.join(result_path, 'all_summary_table.tex'))
        all_data_frame.to_csv(os.path.join(result_path, 'all_summary_table.csv'))


if __name__ == '__main__':
    main()
