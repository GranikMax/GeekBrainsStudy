"""Программа запрашивает у пользователя строку чисел, разделенных пробелом.
 При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
  Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
  Но если вместо числа вводится специальный символ, выполнение программы завершается.
  Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
   этих чисел к полученной ранее сумме и после этого завершить программу."""

def sum ():
    sum_p = 0
    x = False
    while x == False:
        number = input('Введите числа через пробел или "Q" для выхода: ').split()

        y = 0
        for z in range(len(number)):
            if number[z] == 'q' or number[z] == 'Q':
                x = True
                break
            else:
                y = y + int(number[z])
        sum_p = sum_p + y
        print(f'Сумма {sum_p}')
    print(f'Окончательная сумма {sum_p}')


sum()