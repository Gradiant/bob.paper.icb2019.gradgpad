import numpy as np

from bob.paper.icb2019.gradgpad.classes import meet_the_restrictions


def annotations_meet_the_restrictions(annotations, min_annotations, minimum_size_valid=70):
    counter = 0
    for key, annotation in annotations.items():
        if meet_the_restrictions(annotation, minimum_size_valid=minimum_size_valid):
            counter += 1
    return counter >= min_annotations


def get_averaged_annotation(annotations):
    accumulated_bbox = np.zeros(4)
    accumulated_landmarks = np.zeros(5 * 2)  # 5 landmarks
    accumulated_confidence = np.zeros(1)
    counter = 0
    for _, annotation in annotations.items():
        if annotation and meet_the_restrictions(annotation):
            accumulated_bbox += annotation['bbox']
            accumulated_landmarks += annotation['landmarks']
            accumulated_confidence += annotation['confidence']
            counter += 1
    counter = max(1, counter)
    return {'bbox': accumulated_bbox / counter,
            'landmarks': accumulated_landmarks / counter,
            'confidence': accumulated_confidence / counter}


def rescale_annotation(annotation, rescale_factor):
    return {'bbox': annotation['bbox'] * rescale_factor,
            'landmarks': annotation['landmarks'] * rescale_factor,
            'confidence': annotation['confidence']}
