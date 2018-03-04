pos_list = [x for x in range(10)]
phase = 69
pos_set = {1,2,3,4,5,6,7,8,9}


iterable = map(lambda e: (e, phase, pos_set), pos_list)

for i in iterable:
    print(i)