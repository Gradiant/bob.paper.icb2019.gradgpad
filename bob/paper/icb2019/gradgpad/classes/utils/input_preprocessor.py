import numpy as np
from PIL import Image


def input_resize_preprocessor(input_image_array, max_image_size_lowest_side):
    input_image = Image.fromarray(input_image_array.astype('uint8'))
    width = input_image.width
    height = input_image.height
    scale_factor = 1.0
    if height > max_image_size_lowest_side and width > max_image_size_lowest_side:
        if height > width:
            scale_factor = float(max_image_size_lowest_side) / width
        else:
            scale_factor = float(max_image_size_lowest_side) / height
    size = (int(scale_factor * width), int(scale_factor * height))
    resized_io_frame = input_image.resize(size, Image.ANTIALIAS)
    output_image = np.array(resized_io_frame)
    return output_image, scale_factor


def rescale_bounding_boxes(bounding_boxes, scale_factor):
    if scale_factor == 1.0:
        return bounding_boxes
    rescaled_bounding_boxes = []
    for bounding_box in bounding_boxes:
        rescaled_bounding_box = [i / scale_factor for i in bounding_box]
        rescaled_bounding_boxes.append(rescaled_bounding_box)
    return rescaled_bounding_boxes


def rescale_landmarks(landmarks, scale_factor):
    if scale_factor == 1.0:
        return landmarks
    rescaled_landmarks = []
    for landmark in landmarks:
        rescaled_point_landmarks = []
        for point in landmark:
            rescaled_point_landmark = [i / scale_factor for i in point]
            rescaled_point_landmarks.append(rescaled_point_landmark)
        rescaled_landmarks.append(rescaled_point_landmarks)
    return rescaled_landmarks
