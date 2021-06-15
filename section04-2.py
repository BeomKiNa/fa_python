str1 = "I am Boy."
str2 = "NiceMan."
str3 = ""
str4 = str("")

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = 'Do you have a "big collection"'
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r"C:\Programs\Test\Bin"
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인

multi = """
문자열 
멀티라인 
테스트
"""

print(multi)

str_o1 = "*"
str_o2 = "abc "
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o2 * 3)
print("a" in str_o4)
print("f" in str_o4)
print("z" not in str_o4)

# 문자열 형 변환
print(str(77) + "a")
print(str(10.4))

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp
print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("s"))
print("join str: ", str_o1.join(["I'm ", "!"]))
print("replace1: ", str_o1.replace("Nice", "Good"))
print("replace2: ", str_o3.replace("is", "was", 3))
print("split: ", str_o4.split(" "))  # Type 확인
print("sorted: ", sorted(str_o1))  # reverse=True
print("reversed1: ", reversed(str_o2))  # list 형 변환
print("reversed2: ", list(reversed(str_o2)))

# immutable 설명
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ 확인
# 출력
for i in im_str:
    print(i)

# im_str[0] = "T"  # 수정 불가(immutable)

# 슬라이싱(인덱싱)
# 일부분 추출(정말 중요)
str_sl = "Niceboy"

# 슬라이싱 연습
print(str_sl[0:3])
print(str_sl[: len(str_sl)])
print(str_sl[: len(str_sl) - 1])
print(str_sl[:])
print(str_sl[1:4:2])
print(str_sl[-3:6])
print(str_sl[1:-2])
print(str_sl[::-1])
print(str_sl[::2])

# immutable 삭제
del str_sl

# 아스키코드
a = "t"

print(ord(a))
print(chr(116))
