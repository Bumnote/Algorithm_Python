# 문자열 재정렬
# ex) K1KA5CB7 --> ABCKK13 / AJKDLSI412K4JSJ9D --> ADDIJJKKLSS20
# 알파벳 문자는 정렬하고, 숫자 문자는 모두 더한 값을 가장 뒤에 붙여서 출력

s = input()
number = 0
answer = ""
cnt = 0
# 숫자는 따로 더해주고 , remove 하지 않는다.
for i in range(len(s)):
    if ord('0') <= ord(s[i]) <= ord('9'):
        number += int(s[i])
        # list slice 를 하기 위해서 cnt 변수를 생성
        # --> 숫자가 알파벳보다 아스키 코드가 작기 때문에 슬라이싱하는 것이 더 효율적이라고 판단
        cnt += 1
    else:
        pass

s = sorted(s)
# join 함수를 이용해서 문자열 생성
answer = "".join(s[cnt:]) + str(number)
