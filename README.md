# Тестовое задание №1

Доктор принимает с 9 утра до 9 вечера.
Часть времени у него занята: приемы, обед, уборка кабинета.
busy = [
{'start' : '10:30',
'stop' : '10:50'
},
{'start' : '18:40',
'stop' : '18:50'
},
{'start' : '14:40',
'stop' : '15:50'
},
{'start' : '16:40',
'stop' : '17:20'
},
{'start' : '20:05',
'stop' : '20:20'
}
]

Требуется сформировать список свободных окон по 30 минут.

1. "from datetime import datetime, timedelta" Импортируем нужные библиотеки для запуска!
2. Функция для создания списка из элементов словаря и сортировки элементов в списке.
	Добавляем начало и конец рабочего дня в начало списка и конец.
3. Функция с условием проверки элементов на вхождение во временной отрезок.
	Добавление элементов в словарь в цикле,а после в заранее созданный список для словарей.
4. Через цикл "for" обращаемся к функции 3 и получаем список из словарей со свободным временем врача
	поделенным на равные отрезки времени по 30 минут.

# Тестовое задание №2

Написать функцию которая будет сравнивать элементы строки из списка и выводить ключ самого большого элемента (слово по середине).
    1. Сравнивать по первому значению
    2. Если первые элементы равны то сравнить по третьему
    3. Если на вход получить список с n количеством списков... итоговый вариант
