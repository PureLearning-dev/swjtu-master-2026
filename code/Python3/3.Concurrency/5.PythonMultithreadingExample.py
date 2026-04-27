import threading
import requests
from lxml import html
import re


class Stock(threading.Thread):
    def __init__(self, symbol: str) -> None:
        super().__init__()
        self.symbol = symbol
        self.url = f'https://finance.yahoo.com/quote/{symbol}'
        self.price = None
        self.error = None

    def run(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        }

        try:
            response = requests.get(self.url, headers=headers, timeout=10)
            if response.status_code == 200:
                tree = html.fromstring(response.text)

                # 多种方式尝试获取价格
                price_text = None

                # 方法1：通过 fin-streamer 的 data-field 属性
                price_text = tree.xpath('//fin-streamer[@data-field="regularMarketPrice"]/text()')

                # 方法2：通过 fin-streamer 的 data-symbol 属性
                if not price_text or not price_text[0].strip():
                    price_text = tree.xpath(f'//fin-streamer[@data-symbol="{self.symbol}"]/text()')

                # 方法3：通过 id 属性
                if not price_text or not price_text[0].strip():
                    price_text = tree.xpath('//*[@id="quote-header-info"]//fin-streamer[1]/text()')

                # 方法4：使用正则从页面 JavaScript 中提取
                if not price_text or not price_text[0].strip():
                    match = re.search(r'"regularMarketPrice":\s*\{\s*"raw":\s*([\d.]+)', response.text)
                    if match:
                        self.price = float(match.group(1))
                        return

                if price_text and price_text[0].strip():
                    price_str = price_text[0].strip().replace(',', '')
                    self.price = float(price_str)
                else:
                    self.error = "未找到价格信息"
            else:
                self.error = f"HTTP {response.status_code}"

        except requests.exceptions.RequestException as e:
            self.error = f"请求失败: {e}"
        except Exception as e:
            self.error = f"解析失败: {e}"

    def __str__(self):
        if self.price:
            return f'{self.symbol}\t${self.price:.2f}'
        return f'{self.symbol}\t{self.error if self.error else "获取失败"}'


def main():
    """主函数：获取多个股票价格"""
    symbols = ['MSFT', 'GOOGL', 'AAPL', 'META', 'AMZN', 'TSLA']
    threads = []

    print("正在获取股票价格...\n")

    # 创建并启动所有线程
    for symbol in symbols:
        t = Stock(symbol)
        threads.append(t)
        t.start()

    # 等待所有线程完成并打印结果
    for t in threads:
        t.join()
        print(t)


if __name__ == '__main__':
    main()