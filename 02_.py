import threading
import time

def say():
    print("Hello World!!!")
    time.sleep(1)


def say_2():
    print("I love python")
    time.sleep(1)



if __name__ == "__main__":

    for i in range(5):
        t = threading.Thread(target=say)
        t1 = threading.Thread(target=say_2)
        t1.start()
        t.start()
    print("python is best language on the world!")
    while True:
        process_number = threading.enumerate()
        print("当前进程数:", len(process_number))#共创建了十个线程,包括主线程一共有十一个线程
        time.sleep(0.5)
        if len(process_number) == 1:
            break

