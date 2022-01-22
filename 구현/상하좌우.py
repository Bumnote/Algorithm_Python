def isSafe(y, x):
    return 0 < y <= n and 0 < x <= n


n = int(input())

x = 1
y = 1

plan = list(input().split())

for dir in plan:
    if dir == 'R':
        if isSafe(y, x + 1):
            x += 1
        else:
            pass
    elif dir == 'L':
        if isSafe(y, x - 1):
            x -= 1
        else:
            pass
    elif dir == 'U':
        if isSafe(y - 1, x):
            y -= 1
        else:
            pass
    else:
        if isSafe(y + 1, x):
            y += 1
        else:
            pass

print(y, x)
