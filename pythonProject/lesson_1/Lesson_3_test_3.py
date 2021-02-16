"""Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов."""

def func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {func(int(input("Введите число: ")),int(input("Введите второе число: ")),int(input("Введите третье число: ")))}')