n = int(input())

# 00:00:00 ~ n:59:59 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수
cnt = 0
hour = 0
minute = 0
second = 0
while True:
    if hour == n and minute == 59 and second == 59:
        print(cnt)
        break
    if '3' in str(hour) or '3' in str(minute) or '3' in str(second):
        cnt += 1

    second += 1
    if second == 60:
        minute += 1
        second = 0
        if minute == 60:
            hour += 1
            minute = 0

# 답안 예시
# h = int(input())
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
#             # 문자열끼리 더하면 앞 문자열 뒤에 붙는다.
#             if '3' in str(i)+str(j)+str(k):
#                 cnt+=1
# print(cnt)
