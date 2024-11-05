def add_everything_up(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b

    elif isinstance(a, str) or isinstance(b, str):
        if type(a) is not type(b):
            return str(a) + str(b)
        else:
            return a + b


    raise TypeError("Unsupported types")

print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))      # яблоко4215
print(add_everything_up(123.456, 7))           # 130.456