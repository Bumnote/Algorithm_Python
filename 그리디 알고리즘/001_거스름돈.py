# 예제 _ 1 / 시간 복잡도 --> 동전의 총 종류에만 영향을 받기 때문에 O(K) 이다.
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]
for coin in array:
    count += (n // coin)
    n %= coin

print(count)
