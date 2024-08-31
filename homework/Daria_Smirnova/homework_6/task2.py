for item in range(1, 101):
    if item % 3 == 0 and item % 5 == 0:
        print("FuzzBuzz")
    elif item % 5 == 0:
        print("Buzz")
    elif item % 3 == 0:
        print("Fuzz")
    else:
        print(item)
