from math import sqrt


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """Выводит значение."""
    root = calculate_square_root(your_number)
    if your_number > 0:
        print('Мы вычислили квадратный корень из введённого '
              f'вами числа. Это будет: {root}')
        return '0'
    return '1'


print('Добро пожаловать в самую лучшую программу для вычисления '
      'квадратного корня из заданного числа')
calc(25.5)
