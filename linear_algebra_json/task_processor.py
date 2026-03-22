import numpy as np
from coordinate_system import CoordinateSystem   #导入坐标系类

# 美化输出函数
def format_num(x, decimals=2):
    #格式化数字，保留两位小数
    if isinstance(x, np.float64):
        x = float(x)
    return f"{x:.{decimals}f}"

def format_vector(vec, decimals=2):
    #格式化向量/列表，
    return "[" + ", ".join([format_num(v, decimals) for v in vec]) + "]"

#任务处理类
class TaskProcessor:
    def __init__(self, data):  #接收 JSON 数据并储存
        self.groups = data

    def run(self):
    #"""执行所有任务"""
     for group in self.groups:
        # 打印分组标题
        print(f"\n========= {group['group_name']} =========")
        
        # 初始化向量和坐标系
        vectors = [np.array(v, dtype=float) for v in group["vectors"]]
        coord = CoordinateSystem(group["ori_axis"])
        
        # 遍历分组内任务
        for task in group["tasks"]:
            t = task["type"]  # 判断要执行的任务
            
            if t == "change_axis":
                # 创建新坐标系并进行坐标变换
                new_coord = CoordinateSystem(task["obj_axis"])
                transformed_vectors = new_coord.change_coordinates(vectors)
                print("\n坐标系转换完成 (新坐标系基向量: {})".format(task["obj_axis"]))
                print("变换后的坐标:")
                for i, v in enumerate(transformed_vectors, 1):
                    print(f"  v{i}': {format_vector(v)}")
                # 更新vectors为变换后的结果，以便后续任务使用
                vectors = transformed_vectors
                coord = new_coord
                
            elif t == "axis_projection":
                proj_list = coord.projection(vectors)
                print("\n坐标系投影:")
                print("  原始向量 -> 投影结果")
                for i, (orig, proj) in enumerate(zip(vectors, proj_list), 1):
                    print(f"  v{i}: {format_vector(orig)} -> {format_vector(proj)}")
                    
            elif t == "axis_angle":
                angle_list = coord.angle(vectors)
                print("\n坐标系夹角 :")
                print("  向量\t与x轴夹角\t与y轴夹角")
                for i, (v, angles) in enumerate(zip(vectors, angle_list), 1):
                    if len(angles) >= 2:
                        print(f"  v{i}: {format_vector(v)}\t{angles[0]:.2f}°\t\t{angles[1]:.2f}°")
                    else:
                        print(f"  v{i}: {format_vector(v)}\t{angles[0]:.2f}°")
            elif t == "area":
                    area_val = coord.area()
                    print(f"坐标系面积: {format_num(area_val, decimals=2)}")            

    def _task_area(self):
        """面积计算任务：基于变换后的坐标系"""
        if self.transformed_coord is None:
            print("错误：未执行坐标变换，无法计算面积")
            return
        
        area_val = self.transformed_coord.area()
        print(f"变换后坐标系面积：{format_num(area_val)}")
        print()

    def _task_axis_projection(self):
        """投影计算任务：变换后向量在新坐标轴上的投影"""
        if self.transformed_coord is None or self.transformed_vectors is None:
            print("错误：未执行坐标变换，无法计算投影")
            return
        
        proj_list = self.transformed_coord.projection(self.transformed_vectors)
        
        print("变换后向量 - 新坐标轴投影:")
        print("  变换后向量 -> 投影结果")
        for i, (vec, proj) in enumerate(zip(self.transformed_vectors, proj_list), 1):
            vec_str = format_vector(vec)
            proj_str = format_vector(proj)
            print(f"v{i}: {vec_str} -> {proj_str}")
        print()