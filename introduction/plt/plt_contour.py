# -*- coding: utf-8 -*-

"""
**************************************

plt.contour()：只画线，不填充颜色

plt.contourf():只填充颜色，不画线

**************************************

"""



import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # 定义等高线高度函数
    def f(x, y):
        return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(- x ** 2 - y ** 2)

    # 数据数目
    n = 256
    # 定义x, y
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)

    # 生成网格数据
    X, Y = np.meshgrid(x, y)

    # 填充等高线的颜色, 8是等高线分为几部分
    plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)
    # 绘制等高线
    C = plt.contour(X, Y, f(X, Y), 8, colors='black')
    # 绘制等高线数据
    plt.clabel(C, inline=True, fontsize=10)

    # 去除坐标轴
    plt.xticks(())
    plt.yticks(())
    plt.show()