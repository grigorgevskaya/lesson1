
def main():

    users_age = int(input("age:"))

    if users_age < 7:
        print("Ты ходишь в детский сад")
    elif 7 >= users_age < 18:
        print("Ты ходишь в школу")

    elif 18 >= users_age < 24:
        print("Ты учишься в ВУЗе")

    elif 24 >= users_age < 65:
        print("Ты работаешь")
    else:
        print("Ты на пенсии")


if __name__ == "__main__":
    main()
