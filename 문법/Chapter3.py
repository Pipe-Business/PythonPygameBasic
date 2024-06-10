# Chapter3. 연산자
# 연산자
# 산술연산자 : 덧셈,뺄셈,나눗셈,곱셉 등...
a = 7
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a // b)  # 몫 (정수 나눗셈)
print(a % b)  # 나머지

print(1 + 3 * 6)
print((1 + 3) * 6)

# 비교 연산자
# 두값을 비교해서 결과를 True 나 False 반환
# <,>,<=,>=,==,!=
print(3 > 5)
print(4 > 6)
print(4 <= 4)
print(5 == 1)
print(12 != 12)

# 논리 연산자 : 두 논리 연산을 True 인지 False 인지 계산
# and, or, not
# and : 두 논리가 모두 참일때 True 나머지 경우는 False
# or : 두 논리 중에 하나만 True 이면 True
# not : 결과값을 뒤집음
score = 100
age = 22
print(score == 100 and age > 10)
print(score < 50 or age != 22)
print(not age < 10)
