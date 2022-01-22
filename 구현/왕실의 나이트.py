def isPossible(y, x):
    return 1 <= y <= 8 and 1 <= x <= 8


# 위치를 입력
position = input()
x, y = int(ord(position[0]) - 96), int(position[1])
# 나이트의 방향 벡터를 설정 --> 8가지 방향 설정
dx = [2, 2, -2, -2, -1, 1, -1, 1]
dy = [-1, 1, - 1, 1, 2, 2, -2, -2]
# dx, dy 가 아닌 튜플을 이용해서 하나의 리스트로도 구현 가능
# steps = [(-2,-1),(-1,-2,),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

answer = 0
for i in range(8):
    if isPossible(y + dy[i], x + dx[i]):
        answer += 1
    else:
        pass

print(answer)
