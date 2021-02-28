'''Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.'''

f_o = open('test.txt', 'w')
line = input('Введите текст: \n')
while line:
    f_o.writelines(line)
    line = input('Введите текст: \n')
    if not line:
        break

f_o.close()
f_o = open('test.txt', 'r')
res = f_o.readlines()
print(res)
f_o.close()