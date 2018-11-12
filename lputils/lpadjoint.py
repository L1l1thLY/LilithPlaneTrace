import numpy as np


class LPAdjoint(object):
    def __init__(self, distance, ratio, time = 0):
        self.distance = distance
        self.time = time
        self.ratio = ratio

    def is_adjoint(self, bezier1, bezier2):

        adjoint_point = 0
        all_point = 0
        for index, value in enumerate(bezier1['xs']):
            vector1 = np.array([value, bezier1['ys'][index]])
            vector1.reshape((2, 1))
            vector2 = np.array([bezier2['xs'][index], bezier2['ys'][index]])
            vector2.reshape((2, 1))
            if np.linalg.norm(vector1 - vector2) < self.distance:
                adjoint_point = adjoint_point + 1
            all_point = all_point + 1

        if adjoint_point / all_point > self.ratio:
            return True
        else:
            return False

