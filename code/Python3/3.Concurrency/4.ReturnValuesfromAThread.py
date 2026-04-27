from threading import Thread
import urllib.request
import urllib.error


class HttpRequestThread(Thread):

    # 将子线程中要返回主线程的值存储到线程实例中
    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url
        self.http_status_code = None
        self.reason = None

    def run(self) -> None:
        try:
            response = urllib.request.urlopen(self.url)
            self.http_status_code = response.code
        except urllib.error.HTTPError as e:
            self.http_status_code = e.code
        except urllib.error.URLError as e:
            self.reason = e.reason


def main() -> None:
    urls = [
        'https://baike.baidu.com/',
        'https://douban.com/',
    ]

    threads = [HttpRequestThread(url) for url in urls]

    # 在子线程不输出，而是换到主线程进行输出，说明主线程可以得到子线程中执行得到的数据
    [t.start() for t in threads]

    [t.join() for t in threads]

    [print(f'{t.url}: {t.http_status_code}') for t in threads]


if __name__ == '__main__':
    main()

