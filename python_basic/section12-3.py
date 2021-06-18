# 테이블 수정, 삭제

import sqlite3

conn = sqlite3.connect(
    "/Users/ki/project/fa_python/python-basic/resource/database.db"
)

c = conn.cursor()

# 수정1
c.execute("UPDATE users SET username = ? WHERE id = ?", ("niceman", 2))

# 수정2
c.execute(
    "UPDATE users SET username = :name WHERE id = :id",
    {"name": "Goodman", "id": 5},
)
# 수정3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ("Badboy", 3))

# 중간 데이터 확인
for user in c.execute("SELECT * FROM users"):
    print(user)

# Row Delete1
c.execute("DELETE FROM users WHERE id = ?", (2,))

# Row Delete2
c.execute("DELETE FROM users WHERE id = :id", {"id": 5})

# Row Delete3
c.execute("DELETE FROM users WHERE id = '%s'" % 4)

# 중간 데이터 확인
for user in c.execute("SELECT * FROM users"):
    print(user)

# 테이블 전체 데이터 삭제
print("users db deleted:", conn.execute("DELETE FROM users").rowcount, "rows")

conn.commit()

# 접속 해제
conn.close()
