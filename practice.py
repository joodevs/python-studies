#1 출력하기01
print("Hello")

#2 출력하기02
print("Hello World")

#3 출력하기03
print("Hello")
print("World")

#4 출력하기04
print("'Hello'")

#5 출력하기05
print('"Hello World"')

#6 출력하기06
print("\"!@#$%^&*()\'")

#07 출력하기07
print("\"C:\Download\\'hello'.py\"")

#08 출력하기08
print("print(\"Hello\\nWorld\")")

#09 문자 1개 입력받아 그대로 출력하기
c = input()
print(c)

#10 정수 1개 입력받아 int로 변환하여 출력하기
n = input()
n = int(n)
print(n)

#11 실수 1개 입력받아 변환하여 출력하기
f = input()
f = float(f)
print(f)

#12 정수 2개 입력받아 그대로 출력하기 1
a = int(input())
b = int(input())
print(a)
print(b)

#13 문자 2개 입력받아 순서 바꿔 출력하기
c1 = input()
c2 = input()
print(c2)
print(c1)

#14 실수 1개 입력받아 3번 출력하기
f = float(input())
for i in range(3):
    print(f)

#15 정수 2개 입력받아 그대로 출력하기 2
a, b = map(int, input().split())
print(a)
print(b)

#16 문자 2개 입력받아 순서 바꿔 출력하기 2
c1, c2 = input().split()
print(c2)
print(c1)

#17 문장 1개 입력받아 3번 출력하기
s = input()
print(s, s, s)

#18 시간 입력받아 그대로 출력하기
a,b = input().split(':')
print(a,b, sep=':')

#19 연월일 입력받아 순서 바꿔 출력하기
y, m, d = input().split('.')
print(d, m, y, sep='-')

#20 주민번호 입력받아 형태 바꿔 출력하기
ssn1, ssn2 = input().split('-')
print(ssn1 + ssn2)

#21 단어 1개 입력받아 나누어 출력하기
s = input()
for i in range(len(s)):
    print(s[i])

#22 연월일 입력받아 나누어 출력하기
s = input()
print(s[0:2], s[2:4], s[4:6], sep=' ')

#23 시분초 입력받아 분만 출력하기
h,m,s = input().split(':')
print(m)

#24 단어 2개 입력받아 이어 붙이기
w1,w2 = input().split()
s = w1 + w2
print(s)

#25 정수 2개 입력받아 합 계산하기
a,b = input().split()
sum = int(a) + int(b)
print(sum)

#26 실수 2개 입력받아 합 계산하기
f1 = float(input())
f2 = float(input())
print(f1 + f2)

#27 10진 정수 입력 받아 16진수로 출력하기 1
n = int(input())
print('%x'%n)

#28 10진 정수 입력받아 16진수로 출력하기 2
n = int(input())
print('%X'%n)

#29 16진 정수 입력받아 8진수로 출력하기
n = int(input(), 16)
print('%o' %n)

#30 영문자 1개 입력받아 10진수로 변환하기
n = ord(input())
print(n)

#31 정수 입력받아 유니코드 문자로 변환하기
c = int(input())
print(chr(c))

#32 정수 1개 입력받아 부호 바꾸기
n = int(input())
print(-n)

#33 문자 1개 입력받아 다음 문자 출력하기
n = ord(input())
print(chr(n+1))

#34 정수 2개 입력받아 차 계산하기
a, b = map(int, input().split())
c = a - b
print(c)

#35 실수 2개 입력받아 곱 계산하기
f1, f2 = map(float, input().split())
m = f1 * f2
print(m)

#36 단어 여러 번 출력하기
w, n = input().split()
print(w*int(n))

#37 문장 여러 번 출력하기
n = input()
s = input()
print(int(n)*s)

#38 정수 2개 입력받아 거듭제곱 계산하기
a, b = map(int, input().split())
c = a**b
print(c)

#39 실수 2개 입력받아 거듭제곱 계산하기
f1, f2 = map(float, input().split())
m = f1**f2
print(m)

#40 정수 2개 입력받아 나눈 몫 계산하기
a, b = map(int, input().split())
print(a//b)

#41 정수 2개 입력받아 나눈 나머지 계산하기
a, b = map(int, input().split())
print(a%b)

#42 실수 1개 입력받아 소숫점이하 자리 변환하기
a = float(input())
print(format(a, ".2f"))

#43 실수 2개 입력받아 나눈 결과 계산하기
f1, f2 = map(float, input().split())
print(format(f1/f2, ".3f"))

#44 정수 2개 입력받아 자동 계산하기
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, ".2f"))

#45 정수 3개 입력받 합과 평균 출력하기
a, b, c = map(int, input().split())
sum = a + b + c
avg = sum / 3
print(sum, format(avg, ".2f"))

#46 정수 1개 입력받아 2배 곱해 출력하기
n = int(input())
print(n<<1)

#47 2의 거듭제곱 배로 곱해 출력하기
a, b = map(int, input().split())
print(a<<b)

#48 정수 2개 입력받아 비교하기 1
a, b = map(int, input().split())
if a < b:
    print(True)
else:
    print(False)

#49 정수 2개 입력받아 비교하기 2
a, b = map(int, input().split())
if a == b:
    print(True)
else:
    print(False)

#50 정수 2개 입력받아 비교하기 3
a, b = map(int, input().split())
if a <= b:
    print(True)
else:
    print(False)