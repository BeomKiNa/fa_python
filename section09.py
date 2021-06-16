# 파일 read, write
# 읽기 모드: r, 쓰기 모드(기존 파일 삭제): w, 추가 모드(파일 생성 또는 추가): a
# 상대 경로('../', './'), 절대 경로 확인('C:\...')
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
f = open("./resource/review.txt", "r")
content = f.read()
print(content)
print(dir(f))
# 반드시 close로 리소스 반환
f.close

print("-------------------------------------")
print("-------------------------------------")

with open("./resource/review.txt", "r") as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print("-------------------------------------")
print("-------------------------------------")


with open("./resource/review.txt", "r") as f:
    for c in f:
        print(c.strip())

print("-------------------------------------")
print("-------------------------------------")

with open("./resource/review.txt", "r") as f:
    content = f.read()
    print(">", content)
    content = f.read()  # 내용 없음
    print(">", content)

print("-------------------------------------")
print("-------------------------------------")

with open("./resource/review.txt", "r") as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end=" #### ")
        line = f.readline()

print("-------------------------------------")
print("-------------------------------------")

with open("./resource/review.txt", "r") as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=" ********* ")

print("-------------------------------------")
print("-------------------------------------")

score = []
with open("./resource/score.txt", "r") as f:
    for line in f:
        score.append(int(line))
    print(score)

print("Average : {:6.3}".format(sum(score) / len(score)))

# 파일 쓰기

with open("./resource/text1.txt", "w") as f:
    f.write("Niceman!\n")

with open("./resource/text1.txt", "a") as f:
    f.write("Goodman!\n")

from random import randint

with open("./resource/text2.txt", "w") as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write("\n")

# writelines: 리스트 -> 파일로 저장
with open("./resource/text3.txt", "w") as f:
    list1 = ["Kim\n", "Park\n", "Cho\n"]
    f.writelines(list1)

with open("./resource/text4.txt", "w") as f:
    print("Test Contents1!", file=f)
    print("Test Contents2!", file=f)
