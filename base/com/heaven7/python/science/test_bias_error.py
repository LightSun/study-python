# -*- coding: UTF-8 -*-
import numpy as np
from sklearn import metrics
y_true = np.array([1.0, 5.0, 4.0, 3.0, 2.0, 5.0, -3.0])
y_pred = np.array([1.0, 4.5, 3.5, 5.0, 8.0, 4.5, 1.0])
# 均方差
print(metrics.mean_squared_error(y_true, y_pred)) # 8.107142857142858