first = int(input("Print number"))
second = int(input("Print other number"))


def something(func):
    def wrapper(first, second):
        if first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        elif second > first:
            operation = "/"
        if first < 0 or second < 0:
            operation = "*"
        return func(first, second, operation)

    return wrapper


@something
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second
    elif operation == "*":
        return first * second


result = calc(first, second)
print(result)
