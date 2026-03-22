import numpy as np
#定义坐标系类
class CoordinateSystem:
    def __init__(self, axis):
        self.axis = np.array(axis, dtype=float)

        if self.axis.shape[0] != self.axis.shape[1]:
            raise ValueError("坐标轴必须为方阵")

        if abs(np.linalg.det(self.axis)) < 1e-8:
            raise ValueError("坐标系不可逆")

    def change_coordinates(self, vectors):
        inv = np.linalg.inv(self.axis)
        return [inv @ v for v in vectors]

    def projection(self, vectors):
        result = []
        for v in vectors:
            proj = []
            for axis in self.axis:
                proj.append(np.dot(v, axis) / np.linalg.norm(axis))
            result.append(proj)
        return result

    def angle(self, vectors):
        result = []
        for v in vectors:
            angles = []
            for axis in self.axis:
                cos_theta = np.dot(v, axis) / (
                    np.linalg.norm(v) * np.linalg.norm(axis)
                )
                cos_theta = np.clip(cos_theta, -1, 1)
                angles.append(np.arccos(cos_theta))
            result.append(angles)
        return result

    def area(self):
        return abs(np.linalg.det(self.axis))