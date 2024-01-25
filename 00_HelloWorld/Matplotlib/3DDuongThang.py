import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Tạo phuong trinh duong thang
t = np.linspace(0,10)
x = 2 + 3*t
y = -1 + 2*t
z = t

# Vẽ đồ thị 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z)


# Thiết lập các nhãn trục
ax.set_xlabel('Trục X')
ax.set_ylabel('Trục Y')
ax.set_zlabel('Trục Z')

# Hiển thị đồ thị
plt.title('Vẽ duong thang trong không gian 3 chiều')
plt.legend()
plt.show()
