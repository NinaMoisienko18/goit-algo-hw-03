import random

def get_numbers_ticket(min, max, quantity):
        list_numbers = random.sample(range(min, max), quantity)
        list_numbers = sorted(list_numbers)
        return list_numbers



while True:

    min = int(input("Мінімальний номер білету >= 1: "))
    max = int(input("Максимальний номер білету <= 1000: "))

    if min >= 1 and max <= 1000:
        quantity = int(input("Кількість унікальних чисел для лотерейного квитка: "))
        lottery_numbers = get_numbers_ticket(min, max, quantity)
        print("Ваші лотерейні білети:", lottery_numbers)
        break
    else:
        not_valid_range = input("На жаль, введені числа не відповідають заданому діапазону.Спробуєте ще раз?"
                                "\n1.Так\n2.Ні\n>>>Відповідь користувача: ")

        if not_valid_range == "2":
            break