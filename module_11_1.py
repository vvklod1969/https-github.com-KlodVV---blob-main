import requests
import numpy as np
from PIL import Image, ImageFilter

print(f'Requests - библиотека упростила выполнение HTTP-запросов, '
      f'дала возможность легко получать данные с веб-сайтов путем использования '
      f'методов "get" и "json", для запроса и обработки данных')
print()
print(f'Демонстрация возможностей библиотеки requests')
""" в примере выполняем GET-запрос к API, проверяем, успешно ли он выполнен (статус 200), 
и преобразуем полученные JSON-данные в Python-объект, чтобы вывести их в консоль. """
print()
print()
# Выполнение GET-запроса
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Проверка статуса ответа
if response.status_code == 200:
    # Преобразование JSON-данных в Python-объект и вывод в консоль
    data = response.json()
    print(data)
else:
    print('Ошибка при запросе данных')

print()

print(f'Numpy - данная библиотека позволяет работать с  массивами и выполнять '
      f'математические операции (вычисление суммы, среднего значения, квадратов элементов и др.'
      f'Использовал методы "array", "sum", "mean" и "square"')
print()
print(f'Демонстрация возможностей библиотеки NUMPY')

# Создание массива
array = np.array([1, 2, 3, 4, 5])

# Сумма элементов массива
sum_array = np.sum(array)
print(f"Сумма: {sum_array}")

# Среднее значение элементов массива
mean_array = np.mean(array)
print(f"Среднее: {mean_array}")

# Возведение в квадрат каждого элемента массива
squared_array = np.square(array)
print(f"Квадраты: {squared_array}")
print()
print()
print(f'Библиотека "Pillow" позволяет обрабатывать изображения, включая изменение '
      f'их размера и применение эффектов с использованием методов'
      f' "open", "resize", "filter" и "save", для манипуляций с изображениями '
      f'с последующем сохранением их в различных форматах.')
print()
print(f'Демонстрация возможностей библиотеки Pillow (ранее известная как PIL)')


# Открытие изображения
image = Image.open('Леопард.jpg')

# Изменение размера
resized_image = image.resize((450, 450))

# Применение эффекта
blurred_image = resized_image.filter(ImageFilter.BLUR)

# Сохранение изображения в другом формате
blurred_image.save('Леопард2.png')

print(f'Изображение "Леопард" обработано и сохранено в файл "Леопард2"')

