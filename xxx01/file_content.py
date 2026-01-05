import datetime
import os

items = os.listdir('c:/temp') 
for item in items:
    print(item)

with open('c:/temp/json.json', 'r', encoding='utf-8') as file:
    content = file.read()
    # print(content)

year = datetime.datetime.now().strftime("%Y-%m-%d")
for item in os.listdir('c:/temp'):
    if item.endswith('.json') and item.startswith(year):
        print("Log: ", item)
        with open(f'c:/temp/{item}', 'r', encoding='utf-8') as file:
            get_logs = file.read()

# print(get_logs)
