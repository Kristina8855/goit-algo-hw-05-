import re
from typing import Callable
def caching_fibonacci():
    cache = {}  # Створення кешу для зберігання обчислених значень

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            result = n
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)

        cache[n] = result
        return result

    return fibonacci

fibonacci = caching_fibonacci()

print(fibonacci(5))
print(fibonacci(10))



# Завдання 2
import re
from typing import Callable

import re
from typing import Callable

def generator_numbers(text: str):
    """
    Функція, яка аналізує текст і повертає генератор дійсних чисел у тексті.
    """
    pattern = r"\b\d+\.\d+\b"  # Регулярний вираз для знаходження дійсних чисел
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    """
    Обчислює загальну суму чисел у тексті, використовуючи заданий генератор.
    """
    return sum(func(text))
def main():
    text = "Income: 100.50, Expenses: 50.25, Profit: 50.25"
    total_profit = sum_profit(text, generator_numbers)
    print("Total profit:", total_profit)

if __name__ == "__main__":
    main()

#3
from pathlib import Path

def parse_input(user_input):
    tokens = user_input.split()
    command = tokens[0].lower()  # перший елемент - команда
    args = tokens[1:]  # решта елементів - аргументи
    return command, args

contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            print(f"Input error: {e}")
    return wrapper

@input_error
def add_contact(name, phone_number):
    contacts[name] = phone_number
    print("Contact added.")

@input_error
def change_contact(name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        print("Contact updated.")
    else:
        print("Contact not found.")

@input_error
def show_phone(name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

@input_error
def show_all():
    for name, phone_number in contacts.items():
        print(f"{name}: {phone_number}")

def main():
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "add":
            add_contact(*args)
        elif command == "change":
            change_contact(*args)
        elif command == "phone":
            show_phone(*args)
        elif command == "all":
            show_all()
        elif command == "close" or command == "exit":
            print("Good bye!")
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()

