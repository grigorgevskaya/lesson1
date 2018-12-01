
def main():
    first_str = input("Введите первую строку: ")
    second_str = input("Введите вторую строку: ")

    if type(first_str) != str or type(second_str) != str:
        return 0
    elif first_str == second_str:
        return 1
    elif first_str > second_str:
        return 2
    elif second_str == 'learn':
        return 3
    elif first_str < second_str:
        return 4


if __name__ == "__main__":
    print(main())
