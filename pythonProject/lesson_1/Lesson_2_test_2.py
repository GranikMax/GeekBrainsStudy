"""Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input()."""


n = int(input("Введите количество элементов в списке "))
l = []
i = 0
x = 0
while i < n:
    l.append(input("Введите следующее значение списка "))
    i += 1
for y in range(int(len(l)/2)):
        l[x], l[x + 1] = l [x + 1], l[x]
        x += 2
print(l)