import cv2
from bob.paper.icb2019.gradgpad.classes.utils.crop_image import meet_the_restrictions, crop_square_face

DEFAULT_NORMALIZED_FACE_SIZE = (64, 64)


def check_bounding_box_integrity(annotation, im_shape):
    bbox = annotation['bbox']
    is_ok = True
    if bbox[0] < 0 or bbox[1] < 0 or bbox[2] > im_shape[0] or bbox[3] > im_shape[1]:
        is_ok = False
    if bbox[2] - bbox[0] <= 0 or bbox[3] - bbox[1] <= 0:
        is_ok = False
    return is_ok


def preprocess_image(image, annotation, normalized_face_size=DEFAULT_NORMALIZED_FACE_SIZE, minimum_size_valid=70):
    if not meet_the_restrictions(annotation, minimum_size_valid=minimum_size_valid):
        return None
    if not check_bounding_box_integrity(annotation, image.shape):
        return None

    cropped_image = crop_square_face(image, annotation)

    preprocessed_image = cv2.resize(cropped_image, normalized_face_size, interpolation=cv2.INTER_CUBIC)
    return preprocessed_image


def normalize(image):
    normalized_image = image - image.min()
    if normalized_image.max() != 0:
        normalized_image = normalized_image / normalized_image.max()
    return normalized_image


def resize_image_with_side_target_size(np_image, side_target_size):
    height, width = np_image.shape[:2]
    scale_factor = 1
    if height > side_target_size or width > side_target_size:
        if height > width:
            scale_factor = float(side_target_size) / height
        else:
            scale_factor = float(side_target_size) / width
    size = (int(scale_factor * width), int(scale_factor * height))
    resized_image = cv2.resize(np_image, size, interpolation=cv2.INTER_CUBIC)
    return resized_image, scale_factor
