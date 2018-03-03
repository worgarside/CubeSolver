from multiprocessing import Pool
import time

def time_function(func, *args):
    start = int(round(time.time() * 1000))
    result = func(*args)
    end = int(round(time.time() * 1000))
    total = (end - start) / 1000
    print('Time: %0.03fs' % total)
    return result


def map_func(n):
    return n*2


def test_func():
    p = Pool(processes=4)
    list_two = p.map(map_func, range(10000000))

def test_func_two():
    list_three = []
    for i in range(10000000):
        list_three.append(i*2)

if __name__ == '__main__':

    time_function(test_func)
    time_function(test_func_two)
