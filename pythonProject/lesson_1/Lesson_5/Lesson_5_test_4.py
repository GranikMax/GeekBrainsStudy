'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
enc_file = []
with open('test_4.txt', 'r', encoding='UTF-8') as f_o:
    #content = f_o.read().split('\n')
    for i in f_o:
        i = i.split(' ', 1)
        enc_file.append(rus[i[0]] + '  ' + i[1])
    print(enc_file)

with open('test_4_new.txt', 'w') as f_o_2:
    f_o_2.writelines(enc_file)