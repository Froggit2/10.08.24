import sqlite3

conection = sqlite3.connect('not_telegram.db')
cursor = conection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTAGER NOT NULL
)''')

ag = 0
for i in range(10):
    bal = 1000
    i += 1
    ag += 10
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", f"{ag}", f"{bal}"))
    cursor.execute("UPDATE Users SET balance = ? WHERE age = ?", (500, f"{i // 2 == 0}"))


conection.commit()
conection.close()