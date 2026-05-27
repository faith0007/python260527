# Python의 list, tuple, dict, set 비교 예제

# 1. 생성
my_list = [1, 2, 3, 3]
my_tuple = (1, 2, 3, 3)
my_dict = {"a": 1, "b": 2, "c": 3}
my_set = {1, 2, 3}

# 2. 출력
print("List :", my_list)
print("Tuple:", my_tuple)
print("Dict :", my_dict)
print("Set  :", my_set)

# 3. 특징 비교
print("\n=== 특징 비교 ===")

# List
print("\n[List]")
print("- 순서 있음")
print("- 수정 가능")
print("- 중복 허용")
my_list.append(4)
print("append 후:", my_list)

# Tuple
print("\n[Tuple]")
print("- 순서 있음")
print("- 수정 불가능")
print("- 중복 허용")
print("Tuple 값:", my_tuple)

# Dict
print("\n[Dict]")
print("- key:value 형태")
print("- key는 중복 불가")
print("- 수정 가능")
my_dict["d"] = 4
print("추가 후:", my_dict)

# Set
print("\n[Set]")
print("- 순서 없음")
print("- 중복 제거")
print("- 수정 가능")
my_set.add(4)
print("add 후:", my_set)

# 4. 중복 비교
print("\n=== 중복 비교 ===")
print("List 길이 :", len(my_list))
print("Tuple 길이:", len(my_tuple))
print("Set 길이  :", len(my_set))

# 5. 타입 확인
print("\n=== 타입 확인 ===")
print(type(my_list))
print(type(my_tuple))
print(type(my_dict))
print(type(my_set))