# 예제 _ 2 / 시간 복잡도 --> log 복잡도를 가진다.
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
