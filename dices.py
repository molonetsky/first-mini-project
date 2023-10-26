import random


def dices():
    while True:
        print(
            'Выберите действие: \n' + '1.Бросить Кости \n' + '2.Выйти из игры \n'
            + '3.Бросать кости пока не выпадет сумма \n' + '4.Бросать кости пока не выпадет дубль \n')
        user = input()
        if user == '2':
            print('Игра окончена')
            break
        elif user == '1':
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(f'Первая кость выпала на {dice1}, Вторая на {dice2}, в сумме выпало {dice1 + dice2} \n')
            continue
        elif user == '3':
            user2 = int(input('Выберете желаемую сумму от 2 до 12 \n'))
            count = 0
            while True:
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                dice_result = dice1 + dice2
                count += 1
                print(dice_result)
                if dice_result == user2:
                    print(f' Выпало! с {count} попытки, Результат {dice_result}')
                    break
                else:
                    continue
        elif user == '4':
            count = 0
            while True:
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                count += 1
                print(dice1, dice2)
                if dice1 == dice2:
                    print(f' Выпало! с {count} попытки, Результат {dice1, dice2}')
                    break
                else:
                    continue
        else:
            continue


dices()
