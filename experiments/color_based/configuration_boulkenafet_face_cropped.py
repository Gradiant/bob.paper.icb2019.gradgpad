from experiments.helpers.aggregate_database_provider import aggregate_database_provider, get_available_protocols
from experiments.helpers.defaults import DEFAULT_DATABASE_PATHS_CONFIG_FILE, \
    DEFAULT_BASE_RESULT_PATH, DEFAULT_ACCESS_GRID_CONFIG, DEFAULT_NUMBER_THREADS
from bob.paper.icb2019.gradgpad import BoulkenafetFeaturesExtractor

# REQUIRED ARGUMENTS:

# Database paths:
# * You need to add a json file with the information of the databases
from experiments.helpers.pipeline_provider import get_pipeline_average_features_scaled_rbfsvc

database_paths_filename = DEFAULT_DATABASE_PATHS_CONFIG_FILE

# Database and protocol:
aggregate_database = aggregate_database_provider(database_paths_filename)
databases_list = [aggregate_database]
protocols_list = get_available_protocols()

# Feature extraction:
feature_extractor = BoulkenafetFeaturesExtractor()

# Pipeline:
pipeline = get_pipeline_average_features_scaled_rbfsvc('boulkenafet_rbf_svc')

# Result base path:
name_feature_extractor = feature_extractor.__class__.__name__.lower().replace('featuresextractor', '')
result_path = '{}/{}_face_cropped'.format(DEFAULT_BASE_RESULT_PATH, name_feature_extractor)


# Framerate and time parameters:
access_grid_config = DEFAULT_ACCESS_GRID_CONFIG

# -----------------------------------------------------------------
# OPTIONAL ARGUMENTS:

# Pad evaluation comparative using the framework bob.gradiant.pad.comparative
categorized_scores_plotter = None

# Verbose (only True/False are valid):
verbose = True

# Number of threads for parallelizing the features extraction:
number_threads = DEFAULT_NUMBER_THREADS

# Data augmentation:
use_data_augmentation = False

# Features extraction:
skip_features_extraction = True
extracted_features_path = 'resources_bob_paper_icb2019_gradgpad/boulkenafet_face_cropped/ACE/aggregate-database/features'
dict_extracted_features_paths = {'aggregate-database': {'ACE': extracted_features_path}}

# Training: you can skip training stage
skip_training = False

# Scores prediction:
skip_scores_prediction = False
dict_scores_paths = dict()

# Recreate: If it is true, features extraction will be done overwriting previous files
recreate = False
# -----------------------------------------------------------------
