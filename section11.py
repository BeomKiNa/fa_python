# excel, csv 파일 읽기 및 쓰기

# CSV: MIME - text/csv

import csv

with open("./resource/sample1.csv", "r", encoding="euc-kr") as f:
    reader = csv.reader(f)
    # next(reader) # Header를 싑하기 위해 사용됨, 한 행을 건너뜀
    print(dir(reader))
    print()

    for c in reader:
        print(c)
print("\n--------------------------------------------------------\n")

with open("./resource/sample2.csv", "r", encoding="euc-kr") as f:
    reader = csv.reader(f, delimiter="|")
    # next(reader) # Header를 싑하기 위해 사용됨, 한 행을 건너뜀
    print(dir(reader))
    print()

    for c in reader:
        print(c)
print("\n--------------------------------------------------------\n")

# Dict 변환
with open("./resource/sample1.csv", "r", encoding="euc-kr") as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print("**************")
print("\n--------------------------------------------------------\n")

w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open("./resource/sample3.csv", "w", newline="") as f:
    wt = csv.writer(f)
    for v in w:
        wt.writerow(v)

with open("./resource/sample4.csv", "w", newline="") as f:
    wt = csv.writer(f)
    wt.writerows(w)

# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils...
# pandas 를 주로 사용 (내부적으로 openpyxl, xlrd를 사용)

import pandas as pd

xlsx = pd.read_excel(
    "./resource/sample.xlsx"
)  # sheetname='시트명' 또는 숫자, header=3, skiprow=1 실습

# 상위 데이터 확인
print(xlsx.head())
print()

# 데이터 확인
print(xlsx.tail())
print()

# 데이터 구조
print(xlsx.shape)  # 행, 열


# 엑셀 or CSV 다시 쓰기
xlsx.to_excel("./resource/result.xlsx", index=False)
xlsx.to_csv("./resource/result.csv", index=False)
