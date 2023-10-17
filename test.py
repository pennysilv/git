row, column = map(int, input().split())
field = []
field.append('.' * (column + 2))
for i in range(row):
    field.append('.' + input() + '.')
field.append('.' * (column + 2))
count = 0
for i in range(1, row + 1):
    for j in range(1, column + 1):
        if field[i][j] == field[i][j - 1] == field[i][j + 1] == field[i - 1][j] == field[i + 1][j] == '.':
            count += 1
print(count)
