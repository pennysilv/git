X = 'x'
O = 'o'
Empty = ' '

current_player = X

map = [
    [Empty, Empty, Empty],
    [Empty, Empty, Empty],
    [Empty, Empty, Empty],
]

def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print('|', map[i][j], end=' ')
        print('|')

def get_player_turn():
    global current_player

    if current_player == X:
        nums = input('Ходят крестики: ').split()
    else:
        nums = input('Ходят нолики: ').split()
    return int(nums[0]), int(nums[1])

def switch_player():
    global current_player

    if current_player == X:
        current_player = O
    else:
        current_player = X

def change_map(map, row, column):
    global current_player
    map[row - 1][column - 1] = current_player

def is_filled(map, row, column):
    return map[row - 1][column - 1] != Empty

def is_winner(map, player):
    if map[0][0] == map[0][1] == map[0][2] == player:
        return True
    elif map[1][0] == map[1][1] == map[1][2] == player:
        return True
    elif map[2][0] == map[2][1] == map[2][2] == player:
        return True
    elif map[0][0] == map[1][0] == map[2][0] == player:
        return True
    elif map[0][1] == map[1][1] == map[2][1] == player:
        return True
    elif map[0][2] == map[1][2] == map[2][2] == player:
        return True
    elif map[2][0] == map[1][1] == map[0][2] == player:
        return True
    elif map[0][0] == map[1][1] == map[2][2] == player:
        return True

def is_full(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == Empty:
                return False
    return True

def is_tie(map):
    return not is_winner(map, X) and not is_winner(map, O) and is_full(map)

while True:
    print_map(map)
    row, column = get_player_turn()
    while is_filled(map, row, column):
        print('Клетка уже заполнена')
        row, column = get_player_turn()

    change_map(map, row, column)
    if is_winner(map, current_player):
        print_map(map)
        if current_player == X:
            print('Победили крестики!')
        else:
            print('Победили нолики!')
        break
    elif is_tie(map):
        print_map(map)
        print("Ничья!")
        break

    switch_player()