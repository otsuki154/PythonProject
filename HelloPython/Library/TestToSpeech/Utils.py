from dataclasses import dataclass


from gtts import gTTS
import requests, os
from bs4 import BeautifulSoup

@dataclass
class VnExpress:
    def getLinks(fileLinks):
        """
        Đây là hàm lấy thông tin link từ file txt

        Args:
            fileLinks (str): link path
        Returns:
            list: Chứa thông tin link
        """
        with (open(fileLinks, "r") as file):
            linkList = file.readlines()
        return linkList

    def getContentFromUrl(url,filename):
        """
        Đây là hàm lấy thông tin từ link và lưu lại file txt

        Args:
            url (str): link bài báo
            filename (str): tên file txt được lưu
        """
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
        for paragraph in description_paragraphs + normal_paragraphs[:-1]:
            content += paragraph.get_text(strip=True) + "\n"

        # Lưu nội dung vào file text.txt
        with open(filename+".txt", "w", encoding="utf-8") as file:
            file.write(f"Tiêu đề:\n{title}\n\nNội dung bài báo:\n{content}")

    def textToSpeech(filename):
        """
        Đây là hàm lấy nôi dung text từ file txt và chuyển sang giọng đọc

        Args:
            filename (str): tên file txt
        """
        # Lấy nội dung văn bản
        text = ''
        with (open(filename+".txt", "r") as file):
            listContent = file.readlines()

        for content in listContent:
            text += content

        # Chọn giọng nam tiếng Việt
        voice = 'vi'  # Mã ngôn ngữ cho tiếng Việt

        # Tạo đối tượng gTTS với các tham số
        tts = gTTS(text=text, lang=voice, slow=False)

        # Đường dẫn đến file âm thanh
        file_path = filename+".mp3"
        # Lưu file âm thanh
        tts.save(file_path)

    def playSound(filePath,speed):
        """
        Đây là hàm play audio bằng afplay trong mac os
        Args:
            file_path (str): tfile path của audio
            speed_factor (float): tốc độ phát
        """
        os.system(f"afplay -q 1 -r {speed} {filePath}")

