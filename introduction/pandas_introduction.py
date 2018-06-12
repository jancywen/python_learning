# -*- coding: utf-8 -*-
__author__ = 'wangwenjie'
__data__ = '2018/6/7 下午1:36'
__product__ = 'PyCharm'
__filename__ = 'pandas_introduction'


"""
    Pandas是基于Numpy开发出的,专门用于数据分析的开源Python库
"""

import numpy as np
import pandas as pd
import os

""" Series(一维数据) '键值对' 允许索引重复 """
s1 = pd.Series(np.arange(8))
print(s1)

s2 = pd.Series({"北京": 12, "上海": 13, "深圳": 14})
print(s2)

s3 = pd.Series([1, 2, 3], index=["上海", "上海", "深圳"])
print(s3)

print(s3["上海"])

print("\n*******************************\n")

"""  DataFrame(多特征数据,既有列索引,又有行索引)  """

data_3_4 = pd.DataFrame(np.arange(12).reshape(3, 4))

print(data_3_4)
print(data_3_4[:1])
print(data_3_4[:][0])

print('\n')
result = pd.read_csv(os.path.join("datas", "data_sta.csv"), encoding='gb2312')
print(result)

# 属性
print("属性:\n", "shape:", result.shape, "\nndim:", result.ndim,
      "\ncolumns:", result.columns, "\nindex:", result.index, "\nvalues:", result.values)

# 头
print(result.head())
# 尾
print(result.tail())
# info
print(result.info())
# describe
print(result.describe())


