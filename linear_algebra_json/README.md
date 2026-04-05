# python读取.json文件数据并进行计算
## 项目简介

实现了基于 Python 的高维向量坐标系计算工具，支持：

坐标系变换
向量投影
向量与坐标轴夹角
坐标系面积计算
支持任意维度

---

## 项目结构

```
linear_algebra_json/
│
├── data.json              # JSON数据
│
├── coordinate_system.py   # 坐标系类
├── task_processor.py      # 任务执行
├── main.py                # 主程序入口
│
├── README.md                  # 项目说明
└── requirements.txt           # 依赖           

```

---

## 使用方法

### 1. 安装依赖

```
pip install -r requirements.txt
```

### 2. 运行程序

```
cd src
python main.py
```

---

## 核心原理

坐标变换：x'= B⁻¹x
投影：dot product
夹角：cosθ = (a·b)/(|a||b|)
面积：|det(B)|

---

## 特性

支持高维
面向对象设计
自动检测坐标系合法性

---

## 作者
MaHaoran