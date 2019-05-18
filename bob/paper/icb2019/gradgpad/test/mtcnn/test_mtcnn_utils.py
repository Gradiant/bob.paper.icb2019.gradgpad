from __future__ import print_function, division, absolute_import, generators, with_statement, unicode_literals
import os

from bob.paper.icb2019.gradgpad.test.mtcnn.disable_tensorflow_debugging_info import disable_tensorflow_debugging_info

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '4'
import tensorflow as tf

import os
import cv2
import numpy as np
from bob.paper.icb2019.gradgpad.test.test_utils import TestUtils
from bob.paper.icb2019.gradgpad.classes import MtcnnFaceDetector
from bob.paper.icb2019.gradgpad.classes.mtcnn.mtcnn_utils import _generate_scales, _run_Pnet_one_scale, nms, rerec, \
    pad, _run_Onet, _run_Rnet, _run_Pnet

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

SCALES_ASSET = [0.3, 0.21269999999999997, 0.15080429999999997, 0.10692024869999997,
                0.07580645632829998, 0.05374677753676469, 0.03810646527356616]

PNET_BOX_0 = [1.31000000e+02, 2.60000000e+01, 4.19000000e+02, 3.14000000e+02,
              9.87412810e-01, 3.18562388e-01, 1.33869708e-01, -1.14359379e-01,
              -1.38058633e-01]

disable_tensorflow_debugging_info()


