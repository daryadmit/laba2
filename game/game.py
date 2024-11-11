print('Добро пожаловать в игру "камень, ножницы, бумага"! Вы будете играть против компьютера.')
import random

def get_user_choice():
    user_input = input("Введите 'камень', или 'ножницы', или 'бумага': ").lower()
    while user_input not in ['камень', 'ножницы', 'бумага']:
        print("Ошибка ввода. Введите 'камень', или 'ножницы', или 'бумага'.")
        user_input = input("Введите 'камень', или 'ножницы', или 'бумага': ").lower()
    return user_input

def get_computer_choice():
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "Ничья!"
    elif (user == 'камень' and computer == 'ножницы') or \
         (user == 'ножницы' and computer == 'бумага') or \
         (user == 'бумага' and computer == 'камень'):
        return "Поздравляю! Вы победили!"
    else:
        return "Компьютер победил!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Ваш выбор: {user_choice}")
    print(f"Выбор компьютера: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()