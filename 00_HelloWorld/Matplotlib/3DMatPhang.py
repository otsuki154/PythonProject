import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Ve mat phang: 2x + 3y -4z -5 = 0
# Tạo phuong trinh duong thang
x = np.linspace(-5,5)
y = np.linspace(-5,5)

X, Y = np.meshgrid(x,y) #tao ra luoi cac diem
Z = (2*X + 3*Y -5)/4

# Vẽ đồ thị 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z)


# Thiết lập các nhãn trục
ax.set_xlabel('Trục X')
ax.set_ylabel('Trục Y')
ax.set_zlabel('Trục Z')

# Hiển thị đồ thị
plt.title('Vẽ mat phang trong không gian 3 chiều')
plt.legend()
plt.show()
