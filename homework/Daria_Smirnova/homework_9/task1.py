import datetime

my_date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
human_date = python_date.strftime("%B")
customer_date = python_date.strftime("%d.%m.%Y, %H:%M")
# 15.01.2023, 12:05
print(human_date)
print(customer_date)
