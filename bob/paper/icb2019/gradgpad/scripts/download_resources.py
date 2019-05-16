#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2019+ Gradiant, Vigo, Spain
import os
import logging
import coloredlogs
from bob.paper.icb2019.gradgpad import parser
import subprocess

SCORES_URL = 'https://portal.gradiant.org/GradBox/index.php/s/cmGFGkheEDQlFVn/download'
SCORES_FOLDER = 'resources_bob_paper_icb2019_gradgpad'


def is_already_downloaded():
    already_downloaded = False
    if os.path.isdir(SCORES_FOLDER):
        already_downloaded = True
    return already_downloaded


def get_logger(level='INFO'):
    logger = logging.getLogger('Download scores')
    coloredlogs.install(level=level, logger=logger)
    return logger


def main():
    args = parser()

    if args.verbose:
        quiet = ''
        logger = get_logger(level='DEBUG')
    else:
        quiet = '-q'
        logger = get_logger(level='INFO')

    if not is_already_downloaded():

        name_zip = 'resources_bob_paper_icb2019_gradgpad'
        dest_path_zip = '{}.zip'.format(name_zip)

        dest_path = 'resources_bob_paper_icb2019_gradgpad'
        if not os.path.isdir(dest_path):
            os.makedirs(dest_path)

        commands = {'1-downloading': 'wget {} -O {} {}'.format(SCORES_URL, dest_path_zip, quiet),
                    '2-unzipping': 'unzip {}'.format(dest_path_zip)
                    }

        for message, cmd in sorted(commands.items()):
            logger.debug('{}...'.format(message))
            logger.debug('command : {}'.format(cmd))

            output = subprocess.check_output(cmd, shell=True)
            if args.verbose:
                print(output)

        if os.path.isfile(dest_path_zip):
            os.remove(dest_path_zip)
    else:
        logger.debug('The score files are already downloaded in {}'.format(SCORES_FOLDER))


if __name__ == '__main__':
    main()
