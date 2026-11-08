import re
from typing import Callable


#TASK 1

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0: return 0
        elif n == 1: return 1
        elif n == cache: return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610



#TASK 2

def generator_numbers(text: str):
    matches = re.finditer(r"\d+\.\d+", text)

    for match in matches:
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

