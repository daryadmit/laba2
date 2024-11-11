def get_number():
    odd_numbers = []
    for number in range(30):
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers

odd_numbers = get_number()

if len(odd_numbers) > 0:
    print(f"Первое нечетное число: {odd_numbers[0]}")
else:
    print("Нет нечетных чисел.")

if len(odd_numbers) >= 5:
    print(f"Пятое нечетное число: {odd_numbers[4]}")
else:
    print("Нет нечетных чисел.")

if len(odd_numbers) > 0:
    print(f"Последнее нечетное число: {odd_numbers[-1]}")
else:
    print("Нет нечетных чисел.")