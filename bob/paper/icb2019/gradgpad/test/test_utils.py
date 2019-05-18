#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2019+ Gradiant, Vigo, Spain

from __future__ import division

import os
import cv2
import numpy as np


class TestUtils(object):
    resources_path = os.path.dirname(__file__) + '/../../../../../resources'
    result_path = os.path.dirname(__file__) + '/../../../../../result'

    @classmethod
    def get_resources_path(cls):
        return cls.resources_path

    @classmethod
    def get_result_path(cls):
        return cls.result_path

    @classmethod
    def get_image_and_bbox(cls, filename):
        bboxes = {"one_face.jpg": np.array([70, 212, 264, 361])}

        if filename not in bboxes:
            raise ValueError("filename is not available. Try with {}".format(list(bboxes)))
        bgr_image = cv2.imread(cls.resources_path + '/' + filename)
        rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        return {"image": rgb_image, "bbox": bboxes[filename]}

    @classmethod
    def get_synthetic_dict_image(cls, timestamp_reference=1500000000):
        dict_images = {}
        timestamp_reference = timestamp_reference
        for timestamp in range(timestamp_reference, timestamp_reference + 5000, 33):
            dict_images[timestamp] = cls.get_image()
        return dict_images

    @classmethod
    def get_synthetic_sequence(cls, sequence_len=10, image_size=100):
        dict_images = {}
        time_stamps = range(0, 33*sequence_len, 33)
        square_size = image_size//sequence_len
        for i, t in enumerate(time_stamps):
            image = np.zeros((image_size, image_size, 3))
            image[i * square_size:(i + 1) * square_size, i * square_size:(i + 1) * square_size, :] = 1
            dict_images[str(t)] = image.astype(np.uint8)
        return dict_images

