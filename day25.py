
def gen_next(v, x, y):
    next = (v * 252533) % 33554393
    if x == 0:
        x = y + 1
        y = 0
    else:
        x -= 1
        y += 1
    return [next, x, y]

a = [[0 for i in range(10)] for j in range(10)]

[v, x, y] = [20151125, 0, 0]

dx = 3010
dy = 3019

dx -= 1
dy -= 1

while True:
    [v, x, y] = gen_next(v, x, y)
    #a[x][y] = v
    if x == dx and y == dy:
        print(v)
        break

print('res =', v)
