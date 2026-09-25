### Калькулятор и конвертер величин на языке Python.

# Использование
`python -m toolkit COMMAND ARGUMENTS`
# Команды
+ `calc EXPRESSION` - вычисление выражения
+ `convert VALUE --from UNIT --to UNIT` - конвертировать единицу измерения
+ `--help` - вывести эту справку
# Примеры
+ `python -m toolkit calc "2 + 3 * 4`
+ `python -m toolkit convert 100 --from cm --to m`
+ `python -m toolkit --help`
# Поддерживаемые единицы измерения
+ Длина
    + mm **(миллиметр)**
    + cm **(сантиметр)**
    + m  **(метр)**
    + km **(километр)**
+ Масса
    + g  **(грамм)**
    + kg **(килограмм)**
+ Температура
    + c **(Цельсий)**
    + f **(Фаренгейт)**
    + k **(Кельвин)**
