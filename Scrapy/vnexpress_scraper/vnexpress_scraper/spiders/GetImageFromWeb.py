import requests
import os

# Hàm để download và lưu ảnh
def download_and_save_image(url, folder_path, image_name):
    response = requests.get(url)
    if response.status_code == 200:
        # Kiểm tra và tạo thư mục nếu chưa tồn tại
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Tạo đường dẫn đầy đủ cho ảnh
        image_path = os.path.join(folder_path, image_name)

        # Lưu ảnh vào thư mục
        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f"Đã lưu ảnh: {image_path}")
    else:
        print(f"Không thể download ảnh từ {url}")

# URL của API trả về JSON
api_url = "https://unsplash.com/napi/topics/nature/photos"
params = {"page": 5, "per_page": 50}

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Host": "unsplash.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.3 Safari/605.1.15",
    "Accept-Language": "en-US",
    "Referer": "https://unsplash.com/t/nature",
    "Connection": "keep-alive",
}

response = requests.get(api_url, params=params, headers=headers)

if response.status_code == 200:
    json_data = response.json()

    # Thư mục để lưu ảnh
    image_folder = "imageDL"

    for photo in json_data:
        # Lấy thông tin về ảnh từ JSON
        image_url = photo["urls"]["small"]
        image_name = f"{photo['id']}.jpg"

        # Download và lưu ảnh
        download_and_save_image(image_url, image_folder, image_name)
else:
    print(f"Không thể lấy dữ liệu JSON từ {api_url}")
