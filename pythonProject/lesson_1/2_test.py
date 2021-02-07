time_sec = int(input("Введите время в секундах: "))
hours = time_sec // 3600
ostatok = time_sec % 3600
min = ostatok // 60
sec = ostatok % 60

print(f"{hours}:{min}:{sec} ")
