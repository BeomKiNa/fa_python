# 모듈, 패키지

# 상대 경로
# .. : 부모 디렉토리
# . : 현제 디렉토리

# 클래스 사용
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)
print("ex1: ", Fibonacci.fib2(400))
print("ex1: ", Fibonacci().title)

# 클래스 사용2
from pkg.fibonacci import *

Fibonacci.fib(500)
print("ex2: ", Fibonacci.fib2(600))
print("ex2: ", Fibonacci().title)

# 클래스 사용2
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)
print("ex2: ", fb.fib2(1600))
print("ex2: ", fb().title)

# 함수
import pkg.calculations as c

print("ex4: ", c.add(10, 100))
print("ex4: ", c.mul(10, 100))

# 함수2
from pkg.calculations import div as d

print("ex5: ", int(d(100, 10)))

# 함수3
import pkg.prints as p

p.prt1()
p.prt2()

# 기본제공 함수
import builtins

print(dir(builtins))
