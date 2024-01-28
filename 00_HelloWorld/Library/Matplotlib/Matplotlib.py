import numpy as np
import matplotlib.pyplot as plt

# Tạo dãy giá trị x từ -2*pi đến 2*pi
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Tính giá trị y cho hàm sin(x) + cos(x)
y = np.sin(x) + np.cos(x)

# Vẽ đồ thị
plt.plot(x, y, label=r'$\sin(x) + \cos(x)$')
plt.title('Đồ thị hàm sin(x) + cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
