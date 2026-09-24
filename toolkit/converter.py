metric = ["mm", "cm", "m", "km"]
mass = ["g", "kg"]
temperature = ["c", "f", "k"]
types = [metric, mass, temperature]

to_base = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "g": 1, "kg": 1000}


def is_compatible(unit_from, unit_to):
    if unit_from not in (metric + mass + temperature):
        raise ValueError(f"Неизвестная единица измерения: {unit_from}")
    if unit_to not in (metric + mass + temperature):
        raise ValueError(f"Неизвестная единица измерения: {unit_to}")
    return any(unit_from in list and unit_to in list for list in types)


def convert_temperature(value, unit_from, unit_to):
    value = float(value)
    if unit_from == "c":
        celsius = value
    elif unit_from == "f":
        celsius = (value - 32) * 5 / 9
    elif unit_from == "k":
        celsius = value - 273.15
    else:
        raise ValueError(f"Неизвестная единица температуры: {unit_from}")
    if celsius <= -273.15:
        raise ValueError("Температура ниже абсолютного нуля не существует")

    if unit_to == "c":
        return celsius
    elif unit_to == "f":
        return celsius * 9 / 5 + 32
    elif unit_to == "k":
        return celsius + 273.15
    else:
        raise ValueError(f"Неизвестная единица температуры: {unit_to}")


def convert(value, unit_from, unit_to):
    value = float(value)
    if not is_compatible(unit_from, unit_to):
        raise ValueError(f"Нельзя перевести {unit_from} в {unit_to}")
    if unit_from in temperature and unit_to in temperature:
        return convert_temperature(value, unit_from, unit_to)
    return (value * to_base[unit_from]) / to_base[unit_to]
