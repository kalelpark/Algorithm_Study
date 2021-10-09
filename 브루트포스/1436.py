import sys

num1 = int(sys.stdin.readline())

count = 0
six = 666
while 1:
    if '666' in str(six):           # 문자열 리스트로 파악하기
        count += 1
        if count == num1:
            print(six)
            break
    six += 1

# 이문제를 보고, 6이 연속인 값을 가지고 있어야 한다는 것을 파악해야 한다.
# 그리고, "항상 숫자가 어디에 존재하냐"라는 문제가 있는 경우
# 문자열로 변경해서 문제를 풀 수 있음을 생각해야 한다.
# 항상 문제 풀 때, 범위 놓치지 말자.
# 대체적으로 시간복잡도의 나온 값이 1억이 나ㅓㅁ지 않으면, 웬만한 무거운 연산도 1초안에 통과한다.