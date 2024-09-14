def calc(result):
    number = int(result[result.index(':') + 1:]) + 10
    return number


results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]
for result in results:
    print(calc(result))
