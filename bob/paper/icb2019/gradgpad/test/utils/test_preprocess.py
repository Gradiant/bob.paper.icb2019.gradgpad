#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2019+ Gradiant, Vigo, Spain
import unittest
from bob.paper.icb2019.gradgpad.classes import resize_image_with_side_target_size
from bob.paper.icb2019.gradgpad.test.test_utils import TestUtils


class UnitPreprocess(unittest.TestCase):

    image_and_bbox = TestUtils.get_image_and_bbox("one_face.jpg")
    image = image_and_bbox["image"]

    def test_should_return_an_resized_image_with_resize_image_with_side_target_size(self):
        resized_image, rescale_factor = resize_image_with_side_target_size(self.image, 400)
        self.assertEqual(resized_image.shape, (216, 400, 3))
        self.assertAlmostEqual(rescale_factor, 0.6666666666666666, delta=0.1)



