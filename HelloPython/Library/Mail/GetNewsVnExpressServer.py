import psycopg2
import re
import os
import requests
from bs4 import BeautifulSoup
from psycopg2 import sql
from unidecode import unidecode
from datetime import datetime

def convert_to_formatted_time(date_str):
    # Tách chuỗi theo dấu phẩy
    date_parts = date_str.split(", ")
    try:
        # Ghép lại các phần tử cần thiết
        formatted_date_str = f"{date_parts[1]} {date_parts[2].replace(' (GMT+7)', '')}"
        # Chuyển đổi thành đối tượng datetime
        date_obj = datetime.strptime(formatted_date_str, "%d/%m/%Y %H:%M")

        # Định dạng lại ngày thành chuỗi theo định dạng mong muốn
        formatted_time = date_obj.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time
    except Exception as e:
        return ""

def get_article_content(url):
    # Gửi yêu cầu HTTP để lấy nội dung trang web
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Bỏ nội dung trong thẻ span có class location-stamp
        for span_tag in soup.find_all("span", class_="location-stamp"):
            span_tag.decompose()
        # Lấy tiêu đề
        title_tag = soup.find('h1', class_='title-detail')
        title = title_tag.text.strip() if title_tag else "No Title"
        # Lấy date
        date_tag = soup.find('span', class_='date')
        date = date_tag.text.strip() if title_tag else "No Date"
        published_date = convert_to_formatted_time(date)
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

        html_content = "<p>"+ description+ "</p>" + content

        # Lấy đường link hình ảnh
        image_url = None
        # Lấy nội dung bài báo
        article_content = soup.find('article', class_='fck_detail')
        if article_content:
            image_tag = article_content.find('img')
            if image_tag:
                image_url = image_tag['src'] if image_tag and 'src' in image_tag.attrs else None

        return title, html_content, image_url,published_date
    else:
        print(f"Failed to fetch content. Status code: {response.status_code}")
    return None

def download_image(image_folder,image_url, article_title):
    # Tạo thư mục nếu chưa tồn tại
    os.makedirs(image_folder, exist_ok=True)
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

def getArtcalDataInfors(url,image_folder,catagoryId):
    # Lấy danh sách các bài báo
    article_links = []
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    articles = soup.select("p.description a")
    for article in articles:
        if 'box_comment_vne' not in article["href"]:
            article_links.append(article["href"] )

    # Tạo insert data
    insertData = []

    i = 1
    for article_url in article_links[1:]:
        try:
            title, content, image_url, public_date = get_article_content(article_url)
            if image_url is None or content == 'No Content':
                print(f'title:{title} imageUrl:{image_url} link:{article_url}')
                continue
            slug = slugify(title)
            if i == 1:
                special = True
            else:
                special = False
            # public_date = get_current_time()
            image = "home/images/artical/" + slug + ".jpg"
            status = "published"
            ordering = i
            i += 1
            # Dữ liệu mẫu, bạn có thể thay đổi tùy theo nhu cầu
            articleInfor = (title, slug, special, public_date, content, image, catagoryId, status, ordering)
            insertData.append(articleInfor)

            # Tải hình ảnh và lưu vào thư mục images
            download_image(image_folder, image_url, slug)
        except Exception as e:
            print(f'title:{title} imageUrl:{image_url} link:{article_url}')
            continue
    return insertData

def UpdateAritcleDataInfors(insertData,catagoryid):

    # Kết nối đến PostgreSQL
    conn = psycopg2.connect(
        dbname="djangodb",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

    # Tạo một đối tượng cursor để thực hiện các truy vấn SQL
    cur = conn.cursor()

    try:
        # Xoá tất cả các bản ghi từ bảng
        table_identifier = sql.Identifier("public", "home_artical")
        condition = sql.SQL("catagory_id = {}").format(sql.Literal(catagoryid))  # Thay đổi giá trị điều kiện nếu cần

        # DELETE dữ liệu cũ
        delete_query = sql.SQL("DELETE FROM {} WHERE {}").format(table_identifier, condition)
        cur.execute(delete_query)

        # Create SQL query
        insert_query = sql.SQL("""
            INSERT INTO public.home_artical ("name", slug, special, publish_date, content, image, catagory_id, status, ordering)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """)

        # Insert Article Datas
        cur.executemany(insert_query, insertData)
        conn.commit()

    finally:
        # Đóng kết nối
        cur.close()
        conn.close()


if __name__ == "__main__":

    urls = [
        "https://vnexpress.net/the-thao",
        "https://vnexpress.net/kinh-doanh",
        "https://vnexpress.net/thoi-su/chinh-tri",
        "https://vnexpress.net/khoa-hoc",
        "https://vnexpress.net/the-gioi",
        "https://vnexpress.net/giao-duc",
    ]
    categoryIds = [
        3,
        4,
        5,
        6,
        7,
        8,
    ]

    # Thư mục để lưu trữ hình ảnh
    image_folder = "/home/thanh/code-server/config/PythonProject/DjangoWeb/static/home/images/artical"
    combined_dict = dict(zip(categoryIds, urls))
    for categoryId, url in combined_dict.items():

        insertData = getArtcalDataInfors(url,image_folder,categoryId)
        UpdateAritcleDataInfors(insertData,categoryId)