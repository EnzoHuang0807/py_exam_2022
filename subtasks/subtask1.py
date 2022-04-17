from random import randint, shuffle

n = randint(3, 5)
m = randint(3, 5)
print(n, m)

id = [i for i in range(1, 10000)]
shuffle(id)

for i in range(n):
    for j in range(m):
        print(id[0], end = ' ')
        id.pop(0);
    print('')

row = randint(0, n - 1)
col = randint(0, m - 1)
print(row, col)

num = randint(1, 5)
print(num)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

i = 0
while i < num:
    direction = randint(1,2);
    r = dr[direction - 1]
    c = dc[direction - 1]
    if (row + r < n and row + r >= 0) and (col + c < m and col + c >= 0):
        print(direction)
        row += r
        col += c
        i += 1
