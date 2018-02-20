import timeit


def test():
    count = 0
    for i in range(100):
        if i % 5 == 0:
            if i % 10 == 0:
                count += 1


def test_two():
    count = 0
    for i in range(100):
        if i % 5 == 0 and i % 10 == 0:
            count += 1


def test_three():
    for i in range(1000):
        if i % 6 == 0:
            continue

        if i % 10 == 0 and i % 5 == 0:
            continue


def test_four():
    for i in range(1000):
        if i % 6 == 0 or (i % 10 == 0 and i % 5 == 0):
            continue


for i in range(10):
    one = timeit.timeit(test_three)
    two = timeit.timeit(test_four)
    print('%0.3f    %0.3f        %0.3f' % (one, two, one - two))
