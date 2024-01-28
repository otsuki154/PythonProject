import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Thông tin tài khoản Gmail
sender_email = "huythanhapp@gmail.com"
sender_password = "twib waak utap yadr" #tạo pass trong security> 2-step varification > app

# Người nhận email
receiver_email = "nvthanh15490@gmail.com"

# Tạo đối tượng MIMEMultipart
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Xin chào Thạnh! Tôi đến từ Python"

# Nội dung email
body = "Đây là mail được gửi để test gửi mail từ thư viện smtplib trong python"
message.attach(MIMEText(body, "plain"))

# Kết nối đến máy chủ SMTP của Gmail (sử dụng cổng 587)
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls() #enable security
    server.login(sender_email, sender_password)

    # Gửi email
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")
