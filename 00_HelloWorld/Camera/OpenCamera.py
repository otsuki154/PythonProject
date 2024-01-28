
import cv2 #đang lỗi vì không có version tương thích với mac os hiện tại

# Mở kết nối với camera (đối số 0 thường là camera mặc định trên máy tính)
cap = cv2.VideoCapture(0)

# Kiểm tra xem camera có được mở thành công hay không
if not cap.isOpened():
    print("Không thể mở camera.")
    exit()

while True:
    # Đọc frame từ camera
    ret, frame = cap.read()

    # Kiểm tra xem frame có được đọc thành công hay không
    if not ret:
        print("Không thể đọc frame.")
        break

    # Hiển thị frame trong một cửa sổ
    cv2.imshow('Camera', frame)

    # Để thoát khỏi vòng lặp, nhấn 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên khi kết thúc
cap.release()
cv2.destroyAllWindows()
