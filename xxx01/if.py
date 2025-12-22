winter = True #input('Do you like winter? ')
has_high_income = True
has_high_credit = True
temperature = 30

if winter == "yes": 
    print("YEY. You like winter")
else: 
    print("You don't like winter")

if has_high_income and has_high_credit:
    print("Eligible for loan")

if not has_high_income:
    print("Not eligible for loan")

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
