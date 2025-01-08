import sqlite3

DATABASE_NAME = 'products.db'


def initiate_db():
    """Создает таблицы Products и Users, если они еще не созданы."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            image_url TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    """)
    conn.commit()

    # Добавление данных о продуктах
    products_data = [
        ("Product 1",
         "Ускоряет сжигание жиров и предотвращает их накопление в организме,\nвыводит токсины, снижает уровень холестерина.\nНа 80% выгоднее зарубежного аналога",
         931, "https://shop.evalar.ru/upload/iblock/424/ub850grpfux6l7r2wtwhmshpe89xx7oo.png"),
        ("Product 2", "Морской хитозан из панцирей крабов для похудения, детокса, контроля уровня холестерина", 859,
         "https://shop.evalar.ru/upload/iblock/843/x95zvl4vqjjioi8ql0crhkxwcz3paddl.png"),
        ("Product 3",
         "Устраняет сразу несколько причин лишнего веса, способствует снижению аппетита, активизирует сжигание жиров",
         519, "https://shop.evalar.ru/upload/iblock/c51/mam75h042zsrfk7wgmdjhyhtzrugrzua.png"),
        ("Product 4", "Cпособствует снижению аппетита, помогает соблюдать диету и контролировать вес", 289,
         "https://shop.evalar.ru/upload/iblock/b70/h3hmu0dit5fqtlghhqcgurb8kwinqtkg.png")
    ]

    cursor.execute("SELECT COUNT(*) FROM Products")
    count = cursor.fetchone()[0]

    if count == 0:
        try:
            cursor.executemany("INSERT INTO Products (title, description, price, image_url) VALUES (?, ?, ?, ?)",
                               products_data)
            conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Ошибка при добавлении данных: {e}")  # Выводим ошибку

    conn.close()


def get_all_products():
    """Возвращает все записи из таблицы Products."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, price, image_url FROM Products")
    products = cursor.fetchall()
    conn.close()
    return products


def add_user(username, email, age):
    """Добавляет нового пользователя в таблицу Users."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                       (username, email, age, 1000))
        conn.commit()
    except sqlite3.IntegrityError as e:
        conn.close()
        if "UNIQUE constraint failed: Users.email" in str(e):
            raise ValueError("Пользователь с таким email уже существует")
        else:
            raise ValueError("Ошибка добавления пользователя.")
    conn.close()


def is_included(username):
    """Проверяет, существует ли пользователь с данным именем в таблице Users."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM Users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return bool(result)


if __name__ == '__main__':
    initiate_db()