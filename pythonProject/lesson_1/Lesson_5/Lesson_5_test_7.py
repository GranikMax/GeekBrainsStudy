'''
оздать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
'''

from json import dumps


#SRC_FILENAME = "task7.txt"
#DST_FILENAME = "task7.json"

results = [{}, {}]


with open('test_7.txt', 'r', encoding='UTF-8') as f_o:
    lines = f_o.readlines()
    for line in lines:
        name, _, proceeds, expenses = line.split()
        results[0][name] = int(proceeds) - int(expenses)
    results[1]['Средний доход'] = round(
        sum(
            profit for _, profit in results[0].items() if profit > 0
        ) / len(results[0])
    )
with open('Test_7.json', "w", encoding='utf-8') as f_o:
        f_o.write(dumps(results))

print (results)