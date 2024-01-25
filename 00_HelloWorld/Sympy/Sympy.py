from sympy import symbols, integrate

# Bước 2: Định nghĩa biểu thức của tích phân
x = symbols('x')
expression = x**2 + 2*x + 1

# Bước 3: Sử dụng hàm integrate để giải tích phân
result = integrate(expression, (x, 0, 10))

# In kết quả
print("Kết quả của tích phân là:", result)
