type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())
cost = 0

if type_of_flowers == "Roses":
    cost = 5 * number_of_flowers
    if number_of_flowers > 80:
        cost -= cost * 0.10

elif type_of_flowers == "Dahlias":
    cost = 3.80 * number_of_flowers
    if number_of_flowers > 90:
        cost -= cost * 0.15

elif type_of_flowers == "Tulips":
    cost = 2.80 * number_of_flowers
    if number_of_flowers > 80:
        cost -= cost * 0.15

elif type_of_flowers == "Narcissus":
    cost = 3 * number_of_flowers
    if number_of_flowers < 120:
        cost += cost * 0.15

elif type_of_flowers == "Gladiolus":
    cost = 2.50 * number_of_flowers
    if number_of_flowers < 80:
        cost += cost * 0.20

diff = abs(budget - cost)

if budget >= cost:
    print(f'Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')

