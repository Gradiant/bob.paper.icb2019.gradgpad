import numpy as np


def get_bounding_box_from_annotations(annotation):
    if 'bbox' not in annotation:
        raise ValueError("bbox is not on annotations")
    bounding_box = annotation['bbox']
    return int(bounding_box[1]), \
           int(bounding_box[0]), \
           int(bounding_box[3]), \
           int(bounding_box[2])


def crop_from_bbox(image, bbox):
    bbox[0] = max(0, bbox[0])
    bbox[1] = max(0, bbox[1])
    bbox[2] = min(image.shape[0], bbox[2])
    bbox[3] = min(image.shape[1], bbox[3])

    bbox = bbox.astype(int)

    return image[bbox[0]:bbox[2], bbox[1]:bbox[3], :]


def crop_image(image, annotation):
    if 'bbox' not in annotation:
        raise ValueError("bbox is not on annotations")

    bbox = annotation['bbox']
    return crop_from_bbox(image, bbox)


def crop_square_face(image, annotation):
    bbox = annotation['bbox']

    h = min(bbox[2], image.shape[0]) - max(bbox[0], 0)
    w = min(bbox[3], image.shape[1]) - max(bbox[1], 0)
    largest = max(h, w)
    center_y = bbox[0] + h / 2
    center_x = bbox[1] + w / 2
    top = center_y - largest / 2
    bottom = center_y + largest / 2
    left = center_x - largest / 2
    right = center_x + largest / 2
    square_box = np.array([top, left, bottom, right])
    return crop_from_bbox(image, square_box)


def meet_the_restrictions(annotation, minimum_size_valid=70):
    x1, y1, x2, y2 = get_bounding_box_from_annotations(annotation)
    x_side_size = x2 - x1
    y_side_size = y2 - y1

    if min(x_side_size, y_side_size) > minimum_size_valid:
        return True
    else:
        return False
