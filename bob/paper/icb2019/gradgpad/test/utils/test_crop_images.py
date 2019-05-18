#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2019+ Gradiant, Vigo, Spain
import unittest
from bob.paper.icb2019.gradgpad import crop_square_face, crop_image, meet_the_restrictions
from bob.paper.icb2019.gradgpad.test.test_utils import TestUtils


class UnitCropImages(unittest.TestCase):

    image_and_bbox = TestUtils.get_image_and_bbox("one_face.jpg")
    image = image_and_bbox["image"]
    bbox = image_and_bbox["bbox"]

    def test_should_crop_an_image_square(self):
        image = self.image
        annotation = {"bbox": self.bbox}
        cropped_image = crop_square_face(image, annotation)

        self.assertEqual(cropped_image.shape[0], cropped_image.shape[1])

    def test_should_crop_an_image_with_renctangle_bbox(self):
        image = self.image
        annotation = {"bbox": self.bbox}
        cropped_image = crop_image(image, annotation)

        self.assertNotEqual(cropped_image.shape[0], cropped_image.shape[1])

    def test_should_return_true_when_check_meet_the_restrictions(self):
        annotation = {"bbox": self.bbox}

        is_valid_with_80 = meet_the_restrictions(annotation, minimum_size_valid=80)
        is_valid_with_3000 = meet_the_restrictions(annotation, minimum_size_valid=3000)

        self.assertTrue(is_valid_with_80)
        self.assertFalse(is_valid_with_3000)
