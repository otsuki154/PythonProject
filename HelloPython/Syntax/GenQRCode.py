import qrcode
from PIL import Image, ImageDraw, ImageFont

def create_wifi_qrcode(ssid, password):
    # Tạo đối tượng QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Tạo dữ liệu chứa thông tin WiFi
    wifi_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"

    # Thêm dữ liệu vào QRCode
    qr.add_data(wifi_data)
    qr.make(fit=True)

    # Tạo hình ảnh QRCode
    img = qr.make_image(fill_color="black", back_color="white")

    return img

# Thông tin WiFi
wifi_2g_ssid = "SPWH_L11_E741DA"
wifi_2g_password = "6BPS867A5S"

wifi_5g_ssid = "SPWH_L11_E741DA_5G"
wifi_5g_password = "6BPS867A5S"

# Tạo QR code cho mạng WiFi 2.4GHz
img_2g = create_wifi_qrcode(wifi_2g_ssid, wifi_2g_password)

# Tạo QR code cho mạng WiFi 5GHz
img_5g = create_wifi_qrcode(wifi_5g_ssid, wifi_5g_password)

# Kích thước của mỗi QR code
width, height = img_5g.size

# Tạo hình ảnh lớn để chứa cả hai QR code
img_combined = Image.new("RGB", (width * 2, height), "white")

# Paste QR code của mạng WiFi 2.4GHz và thêm tên
draw_2g = ImageDraw.Draw(img_combined)
draw_2g.text((10, 10), "WiFi 2.4GHz", fill="black")
img_combined.paste(img_2g, (0, 30))

# Paste QR code của mạng WiFi 5GHz và thêm tên
draw_5g = ImageDraw.Draw(img_combined)
draw_5g.text((width + 10, 10), "WiFi 5GHz", fill="black")
img_combined.paste(img_5g, (width, 30))

# Lưu hình ảnh chứa cả hai QR code
img_combined.save("ThanhWifiInfor.png")

