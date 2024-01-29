import requests
import time
import sys
import locale

currency = 'USD'

def format_currency(number):
    # Đặt locale theo định dạng tiền tệ
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    # Định dạng số thành chuỗi tiền tệ
    formatted_number = locale.currency(number, grouping=True)

    return formatted_number

def get_coin_prices(api_key, symbols):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
        'start': '1',
        'limit': '10',
        'convert': currency
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    try:
        while True:
            response = requests.get(url, headers=headers, params=parameters)
            data = response.json()

            if response.status_code == 200:
                # Di chuyển con trỏ về đầu dòng
                sys.stdout.write("\r")
                sys.stdout.flush()

                for coin in data['data']:
                    symbol = coin['symbol']
                    if symbol in symbols:
                        price = coin['quote'][currency]['price']
                        # In giá của coin mà không tạo dòng mới
                        sys.stdout.write(f'Giá của {symbol}: {format_currency(price)} ' + currency + '   ')
                        sys.stdout.flush()

            else:
                print(f'Lỗi: {data["status"]["error_message"]}')

            time.sleep(3)  # Đợi 3 giây trước khi gửi yêu cầu tiếp theo

    except KeyboardInterrupt:
        print("\nDừng cập nhật giá.")
        sys.exit()


def get_market_info(api_key):
    url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest"

    parameters = {
        'CMC_PRO_API_KEY': api_key
    }

    response = requests.get(url, params=parameters)
    data = response.json()

    if 'status' in data and data['status']['error_code'] == 0:
        market_info = data['data']
        return market_info
    else:
        print("Error:", data['status']['error_message'])
        return None


def print_market_info(market_info):
    if market_info:
        print("Thông Tin Thị Trường Cryptocurrency:")
        print("-------------------------------")
        vonhoa = market_info['quote'][currency]['total_market_cap']
        print(f"Tổng Vốn Hóa Thị Trường: {format_currency(vonhoa)} " + currency)
        thaydoi = market_info['quote'][currency]['total_market_cap_yesterday']
        print(f"Thay Đổi 24 Giờ: {format_currency(thaydoi)} " + currency)
        rate = market_info['quote'][currency]['total_market_cap_yesterday_percentage_change']
        print(f"Tỷ Lệ Biến Động 24 Giờ: {format_currency(rate)}%")
    else:
        print("Không có thông tin thị trường.")


def get_ethereum_info(api_key):
    # Đặt symbol là 'ETH' cho Ethereum
    symbol = 'ETH'

    # Tạo URL để gửi yêu cầu API đến CoinMarketCap
    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?symbol={symbol}&CMC_PRO_API_KEY={api_key}'

    # Gửi yêu cầu GET và lấy dữ liệu JSON
    response = requests.get(url)
    data = response.json()

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Lấy thông tin chi tiết của Ethereum
        ethereum_info = data['data'][0]

        # In thông tin chi tiết
        print("Thông tin chi tiết của Ethereum (ETH):")
        print(f"Tên: {ethereum_info['name']}")
        print(f"Symbol: {ethereum_info['symbol']}")
        print(f"Giá hiện tại (USD): {ethereum_info['quote']['USD']['price']}")
        print(f"Vốn hóa thị trường (USD): {ethereum_info['quote']['USD']['market_cap']}")
        print(f"Khối lượng giao dịch 24 giờ: {ethereum_info['quote']['USD']['volume_24h']}")
    else:
        print("Yêu cầu không thành công. Kiểm tra lại API key hoặc thử lại sau.")


if __name__ == "__main__":
    # Đặt API key của bạn ở đây
    api_key = '710c3d08-ac91-4d6e-8a30-6d57c1fec8cd'

    # Lấy thông tin thị trường
    market_info = get_market_info(api_key)
    # Hiển thị thông tin thị trường
    print_market_info(market_info)
    get_ethereum_info(api_key)
    # Danh sách các loại coin bạn quan tâm (ví dụ: Bitcoin, Ethereum, Ripple)
    crypto_symbols = ['BTC', 'ETH', 'XRP']
    get_coin_prices(api_key, crypto_symbols)
