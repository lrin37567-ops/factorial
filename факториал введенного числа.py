import math

def get_positive_integer():
    while True:
        user_input = input("Введите положительное целое число: ").strip()
        try:
            number = int(user_input)
            if number < 0:
                print("Ошибка: число должно быть положительным.")
            else:
                return number
        except ValueError:
            print("Ошибка: введите корректное целое число.")

def calculate_factorial(n):
    return math.factorial(n)

def main():
    n = get_positive_integer()
    result = calculate_factorial(n)
    print(f"Факториал числа {n} равен {result}")

if __name__ == "__main__":
    main()
