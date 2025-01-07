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
for i in range(1, 11):  # цикл для вставки 10 записей.
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

# сохраняем изменения
connection.commit()

# --- решаем задачу "Средний баланс пользователя" ---

# Удаляем запись с id = 6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))


# Подсчитываем общее количество записей
cursor.execute("SELECT COUNT(*) FROM Users")
total_records = cursor.fetchone()[0]
print(f"\nОбщее количество записей: {total_records}")

# Подсчитываем сумму всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]
print(f"Сумма всех балансов: {total_balance}")

# Вычисляем и выводим средний баланс
if total_records > 0:
    average_balance = total_balance / total_records
    print(f"Средний баланс всех пользователей: {average_balance:.2f}")
else:
    print("Нет записей в базе данных для расчета среднего баланса.")


# сохраняем изменения и закрываем
connection.commit()
connection.close()