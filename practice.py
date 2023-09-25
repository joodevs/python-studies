# #1 출력하기01
# print("Hello")
#
# #2 출력하기02
# print("Hello World")
#
# #3 출력하기03
# print("Hello")
# print("World")
#
# #4 출력하기04
# print("'Hello'")
#
# #5 출력하기05
# print('"Hello World"')
#
# #6 출력하기06
# print("\"!@#$%^&*()\'")
#
# #07 출력하기07
# print("\"C:\Download\\'hello'.py\"")
#
# #08 출력하기08
# print("print(\"Hello\\nWorld\")")
#
# #09 문자 1개 입력받아 그대로 출력하기
# c = input()
# print(c)
#
# #10 정수 1개 입력받아 int로 변환하여 출력하기
# n = input()
# n = int(n)
# print(n)
#
# #11 실수 1개 입력받아 변환하여 출력하기
# f = input()
# f = float(f)
# print(f)
#
# #12 정수 2개 입력받아 그대로 출력하기 1
# a = int(input())
# b = int(input())
# print(a)
# print(b)
#
# #13 문자 2개 입력받아 순서 바꿔 출력하기
# c1 = input()
# c2 = input()
# print(c2)
# print(c1)
#
# #14 실수 1개 입력받아 3번 출력하기
# f = float(input())
# for i in range(3):
#     print(f)
#
# #15 정수 2개 입력받아 그대로 출력하기 2
# a, b = map(int, input().split())
# print(a)
# print(b)
#
# #16 문자 2개 입력받아 순서 바꿔 출력하기 2
# c1, c2 = input().split()
# print(c2)
# print(c1)
#
# #17 문장 1개 입력받아 3번 출력하기
# s = input()
# print(s, s, s)
#
# #18 시간 입력받아 그대로 출력하기
# a,b = input().split(':')
# print(a,b, sep=':')
#
# #19 연월일 입력받아 순서 바꿔 출력하기
# y, m, d = input().split('.')
# print(d, m, y, sep='-')
#
# #20 주민번호 입력받아 형태 바꿔 출력하기
# ssn1, ssn2 = input().split('-')
# print(ssn1 + ssn2)
#
# #21 단어 1개 입력받아 나누어 출력하기
# s = input()
# for i in range(len(s)):
#     print(s[i])
#
# #22 연월일 입력받아 나누어 출력하기
# s = input()
# print(s[0:2], s[2:4], s[4:6], sep=' ')
#
# #23 시분초 입력받아 분만 출력하기
# h,m,s = input().split(':')
# print(m)
#
# #24 단어 2개 입력받아 이어 붙이기
# w1,w2 = input().split()
# s = w1 + w2
# print(s)
#
# #25 정수 2개 입력받아 합 계산하기
# a,b = input().split()
# sum = int(a) + int(b)
# print(sum)
#
# #26 실수 2개 입력받아 합 계산하기
# f1 = float(input())
# f2 = float(input())
# print(f1 + f2)
#
# #27 10진 정수 입력 받아 16진수로 출력하기 1
# n = int(input())
# print('%x'%n)
#
# #28 10진 정수 입력받아 16진수로 출력하기 2
# n = int(input())
# print('%X'%n)
#
# #29 16진 정수 입력받아 8진수로 출력하기
# n = int(input(), 16)
# print('%o' %n)
#
# #30 영문자 1개 입력받아 10진수로 변환하기
# n = ord(input())
# print(n)
#
# #31 정수 입력받아 유니코드 문자로 변환하기
# c = int(input())
# print(chr(c))
#
# #32 정수 1개 입력받아 부호 바꾸기
# n = int(input())
# print(-n)
#
# #33 문자 1개 입력받아 다음 문자 출력하기
# n = ord(input())
# print(chr(n+1))
#
# #34 정수 2개 입력받아 차 계산하기
# a, b = map(int, input().split())
# c = a - b
# print(c)
#
# #35 실수 2개 입력받아 곱 계산하기
# f1, f2 = map(float, input().split())
# m = f1 * f2
# print(m)
#
# #36 단어 여러 번 출력하기
# w, n = input().split()
# print(w*int(n))
#
# #37 문장 여러 번 출력하기
# n = input()
# s = input()
# print(int(n)*s)
#
# #38 정수 2개 입력받아 거듭제곱 계산하기
# a, b = map(int, input().split())
# c = a**b
# print(c)
#
# #39 실수 2개 입력받아 거듭제곱 계산하기
# f1, f2 = map(float, input().split())
# m = f1**f2
# print(m)
#
# #40 정수 2개 입력받아 나눈 몫 계산하기
# a, b = map(int, input().split())
# print(a//b)
#
# #41 정수 2개 입력받아 나눈 나머지 계산하기
# a, b = map(int, input().split())
# print(a%b)
#
# #42 실수 1개 입력받아 소숫점이하 자리 변환하기
# a = float(input())
# print(format(a, ".2f"))
#
# #43 실수 2개 입력받아 나눈 결과 계산하기
# f1, f2 = map(float, input().split())
# print(format(f1/f2, ".3f"))
#
# #44 정수 2개 입력받아 자동 계산하기
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(format(a/b, ".2f"))
#
# #45 정수 3개 입력받 합과 평균 출력하기
# a, b, c = map(int, input().split())
# sum = a + b + c
# avg = sum / 3
# print(sum, format(avg, ".2f"))
#
# #46 정수 1개 입력받아 2배 곱해 출력하기
# n = int(input())
# print(n<<1)
#
# #47 2의 거듭제곱 배로 곱해 출력하기
# a, b = map(int, input().split())
# print(a<<b)
#
# #48 정수 2개 입력받아 비교하기 1
# a, b = map(int, input().split())
# if a < b:
#     print(True)
# else:
#     print(False)
#
# #49 정수 2개 입력받아 비교하기 2
# a, b = map(int, input().split())
# if a == b:
#     print(True)
# else:
#     print(False)
#
# #50 정수 2개 입력받아 비교하기 3
# a, b = map(int, input().split())
# if a <= b:
#     print(True)
# else:
#     print(False)
#
# #51 정수 2개 입력받아 비교하기 4
# a, b = map(int, input().split())
# if a != b:
#     print(True)
# else:
#     print(False)
#
# #52 정수 입력받아 참 거짓 평가하기
# n = int(input())
# print(bool(n))
#
# #53 참 거짓 바꾸기
# a = bool(int(input()))
# print(not a)
#
# #54 둘 다 참일 경우만 참 출력하기
# a, b = map(int, input().split())
# print(bool(a and b))
#
# #55 하나라도 참이면 참 출력하기
# a, b = map(int, input().split())
# print(bool(a or b))
#
# #56 참/거짓이 서로 다를 때에만 참 출력하기
# a, b = map(int, input().split())
# print(bool(((not a) and b) or (a and (not b))))
#
# #57 참/거짓이 서로 같을 때에만 참 출력하기
# a, b = map(int, input().split())
# print(bool(a) == bool(b))
#
# #58 둘 다 거짓일 경우만 참 출력하기
# a, b = map(int, input().split())
# print(not(a or b))
#
# #59 비트단위로 NOT 하여 출력하기
# n = int(input())
# print(~n)
#
# #60 비트단위로 AND 하여 출력하기
# n1, n2 = map(int, input().split())
# print(n1 & n2)
#
# #61 비트단위로 OR 하여 출력하기
# n1, n2 = map(int, input().split())
# print(n1 | n2)
#
# #62 비트단위로 XOR 하여 출력하기
# n1, n2 = map(int, input().split())
# print(n1 ^ n2)
#
# #63 정수 2개 입력받아 큰 값 출력하기
# a, b = map(int, input().split())
# print(a if (a>=b) else b)
#
# #64 정수 3개 입력받아 가장 작은 값 출력하기
# a, b, c = map(int, input().split())
# print((a if (a<b) else b) if ((a if (a<b) else b) < c) else c)
#
# #65 정수 3개 입력받아 짝수만 출력하기
# a, b, c = map(int, input().split())
# if a%2 == 0:
#     print(a)
# if b%2 == 0:
#     print(b)
# if c%2 == 0:
#     print(c)
#
# #66 정수 3개 입력받아 짝/홀 출력하기
# a, b, c = map(int, input().split())
# # print("even" if a%2 == 0 else print("odd"))
# # print("even" if b%2 == 0 else print("odd"))
# # print("even" if c%2 == 0 else print("odd"))
#
# if a%2==0:
#     print("even")
# else:
#     print("odd")
#
# if b%2==0:
#     print("even")
# else:
#     print("odd")
#
# if c%2==0:
#     print("even")
# else:
#     print("odd")
#
# #67 정수 1개 입력받아 분류하기
# n = int(input())
# if n < 0:
#     if n%2==0:
#         print('A')
#     else:
#         print('B')
# else:
#     if n%2==0:
#         print('C')
#     else:
#         print('D')
#
# #68 점수 입력받아 평가 출력하기
# n = int(input())
# if n >= 90:
#     print('A')
# else:
#     if n>=70:
#         print('B')
#     else:
#         if n>= 40:
#             print('C')
#         else:
#             print('D')
#
# #69 평가 입력받아 다르게 출력하기
# eval = input()
# if eval == 'A':
#     print('best!!!')
# elif eval == 'B':
#     print('good!!')
# elif eval == 'C':
#     print('run!')
# elif eval == 'D':
#     print('slowly~')
# else:
#     print('what?')
#
# #70 월 입력받아 계절 출력하기
# n = int(input())
# if n//3==1:
#     print("spring")
# elif n//3==2:
#     print('summer')
# elif n//3==3:
#     print('fall')
# else:
#     print('winter')
#
# #71 0이 입력될 때까지 무한 출력하기
# n = 1
# while n != 0:
#     n = int(input())
#     if n != 0:
#         print(n)
#
# #72 정수 1개 입력받아 카운트다운 출력하기 1
# n = int(input())
# while n != 0:
#     print(n)
#     n = n-1
#
# #73 정수 1개 입력받아 카운트다운 출력하기 2
# n = int(input())
# while n != 0:
#     n = n-1
#     print(n)
#
# #74 문자 1개 입력받아 알파벳 출력하기
# c = ord(input())
# t = ord('a')
# while t <= c:
#     print(chr(t), end=' ')
#     t += 1
#
# #75 정수 1개 입력받아 그 수까지 출력하기 1
# n = int(input())
# i = 0
# while i <= n:
#     print(i)
#     i = i+1
#
# #76 정수 1개 입력받아 그 수까지 출력하기 2
# n = int(input())
# for i in range(n+1):
#     print(i)
#
# #77 짝숫 합 구하기
# n = int(input())
# sum = 0
# for i in range(n+1):
#     if i % 2 == 0:
#         sum = sum + i
#     i = i+1
# print(sum)
#
# #78 원하는 문자가 입력될 때까지 반복 출력하기
# n = 'a'
# while n != 'q':
#     n = input()
#     print(n)
#
#
# #80: 주사위 2개 던지기
# n, m = map(int, input().split())
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i, j)
#
# #81 16진수 구구단 출력하기
# n = int(input(), 16)
# for i in range(1, 16):
#     print("%X*%X=%X"%(n,i,n*i))
#
# #82 3 6 9 게임의 왕이 되자
# n = int(input())
# for i in range(1, n+1):
#     if (i%10==3) | (i%10==6) | (i%10==9):
#         print("X", end=' ')
#     else: print(i, end=' ')

#83 빛 섞어 색 만들기
r, g, b = map(int, input().split())
n = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            n = n + 1
print(n)

#84 소리 파일 저장용량 계산하기
h, b, c, s = map(int, input().split())
print(round(h*b*c*s/8/1024/1024,1),'MB')