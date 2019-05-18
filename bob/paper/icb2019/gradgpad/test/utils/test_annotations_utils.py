#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2019+ Gradiant, Vigo, Spain
import unittest
import numpy as np
from bob.paper.icb2019.gradgpad.classes.utils.annotations_utils import get_averaged_annotation, rescale_annotation


class UnitAnnotationUtils(unittest.TestCase):
    annotations = {"0": {"bbox": np.ones(4) * 10,
                         "landmarks": np.ones(10) * 10,
                         "confidence": np.array([0.8])
                         },
                   "33": {"bbox": np.array([0, 0, 100, 100]),
                          "landmarks": np.ones(10) * 100,
                          "confidence": np.array([0.8])
                          },
                   "66": {"bbox": np.array([0, 0, 120, 120]),
                          "landmarks": np.ones(10) * 120,
                          "confidence": np.array([0.8])
                          }
                   }

    def test_should_return_an_average_annotation_from_a_dict_of_annotations(self):
        annotation = get_averaged_annotation(self.annotations)

        np.testing.assert_array_equal(annotation["bbox"], np.array([0, 0, 110, 110]))
        np.testing.assert_array_equal(annotation["landmarks"], np.array([110, 110, 110, 110, 110, 110, 110, 110, 110, 110]))
        self.assertAlmostEqual(annotation["confidence"][0], 0.8, delta=0.1)

    def test_should_return_a_rescaled_annotation(self):
        annotation = rescale_annotation(self.annotations['0'], 4)
        np.testing.assert_array_equal(annotation["bbox"], np.array([40, 40, 40, 40]))
        np.testing.assert_array_equal(annotation["landmarks"], np.array([40, 40, 40, 40, 40, 40, 40, 40, 40, 40]))
        self.assertAlmostEqual(annotation["confidence"][0], 0.8, delta=0.1)

