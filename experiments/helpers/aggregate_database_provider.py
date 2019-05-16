import os
from bob.gradiant.face.databases import AggregateDatabase, get_database_from_key, export_database_paths_from_file


def aggregate_database_provider(database_paths_filename):
    export_database_paths_from_file(database_paths_filename)  # temporary
    aggregate_database = get_database_from_key('aggregate-database')  # returns an object of AggregateDatabase class

    if 'USE_CASIA_SURF' not in os.environ:
        del aggregate_database.included_databases['casia-surf']

    return aggregate_database


def get_available_protocols():
    available_protocols = list(AggregateDatabase.get_available_protocols().keys())

    if 'USE_UVAD' not in os.environ:
        if "cross-dataset-test-uvad" in available_protocols:
            available_protocols.remove("cross-dataset-test-casia-surf")

    return sorted(available_protocols)
