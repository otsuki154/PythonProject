import psycopg2
from psycopg2 import sql
import re
from unidecode import unidecode
from datetime import datetime


import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Danh sách các đường link bài báo trên VnExpress
article_urls = [
    'https://vnexpress.net/noi-lo-the-he-trong-giac-mo-world-cup-4709161.html',
    'https://vnexpress.net/klinsmann-cam-thay-han-quoc-giong-argentina-o-world-cup-2022-4709369.html',
]

# Thư mục để lưu trữ hình ảnh
image_folder = "/Users/ThanhNV177/Project/PycharmProjects/DjangoWeb/static/home/images/artical"

# Tạo thư mục nếu chưa tồn tại
os.makedirs(image_folder, exist_ok=True)

def get_article_content(url):
    # Gửi yêu cầu HTTP để lấy nội dung trang web
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Lấy tiêu đề
        title_tag = soup.find('h1', class_='title-detail')
        title = title_tag.text.strip() if title_tag else "No Title"
        # Lấy mô tả
        description_tag = soup.find('p', class_='description')
        description = description_tag.text.strip() if description_tag else "No Description"

        # Lấy danh sách tất cả các thẻ <p> trong nội dung bài báo
        p_tags = soup.find_all('p', class_='Normal')

        # Cộng nội dung của từng thẻ <p> lại với nhau, mỗi thẻ có xuống hàng
        content = ""
        for p_tag in p_tags:
            if p_tag:
                content += "<p>" + p_tag.text.strip()+ "</p>"

        html_content = description + content
        # Lấy đường link hình ảnh
        image_url= None
        # Lấy nội dung bài báo
        article_content = soup.find('article', class_='fck_detail')
        if article_content:
            image_tag = article_content.find('img')
            if image_tag:
                image_url = image_tag['src'] if image_tag and 'src' in image_tag.attrs else None

        return title, html_content, image_url
    else:
        print(f"Failed to fetch content. Status code: {response.status_code}")
    return None


def download_image(image_url, article_title):
    if image_url:
        # Tạo đường dẫn đầy đủ cho hình ảnh
        full_image_path = os.path.join(image_folder, f"{article_title}.jpg")

        # Tải hình ảnh và lưu vào thư mục images
        image_data = requests.get(image_url).content
        with open(full_image_path, 'wb') as image_file:
            image_file.write(image_data)





def slugify(name):
    # Chuyển đổi chuỗi thành chữ thường và loại bỏ dấu
    name = unidecode(name.lower())

    # Loại bỏ các ký tự không phải chữ cái hoặc số và thay thế khoảng trắng bằng dấu gạch ngang
    slug = re.sub(r'[^\w\s-]', '', name)

    # Loại bỏ các dấu gạch ngang liên tiếp và dấu gạch ngang ở đầu và cuối chuỗi
    slug = '-'.join(filter(None, slug.split('-')))
    # Thay thế khoảng trắng bằng dấu gạch ngang
    slug = slug.replace(' ', '-')
    return slug


def get_current_time():
    # Lấy thời gian hiện tại
    current_time = datetime.now()

    # Định dạng thời gian theo yêu cầu
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_time




# Thông tin kết nối đến PostgreSQL
database_name = "djangodb"
user = "postgres"
password = "postgres"
host = "localhost"
port = "5433"

# Kết nối đến PostgreSQL
conn = psycopg2.connect(
    dbname=database_name,
    user=user,
    password=password,
    host=host,
    port=port
)

url = "https://vnexpress.net/thoi-su/chinh-tri"

# Gửi yêu cầu GET đến trang web và lấy nội dung HTML
response = requests.get(url)
html_content = response.text
# Sử dụng BeautifulSoup để phân tích HTML
soup = BeautifulSoup(html_content, "html.parser")
# Lấy danh sách các bài báo
articles = soup.select("p.description a")
article_links = []
for article in articles:
    if 'box_comment_vne' not in article["href"]:
        article_links.append(article["href"] )



# Tạo một đối tượng cursor để thực hiện các truy vấn SQL
cur = conn.cursor()

try:
    # # Xoá tất cả các bản ghi từ bảng
    # Xác định bảng và điều kiện xoá
    table_identifier = sql.Identifier("public", "home_artical")
    condition = sql.SQL("catagory_id = {}").format(sql.Literal(5))  # Thay đổi giá trị điều kiện nếu cần

    # Tạo câu lệnh DELETE
    delete_query = sql.SQL("DELETE FROM {} WHERE {}").format(table_identifier, condition)

    cur.execute(delete_query)


    # Chèn dữ liệu mới
    insert_query = sql.SQL("""
        INSERT INTO public.home_artical ("name", slug, special, publish_date, content, image, catagory_id, status, ordering)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """)
    # Lặp qua danh sách các đường link bài báo và lấy thông tin
    for article_url in article_links[1:]:
        title, content, image_url = get_article_content(article_url)
        if image_url is None or content == 'No Content':
            continue
        slug = slugify(title)
        special = True
        public_date = get_current_time()
        image = "home/images/artical/" + slug + ".jpg"
        catagoryid = 5
        status = "published"
        ordering = 1
        # Dữ liệu mẫu, bạn có thể thay đổi tùy theo nhu cầu
        sample_data = [
            (title, slug, special, public_date, content, image, catagoryid, status, ordering),
            # Thêm các bản ghi khác tùy theo nhu cầu
        ]
        cur.executemany(insert_query, sample_data)

        # Tải hình ảnh và lưu vào thư mục images
        download_image(image_url, slugify(title))
    # Commit lại để lưu thay đổi
    conn.commit()

finally:
    # Đóng kết nối
    cur.close()
    conn.close()
