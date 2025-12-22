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

i = 1 

while i <= 5:
    print(i)
    print( '*' * i)
    i = i + 1

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guesss: '))
    guess_count += 1
    if guess == secret_number:
        print('You won')
        break
else:
    print('Sorry you failed') 
