#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2017 Gradiant, Vigo, Spain

import argparse
import os
import cv2
from bob.gradiant.face.databases import AggregateDatabase, get_database_from_key, export_database_paths_from_file


def has_args(args):
    is_active = False
    for arg in vars(args):
        is_active = is_active or getattr(args, arg)
    return is_active


class ExampleFrame:

    LABEL_CORRESPONDENCES = {0: 'real',
                             1: 'print_low_quality',
                             2: 'print_medium_quality',
                             3: 'print_high_quality',
                             4: 'replay_low_quality',
                             5: 'replay_medium_quality',
                             6: 'replay_high_quality',
                             7: 'mask_paper',
                             8: 'mask_rigid',
                             9: 'mask_silicone'}

    def __init__(self, frame, label, metadata):
        self.frame = frame
        self.label = label
        self.metadata = metadata
        self.label_verbose = self.LABEL_CORRESPONDENCES[self.label]

    def save(self, base_path):
        filename = '{}/{}_{}.png'.format(base_path, self.label_verbose, self.metadata)
        print('Saving frame in {}'.format(filename))
        image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        cv2.imwrite(filename, image)


def get_database_name(access):
    database = access.base_path.split('/')[-1]

    if database == 'database':
        database = 'replay-mobile'

    if database == 'scene01':
        database = 'MSU_MFSD'

    if database == 'Data':
        database = '3DMAD'
 
    if database == 'Movies':
        database = 'replay-attack'

    return database.lower().replace('-','_')

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
        correspondencies = aggregate_database.get_ground_truth_list('grandtest', with_placeholder=False)['Test']
        correspondencies_keys = list(correspondencies.keys())
        example_frames = {}

        used_databases = []
        for access in accesses['All']:

            if len(example_frames) > 10:
                break

            database = get_database_name(access)
            if database in used_databases:
                continue

            name = access.name
            if name not in correspondencies_keys:
                continue

            label = correspondencies[name]


            if label not in example_frames:
                print(' |-> Adding label {} ({} - {})'.format(label, name, database))
                frames = access.load()
                middle_index = int(len(frames) / 2)

                middle_key = list(frames.keys())[middle_index]
                frame = frames[middle_key]
                example_frames[label] = ExampleFrame(frame, label, database)
                used_databases.append(database)

        for example_frame in example_frames.values():
            example_frame.save(args.output_path)



if __name__ == '__main__':
    main()
