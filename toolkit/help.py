def print_help():
    print("""Использование: python -m toolkit COMMAND ARGUMENTS
    Команды:\n
    calc EXPRESSION - вычисление выражения 
    convert VALUE --from UNIT --to UNIT - конвертировать единицу измерения
    --help - вывести эту справку\n
    Примеры:\n
    python -m toolkit calc "2 + 3 * 4" 
    python -m toolkit convert 100 --from cm --to m\n
    Поддерживаемые единицы измерения:\n
    Температура = [k, c, f]
    Длина = [mm, cm, m, km]
    Масса = [g, kg]""")
