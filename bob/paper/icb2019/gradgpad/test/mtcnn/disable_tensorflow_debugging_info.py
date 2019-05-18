import tensorflow as tf
import os


def disable_tensorflow_debugging_info():
    tf.logging.set_verbosity(tf.logging.ERROR)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
