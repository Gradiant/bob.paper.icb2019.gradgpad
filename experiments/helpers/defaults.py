import os
from bob.gradiant.core import AccessGridConfig


"""
Json file with the path of every parsed database
"""
DEFAULT_DATABASE_PATHS_CONFIG_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                  'database_paths.json')

"""
This following class contains the configuration in order to setup our experiments.
This class will combine the options (params) to modify the accesses (video)
consistently with the params.

Default parameters will filter the video from the center, using 2000 ms and 15 frames per second.

:param framerate_list: a list with a selected frame rates (default [15])
:param total_time_acquisition_list: a list with selected times to keep (default [2000] <- 2s)
:param starting_time_acquisition_list: a list with selected points to start the video.
Frames before this value will be discarded. (default [-1] <- ignore this parameter)
:param center_video_acquisition_list: Bool value. If True, it will ignore the starting_time value and crop the video
from the central point. (default [True])
"""
DEFAULT_ACCESS_GRID_CONFIG = AccessGridConfig(framerate_list=[15],
                                              total_time_acquisition_list=[2000],
                                              starting_time_acquisition_list=[-1],
                                              center_video_acquisition_list=[True])

"""
This file help us to maintain the base result path
"""
DEFAULT_BASE_RESULT_PATH = 'resources_bob_paper_icb2019_gradgpad'

"""
Number of threads to be executed extracting features
"""
DEFAULT_NUMBER_THREADS = 4

