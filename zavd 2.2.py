namee = input("Як тебе звати? ")
agee = int(input("Скільки тобі років? "))

def info_about_user(name, age):
    try:
        if age < 0:
            raise ValueError("Ти шо довбень, тобі не може бути менше 0 років")
        elif age > 130:
            raise ValueError("Ти шо довбень, тобі не може бути більше 130 років, чи ти не людина.....")

        return print(f"Привіт, {name}! Твій вік — {age}")

    except ValueError as e:
        return print(e)

info = info_about_user(namee, agee)
print(info)