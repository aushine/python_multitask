import threading
import time


def say():
    for i in range(5):
        print("线程1------")
        time.sleep(1)

def say2():
    for i in range(5):
        print("线程2------")
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=say)
    t2 = threading.Thread(target=say2)
    t1.start()
    t2.start()