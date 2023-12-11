import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
import math

# tao figure
# fig = plt.figure()

# # create 1 or many subplot
# axis1 = fig.add_subplot(2, 2 , 1)
# axis2 = fig.add_subplot(2, 2 , 2)
# axis3 = fig.add_subplot(2, 2 , 3)

# axis1.plot(np.arange(0.0, 6.0, 0.2), 'b--')
# axis2.plot(rand(50).cumsum(), 'r--')
# axis3.plot(np.sin(np.arange(0, 3*np.pi, 0.1)))

# fig, axes = plt.subplots(2,3)
# axes[0,1].plot(rand(50).cumsum(), color='g', linestyle = 'dashed', marker='+')
# axes[1,1].hist(rand(100), bins = 20, color='k', alpha = 0.3)
# axes[0, 2].scatter(np.arange(30), np.arange(30) + 3*rand(30))

# fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
# for i in range(2):
#     for j in range(2):
#         axes[i, j].hist(rand(500), bins = 50, color = 'g', alpha = 0.5)
# plt.subplots_adjust(wspace=1, hspace=1)


# TICKS, LABELS, LEGENDS
x = np.arange(0,math.pi*2 , 0.05 )
y = np.sin(x)

axes = plt.axes()
plt.xlabel("Trục x")
plt.ylabel("Trục y")

plt.title("Biểu diễn đồ thị hình sin")

plt.plot(x, y, color='b', marker="*")

# setting ticker for trục x
axes.set_xticks([0, 2, 4, 6])

# setting ticker for trục y
axes.set_yticks([-1, 0, 1])

# set label for y ticker
axes.set_yticklabels(["sin(-90)", "sin(0)", "sin(90)"])

# luu anh
plt.savefig("hinh_sin.png", dpi=400, bbox_inches = 'tight')

plt.show()