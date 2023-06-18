from collections import defaultdict

# Создаем словарь для хранения количества событий NOK по минутам
events_per_minute = defaultdict(int)

# Открываем файл events.log для чтения
with open('events.log', 'r') as file:
    for line in file:
        # Разделяем строку по пробелам
        parts = line.split()

        # Получаем дату и время из первых двух элементов
        date = parts[0][1:]
        time = parts[1]

        # Получаем минуту из времени
        minute = time.split(':')[1]

        # Если событие - NOK, увеличиваем счетчик для данной минуты
        if parts[3] == 'NOK':
            events_per_minute[(date, minute)] += 1

# Выводим результаты
for key, value in events_per_minute.items():
    print(f"За {key[0]} в {key[1]} минуту было {value} событий NOK")
