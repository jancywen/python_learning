# -*- coding: utf-8 -*-


"""
**************************************

绘制散点

**************************************
"""


import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':


    # 产生测试数据
    x = np.arange(1, 10)
    y = x
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # 设置标题
    ax1.set_title('Scatter Plot')
    # 设置X轴标签
    plt.xlabel('X')
    # 设置Y轴标签
    plt.ylabel('Y')
    # 画散点图
    cValue = ['r', 'y', 'g', 'b', 'r', 'y', 'g', 'b', 'r']
    sValue = x * 10
    lValue = x
    ax1.scatter(x, y, c=cValue, s=sValue, linewidths=lValue, marker='o')
    # 设置图标
    plt.legend('x1')
    # 显示所画的图
    plt.show()
