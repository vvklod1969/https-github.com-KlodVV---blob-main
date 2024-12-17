import asyncio

async def start_strongman(name, power):
    """ Показывает участие силача в соревнованиях по поднятию шаров.
    Args:
        name (str): Имя силача.
        power (int): Подъёмная мощность силача (чем выше, тем быстрее).
    """
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):  # определяем цикл из 5 шаров
        await asyncio.sleep(1 / power)  # определяем задержку которая обратно пропорциональна силе
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    """
    Запускает соревнования между тремя силачами.
    """
    # Создаем задачи для каждого силача
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))

    # Ожидаем завершения всех задач
    await task1
    await task2
    await task3

if __name__ == "__main__":
    asyncio.run(start_tournament())