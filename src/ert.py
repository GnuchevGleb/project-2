import pandas as pd

# создаём DataFrame из списка словарей
data = [
    {"Book": "Звук и Ярость", "Year": 1929, "Author": "Уильям Фолкнер"},
    {"Book": "Над пропастью во ржи", "Year": 1951, "Author": "Дж. Д. Сэлинджер"},
    {"Book": "Уловка-22", "Year": 1961, "Author": "Джозеф Хеллер"},
]

# создаём DataFrame
df = pd.DataFrame(data)

# выводим DataFrame на экран
print(df)
