import multiprocessing
import time

q = multiprocessing.Queue()


def main():
    q.put(1)
    q.put(2)
    q.put(3)


if __name__ == "__main__":
    p = multiprocessing.Queue()
    main()
