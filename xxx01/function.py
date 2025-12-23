def greet_user(name):
    print(f'Hi {name}') 

greet_user('Max')

def square(number):
    return number * number

square(3)

def json_body(name, profession):
    json = {
        "name": name,
         "profession": profession
    }
    return json

json_body("Josh", "CFO")
