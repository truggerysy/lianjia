import numpy as np
from scipy import stats

# 第一组数据
data1 = [30, 37, 45, 49, 26, 48, 45, 44, 27, 49, 31, 48, 52]
# 第二组数据
data2 = [38, 43, 46, 32, 46, 50, 50, 47, 45, 33, 58, 50, 51, 28]

# 计算卡方检验
observed_values = np.array([data1.count(i) for i in set(data1)])
expected_values = np.array([data2.count(i) for i in set(data2)])
chi2, p = stats.chisquare(f_obs=observed_values, f_exp=expected_values)
print("卡方检验结果：")
print("卡方值：", chi2)
print("p值：", p)

# 计算t值
t, p = stats.ttest_ind(data1, data2)
print("t检验结果：")
print("t值：", t)
print("p值：", p)
