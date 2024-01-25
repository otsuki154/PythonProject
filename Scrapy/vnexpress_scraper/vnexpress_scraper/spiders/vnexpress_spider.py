# tạo project bằng lệnh scrapy startproject vnexpress_scraper
# dùng pychame mở project trong thư mục vnexpress_scraper (có chưa folder spiders)

# cd đến /Users/ThanhNV177/PycharmProjects/Scrapy/vnexpress_scraper
# chạy lệnh scrapy crawl vnexpress_spider để craw data web

import scrapy
import requests
import json


class VnExpressSpider(scrapy.Spider):
    name = 'vnexpress_spider'
    allowed_domains = ['https://directory.shoutcast.com/']
    start_urls = ['https://directory.shoutcast.com/']

    def parse(self, response):

        header = {'POST': '/Home/BrowseByGenre HTTP/1.1',
                  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  'Accept': '*/*',
                  'Accept-Language': 'en-us',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Host': 'directory.shoutcast.com',
                  'Origin': 'https://directory.shoutcast.com',
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.3 Safari/605.1.15',
                  'Connection': 'keep-alive',
                  'Referer': 'https://directory.shoutcast.com/',
                  'Content-Length': '24',
                  'Cookie': '_hjSession_503568=eyJpZCI6IjUxYTVkZjAxLTg5ZGEtNGJmOS1hODZkLTE3MmNlMDY1ZjY2NiIsImMiOjE3MDYwOTE4Mjg2ODUsInMiOjAsInIiOjAsInNiIjoxLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _ga_G6NE0JEBWC=GS1.2.1706091829.1.0.1706091829.0.0.0; _fbp=fb.1.1706091828653.1249779168; _ga=GA1.2.1829996514.1706091829; _gat=1; _gid=GA1.2.1593312107.1706091829; _hjSessionUser_503568=eyJpZCI6ImEwZWM0NWZkLTdmMTAtNWY4Yy1iZTY1LWNiNmJkNmY0MTBmZCIsImNyZWF0ZWQiOjE3MDYwOTE4Mjg2ODMsImV4aXN0aW5nIjpmYWxzZX0=; ASP.NET_SessionId=3ltxqhsne52icx4cimart3uq',
                  'X-Requested-With': 'XMLHttpRequest',
                  }
        # Chu y, hay lay lai noi dung cookie(co the la ca header) bang cach tao request tuong ung tren trinh duyet Safari

        fdata = {'genrename': 'Blues'}

        rq = requests.post('https://directory.shoutcast.com/Home/BrowseByGenre', headers=header, data=fdata)
        jsonContent = json.loads(rq.content)

        # Lấy thông tin của thẻ <span><a> , điều quan trọng là phải xác định cấu trúc xpath tương ứng với dữ liệu cần lấy
        span_a_content = response.xpath('//ul/li/span/a/text()').getall()

        # Ghi nội dung vào tệp txt
        with open('aaa.txt', 'w', encoding='utf-8') as file:
            file.write('Menu:\n')
            for parent in span_a_content:
                file.write(f"*{parent.strip()}\n")

            file.write('Station trong ALTERNATIVE / ADULT ALTERNATIVE:\n')
            for i in range(len(jsonContent)):
                print('Name: ' + jsonContent[i]['Name'] + '\n')
                file.write('Name: ' + jsonContent[i]['Name'] + '\n')

#Bài tập: craw 