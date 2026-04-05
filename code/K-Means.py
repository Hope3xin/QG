# 导入必要的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.preprocessing import StandardScaler

# ======================================
# 1. 加载鸢尾花数据集
# ======================================
iris = load_iris()
X = iris.data  # 特征数据：花萼长度、花萼宽度、花瓣长度、花瓣宽度
y = iris.target  # 真实标签（仅用于评估，聚类不使用）
feature_names = iris.feature_names
target_names = iris.target_names

print("="*50)
print("数据集基本信息：")
print(f"样本数量: {X.shape[0]}")
print(f"特征数量: {X.shape[1]}")
print(f"特征名称: {feature_names}")
print(f"类别名称: {target_names}")
print(f"真实类别分布: {np.bincount(y)}")
print("="*50)

# ======================================
# 2. 数据预处理（标准化，消除量纲影响）
# ======================================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("\n✅ 数据标准化完成")

# ======================================
# 3. 确定最佳聚类数K（肘部法则 + 轮廓系数）
# ======================================
inertia = []
silhouette_scores = []
k_range = range(2, 10)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# 绘制肘部法则+轮廓系数图
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(k_range, inertia, 'bo-', linewidth=2)
plt.xlabel('聚类数 K', fontsize=12)
plt.ylabel('簇内平方和 (Inertia)', fontsize=12)
plt.title('肘部法则确定最佳K值', fontsize=14)
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(k_range, silhouette_scores, 'ro-', linewidth=2)
plt.xlabel('聚类数 K', fontsize=12)
plt.ylabel('轮廓系数 (Silhouette Score)', fontsize=12)
plt.title('轮廓系数确定最佳K值', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ======================================
# 4. 训练K-Means模型（K=3，与真实类别数一致）
# ======================================
k = 3
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
y_pred = kmeans.fit_predict(X_scaled)

print("\n" + "="*50)
print(f"✅ K-Means聚类完成，聚类数K={k}")
print(f"聚类中心(标准化后):\n{kmeans.cluster_centers_}")
print(f"聚类结果分布: {np.bincount(y_pred)}")
print("="*50)

# ======================================
# 5. 模型评估
# ======================================
ari = adjusted_rand_score(y, y_pred)
sil_score = silhouette_score(X_scaled, y_pred)

print(f"\n📊 模型评估指标:")
print(f"调整兰德指数 (Adjusted Rand Index): {ari:.4f}")
print(f"轮廓系数 (Silhouette Score): {sil_score:.4f}")

# ======================================
# 6. 可视化聚类结果
# ======================================
# 花瓣长度 vs 花瓣宽度（区分度更高）
plt.figure(figsize=(12, 5))

# 真实标签可视化
plt.subplot(1, 2, 1)
for i, target_name in enumerate(target_names):
    plt.scatter(X[y == i, 2], X[y == i, 3], label=target_name, alpha=0.7, s=50)
plt.xlabel(feature_names[2], fontsize=12)
plt.ylabel(feature_names[3], fontsize=12)
plt.title('鸢尾花数据集真实类别', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# 聚类结果可视化
plt.subplot(1, 2, 2)
for i in range(k):
    plt.scatter(X[y_pred == i, 2], X[y_pred == i, 3], label=f'Cluster {i+1}', alpha=0.7, s=50)
# 反标准化聚类中心到原始尺度
centers = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centers[:, 2], centers[:, 3], c='black', s=200, alpha=0.8, marker='X', label='聚类中心')
plt.xlabel(feature_names[2], fontsize=12)
plt.ylabel(feature_names[3], fontsize=12)
plt.title('K-Means聚类结果 (K=3)', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ======================================
# 7. 输出聚类结果详情
# ======================================
result_df = pd.DataFrame(X, columns=feature_names)
result_df['真实类别'] = [target_names[i] for i in y]
result_df['聚类标签'] = [f'Cluster {i+1}' for i in y_pred]

print("\n" + "="*50)
print("📋 聚类结果前10行预览:")
print(result_df.head(10))
print("="*50)