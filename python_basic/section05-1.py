# if

if True:
    print("true")

if False:
    print("false")
else:
    print("false-else")

# 참 같은 값
# "내용", [내용], (내용), {내용}, 0을 제외한 숫자

print(bool("a"))
print(bool([1]))
print(bool((2,)))
print(bool({"name": "Ki"}))
print(bool(1), bool(-3), bool(58))

# 거짓 같은 값
# "", [], (), {}, 0

print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(0))

# 관계 연산자
# > , >=, <, <=, ==, !=

# 논리 연산자
# and, or, not

a = 100
b = 60
c = 15
print("and: ", a > b and b > c)
print("or: ", a > b or b > c)
print("not: ", not a > b)

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용
print(5 + 10 > 0 and not 7 + 3 == 10)


score1 = 90
score2 = "A"

if score1 >= 90 and score2 == "A":
    print("합격!")
else:
    print("불합격!")


# 다중조건문
num = 70

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("꽝", num)

# 중첩조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A 지원가능")
    elif height >= 160:
        print("B 지원가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")
