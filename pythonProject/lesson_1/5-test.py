viruch = int(input("Ведите выручку: "))
lose = int (input("Введите издержки: "))
if viruch > lose:
    profit = viruch-lose
    rent = profit/viruch
    print (f"Прибыль: {profit}")
    worker = int(input("Введите колтчество работников: "))
    print(f"{profit/worker} доход на одного рабочего")
elif viruch==lose:
    print("Вообще не работал")
else:
   print ("Лучше бы не брался за работу")

