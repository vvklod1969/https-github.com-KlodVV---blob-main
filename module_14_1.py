import sqlite3

# создаем и подключаемся к базе данных
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

# создаем таблицу Users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

# вносим в таблицу 10 записей
for i in range(1, 11): # цикл для вставки 10 записей.
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

# обновляем баланс каждой 2-й записи
for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))


# удаляем каждую 3 запись
for i in range(3, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

# выбираем все записи, где возраст не равен 60 и выводим  на консоль
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
records = cursor.fetchall()

print("Вывод на консоль:")
for record in records:
    username, email, age, balance = record
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")


# сохраняем изменения и закрываем
connection.commit()
connection.close()