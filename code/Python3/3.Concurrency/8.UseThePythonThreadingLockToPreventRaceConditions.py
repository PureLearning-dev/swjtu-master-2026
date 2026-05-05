# 多线程同时执行可能会发生竞争状态，导致我们不期待的结果出现
from concurrent.futures import ThreadPoolExecutor
# 在这里需要引入 “共享变量” 这个概念，是这种状态的变量可以被多个线程进行读取和修改
# 如果只是读取，其实并没有什么影响，但是如果涉及到修改，就会出现问题
# 假设线程 A 正在读取变量 share，线程 B 正在修改变量 share，A 读取到的结果是否是被修改之前的内容呢？答案是否定的
# 但是我们的目的是读取修改之前的 share 中的内容，被 B 修改后读取的内容和我们预想的内容不同，此时就出现了问题！
# 在其他任何有修改的情况下都是可能发生类似的错误情况的，为了解决这样的问题，我们引入 Lock - 锁的概念

from threading import Thread, Lock
from time import sleep

# 多线程执行导致错误结果的示例代码，结果会跟随执行而变化
# counter = 0

# 每个线程都执行这个任务，最终 counter 的值和哪个线程最后执行绑定
# def increase(by):
#     global counter
#
#     local_counter = counter
#     local_counter += by
#
#     sleep(0.1)
#
#     counter = local_counter
#     print(f'counter={counter}')
#
# t1 = Thread(target=increase, args=(10,))
# t2 = Thread(target=increase, args=(20,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print(f'The final counter is {counter}')

# 和本科学习的 OS 这门课程中的 mutex 一致！mutex 是 mutual exclusion 的简写，在 OS 中用 mutex 修饰的变量是互斥访问的
# Lock 可以用日常的锁来理解，当你进入一个房间后会对其上锁，出去后解锁，供另一个人使用
# 当你进入房间并上锁后，其他人就无法进入房间了，此处的房间就是 “共享变量”

# counter = 0
#
# def increase(by, lock):
#     global counter
#     # 在访问 “共享变量” 前获取锁
#     lock.acquire()
#     local_counter = counter
#     local_counter += by
#     sleep(0.1)
#     counter = local_counter
#     # 在访问 “共享变量” 后释放锁
#     lock.release()
#
# lock = Lock()
#
# with ThreadPoolExecutor() as executor:
#     executor.map(lambda x: increase(x, lock), range(10))

# 上述的实现对于 lock 要进行获取和释放，我们可以对其进行优化，使用 with 语句自动释放资源则可
# counter = 0
#
# def increase(by, lock):
#     global counter
#
#     # 在 with lock 后自动获取 lock 资源，结束后自动释放 lock 资源
#     with lock:
#         local_counter = counter
#         local_counter += by
#
#         sleep(0.1)
#
#         counter = local_counter
#
#     print(f'counter={counter}')
#
#
# lock = Lock()
#
# t1 = Thread(target=increase, args=(10, lock))
# t2 = Thread(target=increase, args=(20, lock))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print(f'The final counter is {counter}')

# 当然，可以对其进一步抽象，抽象出一个类，在类中实现线程安全的方法
class Counter:
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, by):
        with self.lock:
            current_count = self.count
            current_count += by
            sleep(0.01)
            self.count = current_count
            print(f'counter={self.count}')

def main():
    counter = Counter()

    t1 = Thread(target=counter.increment, args=(10, ))
    t2 = Thread(target=counter.increment, args=(20, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f'The final counter is {counter.count}')

if __name__ == '__main__':
    main()
