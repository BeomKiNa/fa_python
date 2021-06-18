# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본 출력
print("Hello Python!", "so cool")
print("Hello Python!")
print("""Hello Python!""")
print("""Hello Python!""")

print()

# Separator 옵션
print("T", "E", "S", "T", sep="")
print("2020", "06", "13", sep="-")
print("beomki69", "gmail.com", sep="@")

# End 옵션
print("Welcome To", end=" ")
print("the Python World", end=" ")
print("Nice to see you")

print()

# format
print("{} and {}".format("you", "me"))
print("{0} and {1} and {0}".format("you", "me"))
print("{a} and {b}".format(a="you", b="me"))

# %s: 문자 ,%d: 정수, %f: 실수
print("%s's favorite number is %d" % ("Beomki", 7))

print("Test1: %5d, Price: %4.2f" % (776, 6543.123))
print("Test1: {0:5d}, Price:{1: 4.2f}".format(776, 6543.123))
print("Test1: {a:5d}, Price:{b: 4.2f}".format(a=776, b=6543.123))

"""
참고 : Escape 코드
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...
"""

print("'you'")
print("'you'")  # black이 멋대로 바꾼다...
print('"you"')
print("""'you'""")
print("\\you\\\n")
print("\t\t\t\ttest")
