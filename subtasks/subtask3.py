from random import randint, shuffle

n = randint(3, 50)
m = randint(3, 50)
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

num = randint(1, 1000)
print(num)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

i = 0
while i < num:
    direction = randint(1, 4)
    i += 1
    print(direction)
