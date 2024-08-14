import sqlite3

connection = sqlite3.connect('not_telegram.db')  # написание 'connection'
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL    
)''')  # Исправлено 'INTAGER' на 'INTEGER'

ag = 0
for i in range(10):
    bal = 1000
    i += 1
    ag += 10
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", ag, bal))  # Убраны лишние кавычки для ag и bal

    if i % 2 == 0:  # Обновляем баланс только для четных id
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

    if i % 3 == 0:
        cursor.execute("DELETE FROM User WHERE username = ?", ("User1", ))

connection.commit()
connection.close()
