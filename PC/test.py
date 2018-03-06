import time
from multiprocessing import Pool, Manager


def task(args):
    count = args[0]
    queue = args[1]
    queue.put(count * count)


def main():
    test_list = [x * 3 for x in range(100000)]
    q = Manager().Queue()
    pool = Pool()
    pool.map(task, [(x, q) for x in test_list])
    time.sleep(1)
    while not q.empty():
        print(q.get())
    # print(result.get())


if __name__ == "__main__":
    main()
