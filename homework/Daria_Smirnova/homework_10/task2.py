def repeat_me(func):
    def wrapper(text, count):
        for _ in range(count):
            func(text)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
