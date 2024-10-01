import sys

sys.set_int_max_str_digits(0)


def progression(limit=1000):
    a, b = 0, 1
    count = 1
    while True:
        yield a
        a, b = b, a + b


count = 1
for number in progression(5):
    if count == 5:
        print(number)
        break
    count += 1
for number in progression(200):
    if count == 200:
        print(number)
        break
    count += 1
for number in progression(1000):
    if count == 1000:
        print(number)
        break
    count += 1
for number in progression(100000):
    if count == 100000:
        print(number)
        break
    count += 1
