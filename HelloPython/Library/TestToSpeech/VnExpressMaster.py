from Utils import VnExpress as vne

if __name__ == "__main__":
    # Lấy tất cả các link trong file link.txt
    linkList = vne.getLinks("input/link.txt")
    for index, link in enumerate(linkList):
        fullFilePath = "output/" +str(index+1)
        # Lấy nội dung của link tương ứng và lưu vào file txt
        vne.getContentFromUrl(link.strip(),fullFilePath)
        # Đọc file text và chuyển đổi ra âm thanh
        # vne.textToSpeech(fullFilePath)

    # vne.playSound("output/2.mp3",1.35)