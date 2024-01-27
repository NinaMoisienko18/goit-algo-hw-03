import random

def get_numbers_ticket(min, max, quantity):
    list_numbers = random.sample(range(min, max), quantity)
    list_numbers = sorted(list_numbers)
    return list_numbers


lottery_numbers = get_numbers_ticket(min=1, max=50, quantity=5)
print("Ваші лотерейні числа:", lottery_numbers)