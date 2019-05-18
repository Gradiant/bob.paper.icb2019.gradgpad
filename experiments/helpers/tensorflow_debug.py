import tensorflow as tf
import os


def tf_set_quiet_mode():
    """
    Disable debugging information
    """
    tf.logging.set_verbosity(tf.logging.ERROR)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

