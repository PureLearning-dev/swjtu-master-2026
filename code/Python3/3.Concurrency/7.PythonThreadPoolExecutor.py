# 前面的 py 文件中的多线程，每个线程都是我们自己创建的，对于少数线程都还好，如果可能用到大量的线程，还是采用之前那种方式，会消耗许多的计算机 CPU 资源
# 为了解决这个问题，引入 ThreadPoolExcutor 类（线程池解决方案），通过维护一组线程，在需要时直接获取，用完归还，这样可以大大降低 CPU 开销
# ThreadPoolExcutor 继承 Excutor 类，执行 submit 方法后会返回一个 Future 对象实例

# 学过 JS 就可以将 Excutor 和 Future 类比为 Promise 进行理解

from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor

def task(id: int):
    print(f'Starting the task {id}...')
    sleep(1)
    return f'Done with task {id}'

start = perf_counter()

# ThreadPoolExecutor 类的 submit 方法返回一个 Future 对象实例
# Excutor 类中总共存在 3 个方法：submit、map、shutdown
# submit 将需要执行的任务提交到任务队列中，等待系统调用线程池中的线程进行执行，并返回一个 Future 实例
# Future 类中存在两个核心方法：result、exception
# result 是未来线程执行完这个任务后得到的结果
# 查看源码可以知道，如果不给出线程池中线程的数量，会根据 32 和 本地 CPU 的数量 + 4 做比较，取较大值

# with ThreadPoolExecutor() as executor:
#     f1 = executor.submit(task, 1)
#     f2 = executor.submit(task, 2)
#
#     # 这里也会阻止主线程往下推进
#     # 这个非常容易理解，如果不阻止，则主线程直接执行完成了，导致子线程也结束，从而造成意料之外的情况发生
#     print(f1.result())
#     print(f2.result())
#
# finish = perf_counter()
#
# print(f"It took {finish-start} second(s) to finish.")

# 上述代码也可以使用 map 进行优化

# whith 也保证在子线程结束后关闭
# with ThreadPoolExecutor() as executor:
#     # 右侧的可迭代对象按顺序传递参数到左侧的任务函数中
#     # 返回一个包含执行结果的迭代器
#     # map 将所有子线程任务提交给线程池
#     results = executor.map(task, range(1, 11))
#
# for result in results:
#     print(result)
#
# end = perf_counter()
#
# print(f"Total time: {end - start} seconds")



