""" 1. Создать список и заполнить его элементами различных типов данных.
 Реализовать скрипт проверки типа данных каждого элемента.
  Использовать функцию type() для проверки типа.
   Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""
my_int = 5
my_float = 1.2
my_str = "Таки здравствуй мир"
my_list = ['a', '1']
my_tuple = ('b', '2')
my_dict = {'город': 'Петухово', 'страна': 'Россия'}

all_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in all_list:
    print(f'{i} is {type(i)}')