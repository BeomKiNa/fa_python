# 딕셔너리 순서 X, 중복 X, 수정 O, 삭제 O

a = {"name": "Na", "Phone": "010-8888-8888", "birth": 920609}
b = {0: "hello", 1: "world"}
c = {"arr": [1, 2, 3, 4, 5]}

print(type(a))
print(a["name"])
print(a.get("name"))
print(a.get("address"))  # get을 사용하면 에러가 발생하지 않음
print(c["arr"][1:3])

a["address"] = "Seoul"
print(a)
a["rank"] = [1, 3, 4]
a["rank2"] = (
    1,
    2,
    3,
)
print(a)

print(a.keys())
temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

print(2 in b)
print("name2" not in a)

# 집합 (Sets) (순서 X, 중복 X)

a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1.union(s2))
print(s1 | s2)

print(s1.difference(s2))
print(s1 - s2)

# 추가, 제거

s3 = set([7, 8, 10, 15])

s3.add(18)
s3.add(7)
print(s3)

s3.remove(15)
print(s3)

print(type(s3))
