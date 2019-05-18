#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2019+ Gradiant, Vigo, Spain
import unittest
import numpy as np
from bob.paper.icb2019.gradgpad.classes import MsuIqmFeaturesExtractor
from bob.paper.icb2019.gradgpad.test.test_utils import TestUtils


class UnitTestMsuIqmFeaturesExtractor(unittest.TestCase):

    image_info = TestUtils.get_image_and_bbox("one_face.jpg")
    image = image_info["image"]
    bbox = image_info["bbox"]

    def test_run_with_dict_images_landscape(self):
        dict_images = {'0': self.image,
                       '33': self.image,
                       '66': self.image}

        msu_iqm_features_extractor = MsuIqmFeaturesExtractor()

        dict_features = msu_iqm_features_extractor.run(dict_images)

        self.assertEqual(len(dict_features['0']), 139)
        self.assertEqual(len(dict_features['33']), 139)
        self.assertEqual(len(dict_features['66']), 139)

    def test_run_with_dict_images_portrait(self):
        dict_images = {'0': np.rot90(self.image),
                       '33': np.rot90(self.image),
                       '66': np.rot90(self.image)}

        msu_iqm_features_extractor = MsuIqmFeaturesExtractor()

        dict_features = msu_iqm_features_extractor.run(dict_images)

        self.assertEqual(len(dict_features['0']), 139)
        self.assertEqual(len(dict_features['33']), 139)
        self.assertEqual(len(dict_features['66']), 139)

    def test_run_with_dict_images_landscape_with_face_crop_and_annotations(self):
        dict_images = {'0': self.image,
                       '33': self.image,
                       '66': self.image}

        msu_iqm_features_extractor = MsuIqmFeaturesExtractor(face_crop=True)

        annotations = {'0': {"bbox": self.bbox},
                       '66': {"bbox": self.bbox}}

        dict_features = msu_iqm_features_extractor.run(dict_images, annotations=annotations)

        self.assertEqual(len(dict_features['0']), 139)
        self.assertEqual(len(dict_features['66']), 139)
        assert '33' not in dict_features
