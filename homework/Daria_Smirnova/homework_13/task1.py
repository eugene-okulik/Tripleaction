import os
from datetime import datetime, timedelta
import calendar

base_path = os.path.dirname(__file__)
print(base_path)

homework_path = os.path.dirname(os.path.dirname(base_path))
print(homework_path)

new_path = os.path.join(homework_path, "eugene_okulik", 'hw_13', "data.txt")
print(new_path)

list_of_dates = []
with open(new_path) as new_file:
    lines = new_file.readlines()
for line in lines:
    date_time_part = line.split(" ")[1] + " " + line.split(" ")[2]
    list_of_dates.append(date_time_part)
print(list_of_dates)

first_date = list_of_dates[0]
date_obj1 = datetime.strptime(first_date, "%Y-%m-%d %H:%M:%S.%f")
print(date_obj1 + timedelta(days=7))

second_date = list_of_dates[1]
date_obj2 = datetime.strptime(second_date, "%Y-%m-%d %H:%M:%S.%f")
print(calendar.day_name[date_obj2.weekday()])

third_date = list_of_dates[-1]
date_obj3 = datetime.strptime(third_date, "%Y-%m-%d %H:%M:%S.%f")
now = datetime.now()
a = now - date_obj3
print(a.days)
