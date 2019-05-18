from __future__ import print_function, division, absolute_import, generators, with_statement, unicode_literals
import os

from bob.paper.icb2019.gradgpad.test.mtcnn.disable_tensorflow_debugging_info import disable_tensorflow_debugging_info

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '4'
import tensorflow as tf
import numpy as np
from bob.paper.icb2019.gradgpad.classes import MtcnnFaceDetector
from bob.paper.icb2019.gradgpad.test.test_utils import TestUtils

disable_tensorflow_debugging_info()


class UnitTestMtcnnFaceDetector(tf.test.TestCase):

    def setUp(self):
        tf.reset_default_graph()
        with self.test_session() as sess:
            self.detector = MtcnnFaceDetector(sess, )
        self.image = TestUtils.get_image_and_bbox("one_face.jpg")["image"]

    def tearDown(self):
        pass

    def test_should_detect_one_face(self):
        bboxes, face_landmarks, scores, dnorm_scores = self.detector.detect(self.image)
        self.assertEqual(len(bboxes), 1)

    def test_should_not_detect_a_face(self):
        zero_image = np.zeros(self.image.shape)
        bboxes, face_landmarks, scores, dnorm_scores = self.detector.detect(zero_image)
        self.assertEqual(len(bboxes), 0)

    def test_should_crop_a_face(self):
        bboxes, face_landmarks, scores, dnorm_scores = self.detector.detect(self.image)
        raw_faces = self.detector.crop_faces(self.image, bboxes, False)
        square_faces = self.detector.crop_faces(self.image, bboxes, True)

        self.assertEqual(len(bboxes), len(raw_faces))
        self.assertEqual(len(bboxes), len(square_faces))

    def test_should_initialize_with_internal_session(self):
        _ = MtcnnFaceDetector()

    def test_should_work_with_two_instances(self):
        _ = MtcnnFaceDetector()
        _ = MtcnnFaceDetector()


if __name__ == '__main__':
    tf.test.main()
