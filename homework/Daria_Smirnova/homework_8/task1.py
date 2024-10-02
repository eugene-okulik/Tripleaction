import random

salary = int(input("Напечатайте вашу зарплату: "))
bonus = random.choice([True, False])
if bonus:
    random_bonus = random.randint(100, 5000)  # Генерируем случайный бонус от 100 до 5000
    total_salary = salary + random_bonus
else:
    total_salary = salary

print(f"{salary},{bonus} -'${total_salary}'")
