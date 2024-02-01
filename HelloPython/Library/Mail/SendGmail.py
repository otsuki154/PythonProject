import smtplib
import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Thông tin tài khoản Gmail
sender_email = "huythanhapp@gmail.com"
sender_password = "twib waak utap yadr"  # tạo pass trong security> 2-step varification > app

# Đọc nội dung từ file maillist.txt để lấy receiver_emails
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'receiver_emails.txt')

with open(file_path, "r") as file:
    mailAcc= file.readlines()

# Loại bỏ ký tự xuống dòng từ mỗi dòng và tạo danh sách email
receiver_emails = [email.strip() for email in mailAcc]

# Tạo đối tượng MIMEMultipart
message = MIMEMultipart()
message["From"] = sender_email
#message["To"] = ", ".join(receiver_emails)  # Chuyển danh sách email thành một chuỗi ngăn cách bởi dấu phẩy
message["Bcc"] = ", ".join(receiver_emails)  # Thêm địa chỉ email vào Bcc field

# Định dạng thời gian theo yêu cầu
formatted_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
message["Subject"] = "【" + formatted_time + "】【Haru Aki】Cập nhật báo VnExpress.net"

# Nội dung email
# URL của trang web
url = "https://vnexpress.net/the-thao"

# Gửi yêu cầu GET đến trang web và lấy nội dung HTML
response = requests.get(url)
html_content = response.text

# Sử dụng BeautifulSoup để phân tích HTML
soup = BeautifulSoup(html_content, "html.parser")
# Bỏ nội dung trong thẻ span có class location-stamp
for span_tag in soup.find_all("span", class_="location-stamp"):
    span_tag.decompose()

# Lấy danh sách các bài báo
articles = soup.select("p.description a")

bodytext = "Những bài báo mới nhất trên VnExpress do 春秋 cập nhật\n\n\n\n"
# Sử dụng MIMEText để tạo phần nội dung của email
part = MIMEText(f"<p style='font-size:30px; font-weight:bold'>{bodytext}</p>", "html")

# Thêm phần nội dung vào đối tượng MIMEMultipart
message.attach(part)
for article in articles:
    if 'title' in article.attrs:
        # lấy nội dung title
        title = article['title']
    else:
        continue  # nếu không có attrs title thì bỏ qua luôn bài báo

    link = article["href"]  # lấy link bài báo
    content = article.get_text(strip=True)  # lấy nội dung tóm tắt

    # Sử dụng MIMEText để tạo phần nội dung của email
    part = MIMEText(f"<a style='font-size:20px;font-weight:bold;color:rgb(238, 3, 173)' href='{link}'>{title}</a>"
                    f"<p style='font-size:18px; font-style:italic;font-family:Courier New'>{content}</p>", "html")

    # Thêm phần nội dung vào đối tượng MIMEMultipart
    message.attach(part)

# Kết nối đến máy chủ SMTP của Gmail (sử dụng cổng 587)
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # enable security
    server.login(sender_email, sender_password)

    # Gửi email
    server.sendmail(sender_email, receiver_emails, message.as_string())

print("Email sent successfully!")
