## 一、机器学习基本概念

机器学习：属于人工智能领域，计算机**从数据中自动学习规律**，不断积累经验，能够自动完善、优化程序，实现所需性能的提高。

监督学习:输入包含样本数据的特征和标签,从正确答案学习并建立模型，用于预测标签。

无监督学习(非监督学习)：输入样本只有特征，没有标签，自动地从样本中学习，以实现预测。

强化学习：通过**与环境互动、试错**，并根据获得的**奖励或惩罚**来学习最优策略的机器学习方法。

| 类型       | 数据形式         | 学习方式                                                     |
| :--------- | :--------------- | :----------------------------------------------------------- |
| 监督学习   | 特征, 标签       | 从正确答案学习                                               |
| 无监督学习 | 只有特征         | 自己寻找规律                                                 |
| 强化学习   | 状态, 动作, 奖励 | 试错+奖励**训练集** = 模型“见过并学习”的数据。拟合 = 模型在这组数据上降低误差的过程。 |

**训练集** ： 模型“见过并学习”的数据。

**验证集** ： 模型“没见过但人用它做决定”的数据。人观察模型在验证集上的表现，然后调整超参数（如学习率、网络层数）。模型本身不直接从验证集学习参数 θ。

**测试集** ：模型“从未见过，人也不用它做决定”的数据。仅在项目结束时使用，用于反馈“模型好不好”。

**拟合** ：训练集误差下降，优化的过程。拟合完成 ≠ 模型好。

**过拟合**：模型把训练数据里的偶然巧合当成了规律加入训练。

**泛化** ：模型在测试集上的表现能力。泛化好 = 训练集误差低 ， 测试集误差低。

**模型评估指标** ：测量泛化能力。不同模型测量不同维度。



## 二、监督学习

### 线性模型

#### 线性回归

**实质**：使用线性参数来建立因变量与一个或者多个自变量之间的关系。

【！】对于参数是线性的，不一定是直线（如多项式回归）



**特点**：

①自变量和因变量之间是线性关系。

②**多重共线性**，自相关和异方差对多元线性回归的影响均较大。

③线性回归对异常值非常敏感，异常值会影响预测的结果。

④当同时处理的自变量较多时，需要使用**逐步回归**的方式来逐步确定显著性变量，而无需人工干预



**核心思想：**

逐个引入自变量至模型中，并**f检验，t检验**等来对变量进行筛选，当新的变量被引入且模型的结果不能得到优化时，对该变量进行消除，直至模型的结果相对稳定为止。



**逐步回归**的目的：

选择较少的、重要的自变量来实现具有最大化预测能力的模型。



**选择变量方法：**

①首先选择**最显著**的变量，之后逐渐增加次显著变量；

②首先选择所有的变量，并且**逐渐剔除不重要**的变量。



**公式推导：**

单变量:
$$
\hat{y} = wx + b
$$
损失函数:
$$
MSE = J(w,b) = \frac{1}{n} \sum_{i=1}^n (\hat{y}_i - y_i)^2
$$

$$
\frac{\partial J}{\partial b} = \frac{2}{n} \sum_{i=1}^n (w x_i + b - y_i) = 0
$$

$$
\sum_{i=1}^n (w x_i + b - y_i) = 0
$$

$$
w \sum_{i=1}^n x_i + n b - \sum_{i=1}^n y_i = 0
$$

$$
w \sum_{i=1}^n x_i + n b - \sum_{i=1}^n y_i = 0
$$

$$
\bar{y} = \frac{1}{n} \sum_{i=1}^n y_i
$$

$$
w n \bar{x} + n b - n \bar{y} = 0
$$

$$
\frac{\partial J}{\partial w} = \frac{2}{n} \sum_{i=1}^n (w x_i + b - y_i) x_i = 0
$$

$$
b = \bar{y} - w \bar{x} (1)
$$

将（1）代入：
$$
w \sum_{i=1}^n x_i(x_i - \bar{x}) - \sum_{i=1}^n x_i(y_i - \bar{y}) = 0
$$
又
$$
\sum_{i=1}^n x_i(x_i - \bar{x}) = \sum_{i=1}^n (x_i - \bar{x})^2
$$

$$
\sum_{i=1}^n x_i(y_i - \bar{y}) = \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})
$$

得
$$
w = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}
$$


#### **逻辑回归**

**本质：线性回归+激活函数**

**特点：**

用于解决分类问题（如判断"是 / 否"），输出的是概率。

构建取值0-1的σ函数，把线性回归输出得到的值传入Sigmoid函数σ(y)，映射为概率。设置阈值，根据阈值做出判断。

训练目标 ： 让预测概率尽可能接近真实标签

损失函数：
$$
\mathcal{L}(y, \hat{y}) =
\begin{cases}
-\log(\hat{y}) & y = 1 \\
-\log(1 - \hat{y}) & y = 0
\end{cases}
$$


**公式推导：**

Sigmoid 激活函数：
$$
\sigma(y)=\frac{1}{1+e^{-y}}
$$

$$
\hat{y}=\sigma(wx+b)=\frac{1}{1+e^{-(wx+b)}}
$$

$$
L(w,b)=\prod_{i=1}^{n}P(y_i|x_i)
$$

$$
\ln L(w,b)=\sum_{i=1}^{n}\big[y_i\ln\hat{y}_i+(1-y_i)\ln(1-\hat{y}_i)\big]
$$

