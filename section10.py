# 에러 및 예외

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter: 코드 스타일, 문법 체크

# SyntaxError: 잘못된 문법

# NameError: 참조 변수 없음

# ZeroDivisionError: 0 나누기 에러
# print(10/0)

# IndexError: 인덱스 범위 에러

# KeyError
dic = {"name": "Kim", "Age": 33, "City": "Seoul"}
# print(dic["hobby"])
print(dic.get("hobby"))

# AttributeError: 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time

print(time.time())
# print(time.month())

# ValueError: 참조 값이 없을 때 발생
x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError

# TypeError
x = [1, 2]
y = (1, 2)
z = "test"
# print(x + y)
print(x + list(y))
print("\n\n\n\n")

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장 (EAFP 코딩 스타일)

# try: 에러가 발생할 가능성이 있는 코드 실행
# except: 에러명1
# except: 에러명2
# else :에러가 발생하지 않았을 경우 실행
# finally: 항상 실행

name = ["Kim", "Lee", "Park"]

try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! in name".format(z, x + 1))
except ValueError:
    print("Not found it! - Occurred ValueError!")
else:
    print("OK! Else")

try:
    z = "Jin"
    x = name.index(z)
    print("{} Found it! in name".format(z, x + 1))
except:
    print("Not found it! - Occurred Error!")
else:
    print("OK! Else")

try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! in name".format(z, x + 1))
except:
    print("Not found it! - Occurred Error!")
else:
    print("OK! Else")
finally:
    print("Finally!!")

# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print("try")
finally:
    print("Finally!!")

try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! in name".format(z, x + 1))
except ValueError as l:
    print(l)
    print("Not found it! - Occurred ValueError!")
except IndexError:
    print("Not found it! - Occurred IndexError!")
except Exception:  # 기본값이기 때문에 다른 것들 보다 위에 있으면 모든 에러가 걸러짐
    print("Not found it! - Occurred Error!")
else:
    print("OK! Else")
finally:
    print("Finally!!")
print("\n\n\n\n")

# 예외 발생 : raise 키워드로 예외 직접 발생

try:
    a = "22"
    if a == "Kim":
        print("허가")
    else:
        raise IndexError
except ValueError:
    print("문제 발생!")
except Exception as f:
    print("그외 모든 문제!", f)
else:
    print("ok!")
