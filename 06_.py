import os
import time
from multiprocessing import Pool
def test(n):
    print(f"{n}号进程开始运行,进程id为{os.getpid()}")
    time.sleep(0.3)
    print(f"{n}号进程运行结束")

def main():
    po = Pool(3)  # 创建一个进程池,容量为3
    for i in range(10):  # 创建了十个进程
        po.apply_async(test, (i, ))  # 将十个进程分别放进进程池当中运行

    po.close()
    po.join()
if __name__ == "__main__":
    main()
