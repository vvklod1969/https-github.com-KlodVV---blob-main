import sqlite3

DATABASE_NAME = 'products.db'


def initiate_db():
    """Создает таблицу Products, если она еще не создана."""
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
    conn.commit()
    conn.close()


def get_all_products():
    """Возвращает все записи из таблицы Products."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, price, image_url FROM Products")
    products = cursor.fetchall()
    conn.close()
    return products


if __name__ == '__main__':
    initiate_db()  # Создаём таблицу если её не было
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Проверка на наличие записей в таблице
    cursor.execute("SELECT COUNT(*) FROM Products")
    count = cursor.fetchone()[0]

    if count == 0:
        products = {
            "product1": {
                "name": "Product 1",
                "description": "Ускоряет сжигание жиров и предотвращает их накопление в организме,\nвыводит токсины, снижает уровень холестерина.\nНа 80% выгоднее зарубежного аналога",
                "price": 931,
                "image_url": "https://shop.evalar.ru/upload/iblock/424/ub850grpfux6l7r2wtwhmshpe89xx7oo.png"
            },
            "product2": {
                "name": "Product 2",
                "description": "Морской хитозан из панцирей крабов для похудения, детокса, контроля уровня холестерина",
                "price": 859,
                "image_url": "https://shop.evalar.ru/upload/iblock/843/x95zvl4vqjjioi8ql0crhkxwcz3paddl.png"
            },
            "product3": {
                "name": "Product 3",
                "description": "Устраняет сразу несколько причин лишнего веса, способствует снижению аппетита, активизирует сжигание жиров",
                "price": 519,
                "image_url": "https://shop.evalar.ru/upload/iblock/c51/mam75h042zsrfk7wgmdjhyhtzrugrzua.png"
            },
            "product4": {
                "name": "Product 4",
                "description": "Cпособствует снижению аппетита, помогает соблюдать диету и контролировать вес",
                "price": 289,
                "image_url": "https://shop.evalar.ru/upload/iblock/b70/h3hmu0dit5fqtlghhqcgurb8kwinqtkg.png"
            }
        }
        # Добавление записей, если таблица пуста
        products_to_add = [(data["name"], data["description"], data["price"], data["image_url"]) for key, data in
                           products.items()]
        cursor.executemany("INSERT INTO Products (title, description, price, image_url) VALUES (?, ?, ?, ?)",
                           products_to_add)
        conn.commit()
        print("База данных инициализирована и наполнена данными.")
    else:
        print("База данных уже инициализирована, данные не добавляются")
    conn.close()