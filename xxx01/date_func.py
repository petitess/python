import datetime
from datetime import timedelta

now = datetime.datetime.now()
print(now) 
print(now.strftime("%Y-%m-%d-%H-%M")) 

a = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(now.weekday()) 
print(a[now.weekday()])

this = datetime.datetime(2018, 6, 1)
print(this) 

enddate = now + timedelta(days=10)
print(enddate) 

before = now + timedelta(days=-10)
print(before)

print("Write a date in this format: yyyy-mm-dd")
user_input = input().strip()
today = now.today()

try:
    input_date = now.strptime(user_input, "%Y-%m-%d")
    days_passed = today - input_date
    print(f"{days_passed.days} days passed")
except ValueError:
    # This is similar to DateTime.TryParse failing
    pass
