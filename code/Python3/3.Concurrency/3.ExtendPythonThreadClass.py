from threading import Thread
import urllib.request
import urllib.error
from time import perf_counter


class HttpRequestThread(Thread):
    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url

    # 重写 run 方法中的逻辑，可以达到灵活扩展 Thread 功能的目的
    def run(self) -> None:
        print(f'Checking {self.url} ...')
        try:
            response = urllib.request.urlopen(self.url)
            print(response.code)
        except urllib.error.HTTPError as e:
            print(e.code)
        except urllib.error.URLError as e:
            print(e.reason)


def main() -> None:
    urls = [
        'https://baike.baidu.com/',
        'https://douban.com/',
    ]

    threads = [HttpRequestThread(url) for url in urls]

    [t.start() for t in threads]

    [t.join() for t in threads]


if __name__ == '__main__':
    start = perf_counter()
    main()
    end = perf_counter()
    print(f'Total time: {end - start} seconds')