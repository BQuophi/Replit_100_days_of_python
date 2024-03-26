print('TIP CALCULATOR')
print()

bill = float(input('How much did you spend? '))
print()

tip = int(input('What percentage do you want to tip? '))
print()

people = int(input('How many people in your group? '))
print()

tip_amount = bill * (tip / 100)
print(tip_amount)
total_bill = bill + tip_amount

final_bill = total_bill / people
print('You each owe $' + str(final_bill))