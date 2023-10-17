X = 'x'
O = 'o'

map = [
    [X, O, X],
    [X, O, O],
    [X, X, X],
]

def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print('|', map[i][j], end=' ')
        print('|')


print_map(map)