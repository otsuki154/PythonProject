import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Tạo tập hợp 10 điểm ngẫu nhiên trong không gian 3 chiều
np.random.seed(42)
points = np.random.rand(10, 3)  # Mỗi điểm có tọa độ ngẫu nhiên trong khoảng [0, 1)

# Vẽ đồ thị 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vẽ điểm trong không gian 3 chiều
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='o', label='Điểm')

# Thiết lập các nhãn trục
ax.set_xlabel('Trục X')
ax.set_ylabel('Trục Y')
ax.set_zlabel('Trục Z')

# Hiển thị đồ thị
plt.title('Vẽ các điểm trong không gian 3 chiều')
plt.legend()
#plt.show()
print(points)