import sqlite3

new_connection = sqlite3.connect("data_testing.db")

print(type(new_connection))

new_cursor = new_connection.cursor()
print(type(new_cursor))

new_sql = "SELECT datetime('now', 'localtime');"
# new_cursor.execute(new_sql)
# new_cursor.fetchone()

new_dtime = new_cursor.execute(new_sql).fetchone()[0]
print(new_dtime)

new_connection.close()

# ======= 前面寫的東西可以整理成這樣 ======= Start
with sqlite3.connect('data_testing.db') as new_connection:
    new_cursor = new_connection.cursor()
    new_sql = "SELECT datetime('now', 'localtime');"
    new_dtime = new_cursor.execute(new_sql).fetchone()[0]

print(new_dtime)
# ======= 前面寫的東西可以整理成這樣 ======= End


# ======= 建立 table及資料 ======= Start
import sqlite3
new_connection = sqlite3.connect("data_testing.db")
new_cursor = new_connection.cursor()

# new_cursor.execute("CREATE TABLE clients(Name TEXT, Number INT);")
# new_cursor.execute("INSERT INTO clients VALUES('Deny', 2030)")

new_connection.commit()
new_connection.close()

# 查出剛才建立的資料
new_connection = sqlite3.connect("data_testing.db")
new_cursor = new_connection.cursor()

new_cursor.execute("SELECT * FROM clients;")
print(new_cursor.fetchmany())
# ======= 建立 table及資料 ======= End


# ======= 刪除 table ======= Start
# new_connection = sqlite3.connect("data_testing.db")
new_cursor.execute("DROP TABLE clients;")

new_connection.commit()
new_connection.close()
# ======= 刪除 table ======= End


# ====== 完整的程式碼用於獲取所有在 data_testing資料庫中的資料 ====== Start
import sqlite3

new_values = (
    ("Ronaldo", 7),
    ("Messi", 30),
    ("Salah", 11),
)

with sqlite3.connect("data_testing.db") as new_connection:
    new_cursor = new_connection.cursor()
    new_cursor.execute("DROP TABLE IF EXISTS clients")
    new_cursor.execute("CREATE TABLE clients(Name TEXT, Number INT);")

    # 多筆資料寫入
    new_cursor.executemany("INSERT INTO clients VALUES(?, ?)", new_values)

    new_cursor.execute("SELECT Name, Number FROM clients WHERE Number > 7;")

    for x in new_cursor.fetchall():
        print(x)
# ====== 完整的程式碼用於獲取所有在 data_testing資料庫中的資料 ====== End
