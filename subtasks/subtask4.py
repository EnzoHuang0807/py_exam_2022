from random import randint, shuffle

n = randint(3, 100)
m = randint(3, 100)
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

num = randint(1, 50000)
print(num)

for i in range(num):
    print(randint(1, 4))
