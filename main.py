def sum_nums(a: int, b: int) -> int:
    return a + b


def main():
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    operator = input('Введите операцию: ')

    if operator == '+':
        print(sum_nums(num1, num2))


if __name__ == '__main__':
    main()
