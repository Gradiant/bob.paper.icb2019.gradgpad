import numpy as np


def calculate_coalbp_features(image, lbp_r=1, co_r=2):
    """
    Co-occurrence of Adjacent Local Binary Patterns algorithm
    Input image with shape (height, width, channels)
    Input lbp_r is radius for adjacent local binary patterns
    Input co_r is radius for co-occurence of the patterns
    Output features with length 1024 * number of channels
    """
    h, w, c = image.shape
    # normalize face
    image = (image - np.mean(image, axis=(0, 1))) / (np.std(image, axis=(0, 1)) + 1e-8)
    # albp and co-occurrence per channel in image
    histogram = np.empty(0, dtype=np.int)
    for i in range(image.shape[2]):
        C = image[lbp_r:h - lbp_r, lbp_r:w - lbp_r, i].astype(float)
        X = np.zeros((4, h - 2 * lbp_r, w - 2 * lbp_r))
        # adjacent local binary patterns
        X[0, :, :] = image[lbp_r:h - lbp_r, lbp_r + lbp_r:w - lbp_r + lbp_r, i] - C
        X[1, :, :] = image[lbp_r - lbp_r:h - lbp_r - lbp_r, lbp_r:w - lbp_r, i] - C
        X[2, :, :] = image[lbp_r:h - lbp_r, lbp_r - lbp_r:w - lbp_r - lbp_r, i] - C
        X[3, :, :] = image[lbp_r + lbp_r:h - lbp_r + lbp_r, lbp_r:w - lbp_r, i] - C
        X = (X > 0).reshape(4, -1)
        # co-occurrence of the patterns
        A = np.dot(np.array([1, 2, 4, 8]), X)
        A = A.reshape(h - 2 * lbp_r, w - 2 * lbp_r) + 1
        hh, ww = A.shape
        D = (A[co_r:hh - co_r, co_r:ww - co_r] - 1) * 16 - 1
        Y1 = A[co_r:hh - co_r, co_r + co_r:ww - co_r + co_r] + D
        Y2 = A[co_r - co_r:hh - co_r - co_r, co_r + co_r:ww - co_r + co_r] + D
        Y3 = A[co_r - co_r:hh - co_r - co_r, co_r:ww - co_r] + D
        Y4 = A[co_r - co_r:hh - co_r - co_r, co_r - co_r:ww - co_r - co_r] + D
        Y1 = np.bincount(Y1.ravel(), minlength=256)
        Y2 = np.bincount(Y2.ravel(), minlength=256)
        Y3 = np.bincount(Y3.ravel(), minlength=256)
        Y4 = np.bincount(Y4.ravel(), minlength=256)
        pattern = np.concatenate((Y1, Y2, Y3, Y4))
        histogram = np.concatenate((histogram, pattern))
    # normalize the histogram and return it
    features = (histogram - np.mean(histogram)) / np.std(histogram)
    return features
