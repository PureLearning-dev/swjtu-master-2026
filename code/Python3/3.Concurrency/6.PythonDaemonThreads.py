from threading import Thread
import time


# 子线程执行的函数，通知休眠了多少时间
def show_timer():
    count = 0
    while True:
        count += 3
        time.sleep(3)
        print(f'Has been waiting for {count} second(s)...')

# 一旦开启子线程，根本无法阻止其运行，主线程也可以运行
# 程序会在所有线程都结束后才会结束，在子线程没结束之前，该进程都不会终止，只能通过杀死终端进行终止
# t = Thread(target=show_timer)
# t.start()
# answer = input('Do you want to exit?\n')


# 但是守护线程不会，进程结束，守护线程直接跟着结束，主从交换了
t = Thread(target=show_timer, daemon=True)
t.start()
answer = input('Do you want to exit?\n')

# 守护线程适合做在进程后台支持性、可中断、不要求独立完成收尾的任务
