# -*- coding: utf-8 -*-
__author__ = 'wangwenjie'
__data__ = '2018/6/7 上午9:37'
__product__ = 'PyCharm'
__filename__ = 'numpy_introduction'

""" Numpy 入门 """

import numpy as np

# 1,创建数组方式: array zeros ones empty arange linspace logspace random

# a.将列表转数组
a1 = np.array([[1, 2, 3, 4], [4, 5, 5, 3], [6, 3, 8, 7]], dtype=np.float)
print(a1)


# b. 0矩阵
b1 = np.zeros((3, 4, 5), dtype=np.int)
print('b1:\n', b1)

# c. 1 矩阵
c1 = np.ones((3, 5))
print('c1:\n', c1)

# d. 空 矩阵
d1 = np.empty((4, 4))
print('d1:\n', d1)

# e. range
e1 = np.arange(1, 10, 3, np.int)
print('f1:\n', e1)

# f. 线性数列
f, _ = np.linspace(1, 10, 6, endpoint=False, retstep=True)
print('f:\n', f)

# g. 对数
g = np.logspace(1, 32, 6)
print('g:\n', g)

# h. 随机

# h1. 均匀分布
h = np.random.randint(10, 20, (2, 3, 4))
np.random.ranf()  # [0.0, 1.0)
np.random.rand()  # [0.0, 1.0]
np.random.random()  # [0.0, 1.0)

# h2. 正态分布
np.random.normal()

print(h)
print('元素类型:', h.dtype, '数组形状:', h.shape, '元素个数:', h.size, '数组纬度:', h.ndim)


# 2.切片索引 切片
i = h[1][2][3]
print(i)
j = h[:, :2, 1:2]
print(j)


# 3. 改变形状 确保 size不变
k = h.reshape(1, -1)
print(k)

l = h.reshape(-1, 1)
print(l)

m = h.reshape(3, -1)
print(m)

# 4. 转换类型
n = h.astype(np.float)
print(n)


""" 运算 """

# 1. 条件运算
# a. 条件判断
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
print(stus_score > 80)

# b. 三目运算
print(np.where(stus_score < 80, 0, 90))


# 2. 统计运算
# a. 最值 np.max;np.min axis = 0/1 (列/行)
print(np.max(stus_score))
print(np.max(stus_score, axis=0))
print(np.max(stus_score, axis=1))
print(np.min(stus_score))

# b. 平均值 mean axis = 0/1
print(np.mean(stus_score))

# c. 方差 std
print(np.std(stus_score))

# 3. 数组运算
# a. 数组与数
print(stus_score + 5)
print(stus_score * 0.5)

# 4. 矩阵运算

# a. 相乘 np.dot()
w = [[0.4], [0.6]]
print(np.dot(stus_score, w))

# b. 拼接
v1 = [[0, 1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10, 11]]
v2 = [[12, 13, 14, 15, 16, 17],
      [18, 19, 20, 21, 22, 23]]
# 垂直拼接
result = np.vstack((v1, v2))
print(result)
# 水平拼接
result = np.hstack((v1, v2))
print(result)

