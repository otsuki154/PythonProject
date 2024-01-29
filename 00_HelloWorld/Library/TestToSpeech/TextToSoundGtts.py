# Đọc báo vnexpresss theo link đưa vào từ file link.txt
# Lấy thông tin về bài báo lưu vào file txt rồi đọc từ file txt để chuyển qua speech
from gtts import gTTS
import os
import requests
from bs4 import BeautifulSoup

# Lấy nội dung văn bản
url = ''
with (open("link.txt", "r") as file):
    linkList = file.readlines()

for link in linkList:
    url += link

# Gửi yêu cầu GET đến trang web và lấy nội dung HTML
response = requests.get(url)
html_content = response.text

# Sử dụng BeautifulSoup để phân tích HTML
soup = BeautifulSoup(html_content, "html.parser")
# Bỏ nội dung trong thẻ span có class location-stamp
for span_tag in soup.find_all("span", class_="location-stamp"):
    span_tag.decompose()
# Lấy title
title = soup.find("title").get_text(strip=True)

# Lấy nội dung trong thẻ p có class description và thẻ p có class Normal
description_paragraphs = soup.select("p.description")
normal_paragraphs = soup.select("p.Normal")

# Ghép nội dung từ các đoạn văn bản vào một biến
content = ""
for paragraph in description_paragraphs + normal_paragraphs:
    content += paragraph.get_text(strip=True) + "\n"

# Lưu nội dung vào file text.txt
with open("text.txt", "w", encoding="utf-8") as file:
    file.write(f"Tiêu đề: {title}\n\nNội dung bài báo:\n{content}")

# Lấy nội dung văn bản
text = ''
with (open("text.txt", "r") as file):
    listContent = file.readlines()

for content in listContent:
    text += content

# Chọn giọng nam tiếng Việt
voice = 'vi'  # Mã ngôn ngữ cho tiếng Việt

# Tạo đối tượng gTTS với các tham số
tts = gTTS(text=text, lang=voice, slow=False)

# Đường dẫn đến file âm thanh
file_path = "output_Gtts.mp3"
# Lưu file âm thanh
tts.save(file_path)

# Mở file âm thanh bằng trình nghe nhạc mặc định trên hệ điều hành
# Tốc độ phát nhạc, ví dụ: tăng tốc độ lên gấp đôi
speed_factor = 1.5

# Sử dụng lệnh afplay để phát nhạc với tốc độ tùy chỉnh
os.system(f"afplay -q 1 -r {speed_factor} {file_path}")

print("Đã tạo và phát file âm thanh 'output_Gtts.mp3'")
