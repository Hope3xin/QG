# coordinate_system.py
import numpy as np

class CoordinateSystem:
    """坐标系类 - 处理坐标系变换、投影、角度计算等功能"""
    
    # 构造函数（双下划线，拼写正确）
    def __init__(self, axis):
        """
        初始化坐标系
        :param axis: 坐标系的轴向量组成的方阵（numpy数组/列表）
        """
        self.axis = np.array(axis, dtype=float)
        
        # 验证矩阵是方阵
        if self.axis.shape[0] != self.axis.shape[1]:
            raise ValueError("坐标轴必须为方阵（行数和列数相等）")
        
        # 验证矩阵可逆（行列式不为0）
        if abs(np.linalg.det(self.axis)) < 1e-8:
            raise ValueError("坐标系矩阵不可逆（行列式为0），无法作为坐标系")

    def change_coordinates(self, vectors):
        """
        坐标变换 - 将向量转换到当前坐标系下
        :param vectors: 待变换的向量列表
        :return: 变换后的向量列表
        """
        inv_axis = np.linalg.inv(self.axis)
        return [inv_axis @ np.array(v, dtype=float) for v in vectors]

    def projection(self, vectors):
        """
        向量投影 - 计算向量在各坐标轴上的投影
        :param vectors: 待投影的向量列表
        :return: 投影结果列表
        """
        result = []
        for v in vectors:
            vec = np.array(v, dtype=float)
            proj = []
            for axis in self.axis:
                # 计算投影值
                proj_val = np.dot(vec, axis) / np.linalg.norm(axis)
                proj.append(proj_val)
            result.append(proj)
        return result

    def angle(self, vectors):
        """
        角度计算 - 计算向量与各坐标轴的夹角（弧度）
        :param vectors: 待计算的向量列表
        :return: 夹角列表（弧度）
        """
        result = []
        for v in vectors:
            vec = np.array(v, dtype=float)
            angles = []
            for axis in self.axis:
                # 计算余弦值并限制范围（避免数值误差导致arccos报错）
                cos_theta = np.dot(vec, axis) / (np.linalg.norm(vec) * np.linalg.norm(axis))
                cos_theta = np.clip(cos_theta, -1.0, 1.0)
                angles.append(np.arccos(cos_theta))
            result.append(angles)
        return result

    def area(self):
        """计算坐标系的面积/体积（行列式的绝对值）"""
        return abs(np.linalg.det(self.axis))