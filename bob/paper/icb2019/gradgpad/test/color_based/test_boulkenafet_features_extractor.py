#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2019+ Gradiant, Vigo, Spain

import unittest
from bob.paper.icb2019.gradgpad.classes import BoulkenafetFeaturesExtractor
from bob.paper.icb2019.gradgpad.test.test_utils import TestUtils


class UnitTestBoulkafanetExtractor(unittest.TestCase):

    image_info = TestUtils.get_image_and_bbox("one_face.jpg")
    image = image_info["image"]
    bbox = image_info["bbox"]

    def test_run_with_default_config(self):
        dict_images = {'0': self.image,
                       '33': self.image,
                       '66': self.image
                       }

        features_extractor = BoulkenafetFeaturesExtractor()

        annotations = {'0': {"bbox": self.bbox},
                       '66': {"bbox": self.bbox}
                       }

        dict_features = features_extractor.run(dict_images, annotations)
        del features_extractor
        self.assertEqual(len(dict_features), 1)
        self.assertEqual(dict_features['0'].shape, (19968,))

    def test_throw_an_exception_if_not_annotations(self):
        dict_images = {'0': self.image}
        features_extractor = BoulkenafetFeaturesExtractor()
        self.assertRaises(RuntimeError, features_extractor.run, dict_images, None)
