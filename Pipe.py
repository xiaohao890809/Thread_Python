# author: xiaohao
# time: 2018.01.31 20:15

from multiprocessing import Pipe,Process
import time,random,os

# 发送任务
def proc_send(pipe, urls):
    for url in urls:
        print('Process %s send %s' %(os.getpid(),url))
        pipe.send(url)
        time.sleep(random.random())

# 读取进程
def proc_recv(pipe):
    while True:
        print('Process %s get %s.' %(os.getpid(), pipe.recv()))
        time.sleep(random.random())

if __name__ == '__main__':

    pipe = Pipe()
    p1 = Process(target=proc_send, args=(pipe[0],['url_'+str(i) for i in range(10)]))
    p2 = Process(target=proc_recv, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


