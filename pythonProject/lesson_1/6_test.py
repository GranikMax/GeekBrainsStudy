a = float(input("Начало: "))
b = float(input("Конец: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day =day + 1
print(f"{day} День")