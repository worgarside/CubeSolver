MOVES = ['U', 'D', 'L', 'R', 'F', 'B']
it = iter(MOVES)
for move in it:
    print('%s -:- %s'% (move, next(it)))
