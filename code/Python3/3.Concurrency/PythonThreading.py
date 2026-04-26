from time import sleep, perf_counter
from threading import Thread


# def task():
#     print("task start")
#     sleep(1)
#     print("task end")

# # 实现同步代码，并输出执行时间
# start = perf_counter()
#
# task()
# task()
#
# end = perf_counter()

# print("excute twice task function take times is", end - start, "seconds")

# 改造为多线程
# start = perf_counter()

# 创建两个线程，两个线程分别执行的任务都是 task 函数
# task1 = Thread(target=task)
# task2 = Thread(target=task)
#
# task1.start()
# task2.start()

# join 让主线程等待这两个线程执行完成后才开始执行
# 若不使用 join，会导致后续代码直接执行，从而导致我们无法统计执行时间
# task1.join()
# task2.join()
#
# end = perf_counter()
#
# print(f"It took {end - start} second(s) to complete.")

def task(thread_id):
    print(f"Starting->{thread_id}")
    sleep(1)
    print(f"Exiting->{thread_id}")

threads = []

start = perf_counter()

# 创建 10 个线程放入并调用 start 方法
for i in range(10):
    threads.append(Thread(target=task, args=(i,)))
    threads[i].start()

# 每个线程都可以进行调度，主线程也可以执行，但是调度主要是靠 OS，所以每次执行的顺序大概率是不同的
# 直到执行到 join 方法，会让主线程等待调用 join 的子线程执行完后才继续执行
for i, t in enumerate(threads):
    t.join()
    print(f"{t}-{i}执行完成")

end = perf_counter()

print(f"Total time: {end - start}")