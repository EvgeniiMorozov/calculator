def sum_nums(a: int, b: int) -> int:
    return a + b


def sub_nums(a, b):
    return a - b


def mul_nums(a, b):
    return a * b


def div_nums(a, b):
    return a / b


def main():
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    operator = input('Введите операцию: ')

    if operator == '+':
        print(sum_nums(num1, num2))
    elif operator == '-':
        print(sum_nums(num1, num2))
    elif operator == '*':
        print(mul_nums(num1, num1))
    elif operator == '/':
        print(div_nums(num1, num2))


if __name__ == '__main__':
    main()
