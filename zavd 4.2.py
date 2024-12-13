numbers = []
howmuuch = int(input("Введіть скільки хочете ввести чисел "))

def obrobka(number):
    for _ in range(howmuuch):
        try:
            czysla = int(input("Ввведіть БУДЬ ЛАСКА тільки додатні числа(більші нуля) "))
            if czysla < 0:
                raise ValueError

            numbers.append(czysla)

        except ValueError:
            print("НУ Я Ж ПРОСИВ ТІЛЬКИ ДОДАТНІ ЧИСЛА, АЛОООООО")
            break

    return sum(number)

if numbers:
    sumaa = obrobka(numbers)
    print(f"Сума: {sumaa}")