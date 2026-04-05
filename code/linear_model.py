import numpy as np
import pandas as pd

# 加载数据集
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(url, sep=";")

X = data.iloc[:, :-1].values
y_linear = data.iloc[:, -1].values
y_logistic = (y_linear > 6).astype(int)

# 划分训练集和测试集
np.random.seed(66)
indices = np.random.permutation(len(X))
split = int(0.8 * len(X))
train_idx, test_idx = indices[:split], indices[split:]

X_train, X_test = X[train_idx], X[test_idx]
y_train_lin, y_test_lin = y_linear[train_idx], y_linear[test_idx]
y_train_log, y_test_log = y_logistic[train_idx], y_logistic[test_idx]

# 标准化 + 偏置项
def standardize(X_train, X_test):
    mean = np.mean(X_train, axis=0)
    std = np.std(X_train, axis=0)
    std[std == 0] = 1
    X_train_std = (X_train - mean) / std
    X_test_std = (X_test - mean) / std
    X_train_std = np.hstack([np.ones((X_train_std.shape[0], 1)), X_train_std])
    X_test_std = np.hstack([np.ones((X_test_std.shape[0], 1)), X_test_std])
    return X_train_std, X_test_std

X_train, X_test = standardize(X_train, X_test)

# 线性回归
class LinearRegression:
    def __init__(self, lr=0.01, epochs=20000):
        self.lr = lr
        self.epochs = epochs
        self.theta = None

    def fit(self, X, y):
        m, n = X.shape
        self.theta = np.zeros(n)
        losses = []
        for i in range(self.epochs):
            y_pred = X @ self.theta
            loss = np.mean((y_pred - y) ** 2) / 2
            grad = (X.T @ (y_pred - y)) / m
            self.theta -= self.lr * grad
            losses.append(loss)
            if i > 1 and abs(losses[-1] - losses[-2]) < 1e-7:
                break
        return losses

    def predict(self, X):
        return X @ self.theta

# 逻辑回归
class LogisticRegression:
    def __init__(self, lr=0.01, epochs=20000):
        self.lr = lr
        self.epochs = epochs
        self.theta = None

    def sigmoid(self, z):
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        m, n = X.shape
        self.theta = np.zeros(n)
        losses = []
        for i in range(self.epochs):
            z = X @ self.theta
            y_pred = self.sigmoid(z)
            loss = -np.mean(y * np.log(y_pred + 1e-8) + (1 - y) * np.log(1 - y_pred + 1e-8))
            grad = (X.T @ (y_pred - y)) / m
            self.theta -= self.lr * grad
            losses.append(loss)
            if i > 1 and abs(losses[-1] - losses[-2]) < 1e-7:
                break
        return losses

    def predict(self, X, threshold=0.5):
        prob = self.sigmoid(X @ self.theta)
        return (prob >= threshold).astype(int)

# 训练
model_lin = LinearRegression(lr=0.01)
model_lin.fit(X_train, y_train_lin)
y_pred_lin = model_lin.predict(X_test)

model_log = LogisticRegression(lr=0.01)
model_log.fit(X_train, y_train_log)
y_pred_log = model_log.predict(X_test)

# 评估指标
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

def r2(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1 - ss_res / ss_tot

def accuracy(y_true, y_pred):
    return np.sum(y_true == y_pred) / len(y_true)


print("线性回归测试结果：")
print("MSE =", round(mse(y_test_lin, y_pred_lin), 4))
print("R^2  =", round(r2(y_test_lin, y_pred_lin), 4))

print("================")

print("逻辑回归测试结果：")
print("准确率 =", round(accuracy(y_test_log, y_pred_log), 4))