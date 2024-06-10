# 함수
# 어떤한 동작을 함수안에 정의하여 필요한 시점에 호출하여 사용
# 사용자 정의 함수 : 사용자가 직접 정의한 함수
def say_hello():
    print("hello")
    print("안녕")


say_hello()


def print_my_age(age, name):
    print(f"제 나이는 {age} 살 입니다. 제 이름은 {name} 이구요")


print_my_age(10, "python")
print_my_age(22, "snake")


# 함수에서 return 의 역할
# 1. 함수에 결괏값을 반환
# 2. 함수를 빠져나감

def add(a, b):
    print(f"{a} 랑 {b} 랑 더한 결과는 {a + b} 입니다.")
    return a + b


add_result = add(10, 30)
print(add_result)

# 내장함수: built-in-function 파이썬에서 기본적으로 내장되있는 함수 (print,type,sum,len,sorted )
li = [3, 10, 2, 1, 6]
print(sum(li))  # 리스트의 합계
print(len(li))  # 리스트의 크기
print(sorted(li))  # 리스트 정렬

# 외장함수: 파이썬에서 포함되있지 않은 함수 import 사용해 불러와서 사용
import random

print(random.random())  # 0~1사이의 실수 난수
print(random.randint(1, 10))  # 0~10 사이의 정수 난수
random.shuffle(li)
print(li)
print(random.sample(range(1, 46), 7))
