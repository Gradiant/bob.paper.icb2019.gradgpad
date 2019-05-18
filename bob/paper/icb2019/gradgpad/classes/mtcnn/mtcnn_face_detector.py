from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import tensorflow as tf

from .mtcnn_utils import detect_face, create_mtcnn, run_pnet_features, run_rnet_features
from bob.paper.icb2019.gradgpad.classes.utils.input_preprocessor import input_resize_preprocessor, rescale_bounding_boxes, rescale_landmarks
from bob.paper.icb2019.gradgpad.test.mtcnn.disable_tensorflow_debugging_info import disable_tensorflow_debugging_info

disable_tensorflow_debugging_info()


class MtcnnFaceDetector:
    """ Deep Face Detector
        This Face detector is based on MTCNN architecture (https://kpzhang93.github.io/MTCNN_face_detection_alignment)
    """

    def __init__(self, tf_session=None, min_face_size=40, max_image_size_lowest_side=360):
        """
        Deep Face Detector constructor. If tf_session is not None, then models will be loaded automatically.
        Otherwise, models won't be loaded and load function muste be called later.

        :param tf_session: Tensorflow created session or None
        """
        self.min_face_size = min_face_size
        self.max_image_size_lowest_side = max_image_size_lowest_side
        self.threshold = [0.6, 0.7, 0.9]  # three steps's threshold
        self.factor = 0.709  # scale factor

        self.pnet = None
        self.rnet = None
        self.onet = None
        self.session = None

        if tf_session is None:
            with tf.Graph().as_default() as g:
                gpu_options = tf.GPUOptions(allow_growth=True)
                dev_count = None
                self.session = tf.Session(graph=g, config=tf.ConfigProto(gpu_options=gpu_options, device_count=dev_count))
                self.load(self.session)
        else:
            self.load(tf_session)

    def __del__(self):
        if self.session:
            self.session.close()
            self.session = None

    def load(self, tf_session):
        """ Load Deep Face detector models

        :param tf_session: Tensorflow created session
        :return: None
        """
        if not isinstance(tf_session, tf.Session):
            raise RuntimeError("Unable to load models with None tensorflow session")
        self.pnet, self.rnet, self.onet = create_mtcnn(tf_session, None)

    def detect(self, image):
        """Performs face detection
        :param image: Numpy 3-d array (H,W,C)
        :return: list(bounding boxes), list(5-facial-landmarks), list(Norm2 over conv5 features as a quality measure )
        Each bounding box = [top, left, bottom, right].
        Each 5-facial-landmarks = [left-eye, right-eye, nose, mouth-left-corner, mouth-right-corner] Each point is [x,y]
        """
        self.__check()

        resized_image, scale_factor = input_resize_preprocessor(image, self.max_image_size_lowest_side)

        total_boxes, points, d_norms = detect_face(resized_image,
                                                   self.min_face_size,
                                                   self.pnet,
                                                   self.rnet,
                                                   self.onet,
                                                   self.threshold,
                                                   self.factor)
        face_landmarks = []
        bounding_boxes = []
        scores = []
        dnorm_scores = []
        if len(total_boxes) > 0:
            t_points = points.T
            for i in range(len(total_boxes)):
                top = total_boxes[i][1]
                bottom = total_boxes[i][3]
                left = total_boxes[i][0]
                rigth = total_boxes[i][2]
                bbox = [top, left, bottom, rigth]
                bounding_boxes.append(bbox)
                scores.append(total_boxes[i][4])
                dnorm_scores.append(d_norms[i])
                p = t_points[i]
                landmarks = []
                for j in range(5):
                    landmarks.append([p[j], p[j+5]])
                face_landmarks.append(landmarks)

        bounding_boxes = rescale_bounding_boxes(bounding_boxes, scale_factor)
        face_landmarks = rescale_landmarks(face_landmarks, scale_factor)

        return bounding_boxes, face_landmarks, scores, dnorm_scores

    def get_face_features(self, image):
        map_pnet, prob_pnet = run_pnet_features(self.pnet, image)
        map_rnet, prob_rnet = run_rnet_features(image, self.pnet, self.rnet, threshold=self.threshold[0])
        return map_pnet, map_rnet, prob_pnet, prob_rnet

    def crop_faces(self, image, bounding_boxes, square=False):
        faces = []
        for bbox in bounding_boxes:
            if square:
                face = self.__crop_square_face(image, bbox)
            else:
                face = self.__crop_raw_face(image, bbox)
            faces.append(face)
        return faces

    def __crop_square_face(self, image, bbox):
        h = min(bbox[2], image.shape[0]) - max(bbox[0], 0)
        w = min(bbox[3], image.shape[1]) - max(bbox[1], 0)
        largest = max(h, w)
        center_y = bbox[0] + h/2
        center_x = bbox[1] + w/2
        top = center_y - largest/2
        bottom = center_y + largest/2
        left = center_x - largest/2
        right = center_x + largest/2
        square_box = [top, left, bottom, right]
        return self.__crop_raw_face(image, square_box)

    @staticmethod
    def __crop_raw_face(image, bbox):

        bbox[0] = int(max(0, bbox[0]))
        bbox[1] = int(max(0, bbox[1]))
        bbox[2] = int(min(image.shape[0], bbox[2]))
        bbox[3] = int(min(image.shape[1], bbox[3]))

        return image[bbox[0]:bbox[2], bbox[1]:bbox[3], :]

    def __check(self):
        if self.onet is None or self.pnet is None or self.rnet is None:
            raise RuntimeError('DeepDetector must be previously initialized. Please call load() function')