$$
J(w,b)=-\frac{1}{n}\sum_{i=1}^{n}\big[y_i\ln\hat{y}_i+(1-y_i)\ln(1-\hat{y}_i)\big]
$$

$$
\frac{\partial J}{\partial w}
=-\frac{1}{n}\sum_{i=1}^{n}\frac{\partial}{\partial w}\big[
y_i\ln\hat{y}_i+(1-y_i)\ln(1-\hat{y}_i)
\big]
$$

$$
\frac{\partial J}{\partial w}
\frac{\partial J}{\partial w}=\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i-y_i)x_i
$$

$$
\frac{\partial J}{\partial b}=\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i-y_i)
$$

$$
w=w-\alpha\frac{\partial J}{\partial w},\quad
b=b-\alpha\frac{\partial J}{\partial b}
$$





#### 线性回归&**逻辑回归**不同点对比

| 对比项           | 线性回归             | 逻辑回归                   |
| ---------------- | -------------------- | -------------------------- |
| **任务类型**     | 回归（预测连续值）   | 预测概率/类别判断          |
| **模型输出**     | 任意实数             | 概率（0，1）               |
| **损失函数**     | 均方误差 (MSE)       | 二元交叉熵 ( 负对数似然)   |
| **参数求解**     | 方程 / 梯度下降      | 梯度下降                   |
| **异常值敏感度** | 非常敏感             | 相对不敏感                 |
| **典型应用**     | 预测、拟合、趋势估计 | 分类、点击率预测、风险判断 |

## 三、无监督学习

### K-Means聚类模型

**介绍：**

样本点映射到欧氏空间中，用距离远近衡量近似程度。

cluster：分的每一类

centroid：“中心”，cluster中样本坐标均值

**具体过程：**

1.随机选取n组样本，初始化cluster。（n个cluster）

2.剩下的样本点依次映射到欧氏空间中，计算离哪个cluster的centroid更近，进行归类，然后更新cluster的centroid

3.重复。直到加入样本后每个cluster的centroid位置不再发生变化。

4.新的样本直接计算离哪个cluster更近，直接归类。



**推导K-Means算法公式**:

目标函数（内平方和 SSE）:
$$
J = \sum_{k=1}^K \sum_{\boldsymbol{x}_i \in C_k} \|\boldsymbol{x}_i - \boldsymbol{\mu}_k\|^2
$$
欧氏距离
$$
\|\boldsymbol{x}_i - \boldsymbol{\mu}_k\|^2 = (\boldsymbol{x}_i - \boldsymbol{\mu}_k)^\top (\boldsymbol{x}_i - \boldsymbol{\mu}_k)
$$

$$
\frac{\partial J}{\partial \boldsymbol{\mu}_k} = \sum_{\boldsymbol{x}_i \in C_k} 2(\boldsymbol{x}_i - \boldsymbol{\mu}_k)(-1) = -2\sum_{\boldsymbol{x}_i \in C_k} (\boldsymbol{x}_i - \boldsymbol{\mu}_k)
$$

令梯度为0,得：
$$
-2\sum_{\boldsymbol{x}_i \in C_k} (\boldsymbol{x}_i - \boldsymbol{\mu}_k) = 0
$$
cluster内样本和与中心的关系：
$$
\sum_{\boldsymbol{x}_i \in C_k} \boldsymbol{x}_i = |C_k| \cdot \boldsymbol{\mu}_k
$$
中心：
$$
\boldsymbol{\mu}_k = \frac{1}{|C_k|} \sum_{\boldsymbol{x}_i \in C_k} \boldsymbol{x}_i
$$
定义：
$$
z_{ik} =
\begin{cases}
1, & k = \arg\min_j \|\boldsymbol{x}_i - \boldsymbol{\mu}_j\|^2 \\
0, & \text{else}
\end{cases}
$$

$$
J = \sum_{i=1}^N \sum_{k=1}^K z_{ik} \|\boldsymbol{x}_i - \boldsymbol{\mu}_k\|^2
$$

**算法优点：**

不需要样本的标注就能训练模型。

**算法缺点：**

性能不如监督学习。

准确度受限因素多。

对初始n的选择很敏感。（不同的n，分类结果完全不同）

对数据集的分布很敏感。（初始数据选择很重要）



### PCA（主成分分析）降维技术

#### **计算过程：**

中心化数据

协方差矩阵

特征向量

特征值最大的特征向量为主成分

投影

#### **PCA 在缓解“维度灾难”及数据预处理中的作用：**

**PCA 对维度灾难的缓解机制**

维度灾难的核心问题：当特征的维度增大时，样本稀疏性增加、距离度量失效、泛化误差恶化。

作用：

1.降低有效维度

2.丢弃小特征值方向,主要反映噪声

3.恢复高维空间中的距离度量区分能力



**PCA 在数据预处理中的作用**

1.消除共线性

2.复杂度降低，计算加速（如 K-Means）

3.通过秩约束降低方差，减小测试误差

4.维度d=2，3 可实现聚类结构与异常检测的低维可视化

5.存储量压缩



机器学习 学习资源：[机器学习入门基础（万字总结）（建议收藏！！！）-CSDN博客](https://blog.csdn.net/m0_65121454/article/details/128178708?ops_request_misc=elastic_search_misc&request_id=ddad40927161b1fa4765eeb78af3d1df&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-128178708-null-null.142^v102^pc_search_result_base8&utm_term=机器学习&spm=1018.2226.3001.4187)