# author: xiaohao
# time: 2018.01.30 23:28

from multiprocessing import Process,Queue
import time,random

# 写入进程
def write(q):
    for value in ['A','B','C']:
        print('put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读取进程
def read(q):
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':

    # 父进程创建Queue，并传给子线程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子线程pw，写入
    pw.start()
    # 启动子线程pr，读取
    pr.start()
    # 等待pw结束
    pw.join()
    # pr里进程是死循环，无法等待其结束，智能强行终止
    pr.terminate()

