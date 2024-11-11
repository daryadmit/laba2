from datetime import datetime

def calculate_age():

    while True:
        try:
            bd_str = input("Введите дату рождения. В формате записи дд/мм/гггг: ")
            birth_date = datetime.strptime(bd_str, "%d/%m/%Y").date()

            if birth_date > datetime.now().date():
                print("Неверно введена дата, данное число ещё не наступило.")
                continue

            break
        except ValueError:
            print("Неверный формат даты, введите дату в формате дд/мм/гггг.")

    today = datetime.now().date()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    print(f"Возраст: {age} лет.")

if __name__ == "__main__":
    calculate_age()
