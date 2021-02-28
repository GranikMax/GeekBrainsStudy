'''Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''
string = 0
with open("test_2.txt") as f_o:
    for line in f_o.readlines():
        words = len(line.split(' '))
        string = string + 1
        print(f' {words} Слов в строке')
    print(f'{string} Строк')