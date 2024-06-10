# Chapter5. 조건문
# 조건문
# 조건에따라 프로그램의 흐름을 제어

score = 0

if score >= 90:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
    print("조금더 분발하세요")
else:
    print("불합격입니다.")
    print("다음엔 더 잘해봐요")

# in 연산 : 리스트같은 시퀀스데이터안에 찾고자 하는 값이 있는지 확인 (있다면 True 없다면 False)

my_list = ["apple", "mango", "cookie"]
find_value = "cookie"

if find_value in my_list:
    print(find_value, "가 존재합니다.")
    my_list.remove(find_value)
    print(my_list)
else:
    print(find_value, "가 존재하지 않습니다.")
