# 함수식 및 람다(lamda)


def hello(world):
    print("Hello ", world)


hello("Python")
hello(7777)


def hello_return(world):
    val = "Hello" + str(world)
    return val


str1 = hello_return("Python!!!!")
print(str1)

# 다중 return


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul(3)
print(val1, val2, val3)

# *args, *kwargs


def args_func(*args):
    print(args, type(args))
    # for t in args:
    #     print(t)
    for i, v in enumerate(args):
        print(i, v)


args_func("Kim")
args_func("Kim", "Park")
args_func("Kim", "Park", "Lee")
print()


def kwargs_func(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


kwargs_func(name1="Kim", name2="Park", name3="Lee")
print()


def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul("apple", "banana", "orange", "tomato", f1="lemon", f2="melon")
print()

# 중첩함수(클로저) -- 데코레이터를 나중에 학습하게 된다.
def nested_func(num):
    def func_in_func(num):
        print(">>>", num)

    print("in func")
    func_in_func(num + 10000)


nested_func(3)


def func_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 1000
    y3 = x * 10000
    return [y1, y2, y3]


print(func_mul3(6))

# 람다식: 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func, type(var_func))

lambda_mul_10 = lambda num: num * 10

print("lambda: ", lambda_mul_10(10))


def func_final(x, y, func):
    print(x * y * func(10))


func_final(2, 3, lambda_mul_10)

func_final(2, 3, lambda num: num * 100)
