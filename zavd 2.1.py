namee = input("Як тебе звати? ")
agee = int(input("Скільки тобі років? "))

def info_of_user(name, age):
    if age < 0:
        raise ValueError("Ти шо довбень, тобі не може бути менше 0 років")
    elif age > 130:
        raise ValueError("Ти шо довбень, тобі не може бути більше 130 років, чи ти не людина.....")

    return print(f"Привіт, {name}! Твій вік — {age}")

try:
    info = info_of_user(namee, agee)
    print(info)
except ValueError as e:
    print(e)