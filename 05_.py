import multiprocessing

def download_from_web(q):
    data = list(range(1, 10001))
    for i in data:
        q.put(i)


def data_dispose(q, ):
    data_diposed = list()
    while True:
        # 只有队满才会开始处理数据
        if q.full():
            while True:
                data_diposed.append(q.get())
                if q.empty():
                    data_diposed = list(map(str, data_diposed))
                    print("处理过后的数据:", data_diposed)
                    return


def main():

    # 1. 创建一个队列,最大长度为1W
    q = multiprocessing.Queue(10000)
    # 2. 创建多个进程，将队列的引用当作实参进行传递到当中
    p1 = multiprocessing.Process(target=download_from_web, args=(q, ))
    p2 = multiprocessing.Process(target=data_dispose, args=(q, ))

    p1.start()
    p2.start()

if __name__ == "__main__":
    main()
