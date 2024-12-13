try:
    name = input("Як тебе звати? ")
    age = int(input("Скільки тобі років? "))
    if age < 0:
        raise ValueError
    elif age > 130:
        raise ZeroDivisionError
    else:
        print(f"Привіт, {name}! Твій вік — {age}")
except ValueError:
    print("Ти шо довбень, тобі не може бути менше 0 років")
except ZeroDivisionError:
    print("Ти шо довбень, тобі не може бути більше 130 років, чи ти не людина.....")