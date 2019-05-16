#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2019+ Gradiant, Vigo, Spain

import numpy as np
from bob.gradiant.core import FeaturesExtractor
from bob.pad.face.extractor.ImageQualityMeasure import ImageQualityMeasure
from bob.paper.icb2019.gradgpad.classes.utils.preprocess import preprocess_image


class MsuIqmFeaturesExtractor(FeaturesExtractor):
    """
    18 image-quality measures proposed by Galbally et al
    image-quality features proposed by Wen et al
    """

    def __init__(self, face_crop=False):
        self.image_quality_measure = ImageQualityMeasure()
        self.face_crop = face_crop
        super(MsuIqmFeaturesExtractor, self).__init__()

    def run(self, dict_images, annotations=None):

        dict_features = {}
        sorted_keys = sorted(list(dict_images), key=int)
        for key in sorted_keys:
            try:
                image = dict_images[key]['rgb']
            except IndexError:
                image = dict_images[key]

            if self.face_crop and annotations:

                if key not in annotations:
                    continue

                preprocessed_image = preprocess_image(image, annotations[key])
                if preprocessed_image is None:
                    continue
                image = preprocessed_image

            image_bob_format = np.swapaxes(image, 0, 2)
            features = self.image_quality_measure(image_bob_format)

            dict_features[key] = features
        return dict_features
