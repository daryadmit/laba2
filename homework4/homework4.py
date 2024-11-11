import random

def find_multiples():
    numbers = [random.randint(0, 200) for _ in range(10)]
    print("Сгенерированные числа:", numbers)

    while True:
        try:
            x = int(input("Введите целое число X: "))
            break
        except ValueError:
            print("Ошибка! Необходимо ввести целое число.")

    multiples = list(filter(lambda num: num % x == 0, numbers))

    if multiples:
        print(f"Числа кратные {x}: {multiples}")
    else:
        print(f"Нет чисел кратных {x}.")

find_multiples()