import matplotlib.pyplot as plt
import numpy as np
import numpy.random as randn
import math

# Tạo khung hình figure
fig = plt.figure()

# Thêm subplot vào figure
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 3)
ax3 = fig.add_subplot(2, 2, 4)

ax1.plot(np.arange(0.0, 5.0, 0.2), 'k--')
ax2.plot(np.random.randn(50).cumsum(), 'ro') 
ax3.plot(np.sin(np.arange(0, 3*np.pi, 0.1)))
plt.show()


fig, axes=plt.sub