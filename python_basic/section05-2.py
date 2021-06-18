# 반복문

v1 = 1
while v1 < 11:
    print("v1: ", v1)
    v1 += 1
print()

for v2 in range(10):
    print("v2: ", v2)
print()

for v3 in range(1, 11):
    print("v3: ", v3)
print()

# 1~100 의 합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
print(sum1)

print("sum():", sum(range(1, 101)))
print("even sum():", sum(range(1, 101, 2)))

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수: range, reverse, enumerate, filter, map, zip

names = ["kim", "park", "cho", "choi", "yoo"]
for name in names:
    print("name: ", name)

word = "dreams"
for s in word:
    print("s:", s)

info = {"name": "beomki", "age": 33, "city": "Seoul"}
# 기본값은 키
for key in info:
    print("info: ", key)

for value in info.values():
    print("info-value: ", value)

for key in info.keys():
    print("info-key: ", key)


for key, value in info.items():
    print("info-item: ", key, value)

name1 = "BeomKi"
result = ""
for n in name1:
    if n.isupper():
        print(n.lower())
        result += n.lower()
    else:
        print(n.upper())
        result += n.upper()
print(result)

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for number in numbers:
    if number == 33:
        print("Found 33!")
        break
    else:
        print("Not found 33!")

# for - else 구문 (반복문이 정상적으로 수행 된 경우 else 블럭 수행)
for number in numbers:
    if number == 33:
        print("Found 33!")
        break
    else:
        print("Not found 33!")
else:
    print("Not found 33.......")

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("type: ", type(v))