class UnitTestMtcnnUtils(tf.test.TestCase):

    def setUp(self):
        tf.reset_default_graph()
        self.image = TestUtils.get_image_and_bbox("one_face.jpg")["image"]

    def tearDown(self):
        pass

    def test_scales_generation(self):
        scales = _generate_scales(self.image.shape, 40, 0.709)

        self.assertListEqual(SCALES_ASSET, scales)

    def test_run_pnet_one_scale(self):
        scale = SCALES_ASSET[-1]
        hs = int(np.ceil(self.image.shape[0] * scale))
        ws = int(np.ceil(self.image.shape[1] * scale))
        print("Scale h: ", hs)
        im = cv2.resize(self.image, (ws, hs), interpolation=cv2.INTER_AREA)

        with self.test_session() as sess:
            detector = MtcnnFaceDetector(sess)

        boxes = _run_Pnet_one_scale(detector.pnet, im, scale, 0.6)

        self.assertEqual(boxes.shape[0], 5)
        self.assertEqual(boxes.shape[1], 9)

        self.assertArrayNear(boxes[0, :], PNET_BOX_0, 0.000001)

    def test_nms_from_pnet(self):
        total_boxes = np.empty((0, 9))
        with self.test_session() as sess:
            detector = MtcnnFaceDetector(sess)
        scale = SCALES_ASSET[-1]
        hs = int(np.ceil(self.image.shape[0] * scale))
        ws = int(np.ceil(self.image.shape[1] * scale))
        im = cv2.resize(self.image, (ws, hs), interpolation=cv2.INTER_AREA)
        boxes = _run_Pnet_one_scale(detector.pnet, im, scale, 0.6)
        total_boxes = np.append(total_boxes, boxes, axis=0)
        filtered_boxes = nms(total_boxes.copy(), 0.5, 'Union')

        self.assertEqual(filtered_boxes.shape[0], 1)

    def test_region_to_square_rect(self):  # rerec function
        region_w = PNET_BOX_0[2] - PNET_BOX_0[0]
        region_h = PNET_BOX_0[3] - PNET_BOX_0[1]
        qq1 = PNET_BOX_0[0] + PNET_BOX_0[5] * region_w
        qq2 = PNET_BOX_0[1] + PNET_BOX_0[6] * region_h
        qq3 = PNET_BOX_0[2] + PNET_BOX_0[7] * region_w
        qq4 = PNET_BOX_0[3] + PNET_BOX_0[8] * region_h
        original_rec = np.transpose(np.vstack([qq1, qq2, qq3, qq4, PNET_BOX_0[4]]))

        original_h = original_rec[0, 3] - original_rec[0, 1]
        original_w = original_rec[0, 2] - original_rec[0, 0]
        max_orignal = np.max([original_h, original_w])

        square_rec = rerec(original_rec.copy())

        square_h = square_rec[0, 3] - square_rec[0, 1]
        square_w = square_rec[0, 2] - square_rec[0, 0]

        self.assertAlmostEquals(square_h, max_orignal)
        self.assertAlmostEquals(square_w, max_orignal)

    def test_pad_one_pixel_after_int_conversion(self):
        h = 3264
        w = 2448
        total_boxes = np.array([[5.73378663e+02, 1.07619298e+03, 2.28891714e+03, 2.79173146e+03, 6.11334085e-01]])
        total_boxes[:, 0:4] = np.fix(total_boxes[:, 0:4]).astype(np.int32)
        dy, edy, dx, edx, y, ey, x, ex, tmpw, tmph = pad(total_boxes.copy(), w, h)

        print('Box size: [ %d, %d ] : ' % (tmph[0], tmpw[0]))
        print('Region Patch: y: [ %d, %d ] --- x:  [ %d, %d ]' % (dy[0], edy[0], dx[0], edx[0]))
        print('Region Image: y: [ %d, %d ] --- x:  [ %d, %d ]' % (y[0], ey[0], x[0], ex[0]))

        self.assertEqual(tmph[0], 1716)
        self.assertEqual(tmpw[0], 1716)
        self.assertEqual(dy[0], 1)
        self.assertEqual(dx[0], 1)
        self.assertEqual(edy[0], 1716)
        self.assertEqual(edx[0], 1716)
        self.assertEqual(y[0], 1076)
        self.assertEqual(x[0], 573)
        self.assertEqual(ey[0], 2791)
        self.assertEqual(ex[0], 2288)

    def test_run_nets(self):
        with self.test_session() as sess:
            detector = MtcnnFaceDetector(sess)

        boxes_Pnet, proposals_batch = _run_Pnet(detector.pnet, self.image, SCALES_ASSET, 0.6)
        self.assertEqual(proposals_batch.shape, (24, 24, 3, 43))

        boxes_RNet, refined_proposals_batch = _run_Rnet(detector.rnet, boxes_Pnet, self.image, proposals_batch, 0.7)
        self.assertEqual(refined_proposals_batch.shape, (48, 48, 3, 3))

        boxes_ONet, landmarks, features = _run_Onet(detector.onet, boxes_RNet, refined_proposals_batch, 0.9)
        self.assertEqual(landmarks.shape, (10, 1))
        self.assertEqual(features.shape, (1, 256))


# def draw_rects(image_org, boxes):
#     image = image_org.copy()
#     for box in boxes:
#         cv2.rectangle(image, (int(box[0]), int(box[1])),
#                       (int(box[2]), int(box[3])), (255, 0, 0), 4)
#     # cv2.imwrite('/home/dpcabo/py_image.png', self.image)
#     image = cv2.resize(image, None, fx=0.3, fy=0.3)
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     cv2.imshow('image', image)
#     cv2.waitKey()

#
# def test_crop_face(self):
#     bboxes, face_landmarks, scores, dnorm_scores = self.detector.detect(self.image)
#     raw_faces = self.detector.crop_faces(self.image,bboxes,False)
#     square_faces = self.detector.crop_faces(self.image,bboxes,True)
#
#     self.assertEqual(len(bboxes),len(raw_faces))
#     self.assertEqual(len(bboxes), len(square_faces))
#
#     # for i in range(len(bboxes)):
#     #     f = plt.figure()
#     #     plt.imshow(raw_faces[i])
#     #     plt.title('Raw Face %d' % (i+1))
#     #     ff = plt.figure()
#     #     plt.imshow(square_faces[i])
#     #     plt.title('Square Face %d' % (i + 1))
#     #     plt.show()


if __name__ == '__main__':
    tf.test.main()
