# !/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@paper.org>
# Copyright (C) 2019+ Gradiant, Vigo, Spain
from bob.gradiant.core import FeaturesExtractor

from bob.paper.icb2019.gradgpad.classes.utils.preprocess import preprocess_image
from bob.paper.icb2019.gradgpad.classes.color_based.coalbp import calculate_coalbp_features
from bob.paper.icb2019.gradgpad.classes.color_based.lpq import lpq
import numpy as np
import cv2


class BoulkenafetFeaturesExtractor(FeaturesExtractor):
    """
    Based on the work of Zinelabidine Boulkenafet et al in:

     @inproceedings{boulkenafet2015,
                    title={Face anti-spoofing based on color texture analysis},
                    author={Boulkenafet, Zinelabidine and Komulainen, Jukka and Hadid, Abdenour},
                    booktitle={IEEE International Conference on Image Processing (ICIP), 2015},
                    pages={2636--2640},
                    year={2015},
                    organization={IEEE} }

    @ARTICLE{boulkenafet2016,
             author={Z. Boulkenafet and J. Komulainen and A. Hadid},
             journal={IEEE Transactions on Information Forensics and Security},
             title={Face Spoofing Detection Using Colour Texture Analysis},
             year={2016},
             volume={11},
             number={8},
             pages={1818-1830},
             doi={10.1109/TIFS.2016.2555286},
             ISSN={1556-6013},
             month={Aug},}

    The code is based on the Matlab toolbox:
        https://github.com/zboulkenafet/Face-anti-spoofing-based-on-color-texture-analysis
    """

    def __init__(self):
        super(BoulkenafetFeaturesExtractor, self).__init__()
        self.coalbp_conf = [[1, 2], [2, 4], [4, 8]]

    def run(self, dict_images, annotations=None):
        dict_features = {}

        if annotations is None:
            raise RuntimeError("Face annotations must be provided")
        features_list = []
        sorted_keys = sorted(list(dict_images))
        for key in sorted_keys:
            try:
                image = dict_images[key]['rgb']
            except IndexError:
                image = dict_images[key]

            if key not in annotations:
                continue

            preprocessed_image = preprocess_image(image, annotations[key])
            if preprocessed_image is None:
                continue
            image = preprocessed_image

            ycrcb_image = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
            hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

            features = np.empty(0)
            for color_space in [ycrcb_image, hsv_image]:
                lpq_features = self.compute_lpq_features(color_space)
                coalbp_features = self.compute_coalbp_features(color_space)
                features = np.concatenate((features, lpq_features, coalbp_features))
            features_list.append(features)

        if features_list:
            average_features = np.average(features_list, axis=0)
            if average_features.shape[0] == 19968:
                dict_features['0'] = average_features
            else:
                dict_features['0'] = None
        else:
            dict_features['0'] = None
        return dict_features

    def compute_lpq_features(self, image):
        features = []
        for i in range(image.shape[2]):
            features.append(lpq(image[i], radius=3, rho=0.90))
        return np.concatenate(features)

    def compute_coalbp_features(self, image):
        features = []
        for config in self.coalbp_conf:
            features.append(calculate_coalbp_features(image, lbp_r=config[0], co_r=config[1]))
        return np.concatenate(features)

