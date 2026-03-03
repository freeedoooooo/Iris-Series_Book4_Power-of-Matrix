import matplotlib.pyplot as plt  # 导入Matplotlib库，用于绘图
import numpy as np  # 导入NumPy库，用于数值计算

x1 = np.linspace(-10, 10, num=201)  # 定义x1的范围，从-10到10，共201个点
x2 = x1  # 定义x2的范围与x1相同

xx1, xx2 = np.meshgrid(x1, x2)  # 生成网格，用于二维坐标

p = 2  # 设置Lp范数中的p值，此处为2
zz = ((np.abs((xx1)) ** p) + (np.abs((xx2)) ** p)) ** (1. / p)  # 计算Lp范数的值

fig, ax = plt.subplots(figsize=(8, 8))  # 创建画布和坐标轴，设置大小为12x12

## 绘制等高线
ax.contour(xx1, xx2, zz, levels=np.arange(11), cmap='RdYlBu_r')  # 绘制等高线，颜色映射为RdYlBu_r

## 绘制坐标轴和边框设置
ax.axhline(y=0, color='k', linewidth=0.25)  # 绘制y轴
ax.axvline(x=0, color='k', linewidth=0.25)  # 绘制x轴
ax.set_xlim(-12, 12)  # 设置x轴范围为-12到12
ax.set_ylim(-12, 12)  # 设置y轴范围为-12到12
ax.spines['top'].set_visible(False)  # 隐藏顶部边框
ax.spines['right'].set_visible(False)  # 隐藏右侧边框
ax.spines['bottom'].set_visible(False)  # 隐藏底部边框
ax.spines['left'].set_visible(False)  # 隐藏左侧边框
ax.set_xlabel('$x_1$')  # 设置x轴标签
ax.set_ylabel('$x_2$')  # 设置y轴标签
ax.set_aspect('equal', adjustable='box')  # 设置坐标轴比例为相等
plt.show()  # 显示绘图
