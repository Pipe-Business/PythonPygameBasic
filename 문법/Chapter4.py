# Chapter5. list 와 tuple
# 리스트와 튜플
# 여러변수를 연속적으로 저장 : 시퀀스데이터

# 리스트
my_list = ["apple", "banana", "cookie"]

print(my_list, type(my_list))

# 리스트 : 추가 (append)
# 리스트의 가장 뒤에 값을 추가
my_list.append("cake")
print(my_list)

# 리스트 : 조회 (리스트[원하는 위치값])
# 첫번쨰 위치가 0으로 시작합니다.
print(my_list[0])
print(my_list[2])

# 리스트 : 수정 (리스트[원하는 위치값] = 바꿀값)
my_list[0] = "mango"
print(my_list)

# 리스트 : 삭제 (remove,pop)
my_list.remove("cake")
print(my_list)
removed_value = my_list.pop(1)
print(removed_value)
print(my_list)

# 튜플
my_tuple = (1,)
print(my_tuple, type(my_tuple))
# 튜플은 리스트처럼 추가 수정 삭제연산이 불가능

# 리스트와 튜플의 공통점
# - 여러변수를 연속적으로 저장할수 있는 시퀀스데이터
# - 첫번째값의 위치는 0부터 시작
# 차이점
# - 리스트
#     - 수정 ,삭제, 추가 등 다양한 함수를 제공 (가변성 mutable)
#     - 리스트를 쓸때는 대괄호 [ ]
# - 튜플
#     - 한번 선언하면 수정 삭제 추가등이 불가능 (불변성 immutable)
#     - 튜플을 쓸때는 소괄호 ( )
