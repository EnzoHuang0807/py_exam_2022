
R , C = map(int,input().split())
seat = []

for i in range(R):
        seat.append(list(map(int, input().split())))

row, col = map(int, input().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())

for i in range(N):

    direction = int(input())
    r = dr[direction - 1]
    c = dc[direction - 1]

    if (row + r < R  and row + r >= 0) and (col + c < C and col + c >= 0):
        temp = seat[row][col]
        seat[row][col] = seat[row + r][col + c]
        seat[row + r][col + c] = temp
        row += r
        col += c

for i in range(R):
    print(* seat[i])
