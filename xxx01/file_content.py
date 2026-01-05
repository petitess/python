import os

items = os.listdir('c:/temp') 
for item in items:
    print(item)

with open('c:/temp/json.json', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
