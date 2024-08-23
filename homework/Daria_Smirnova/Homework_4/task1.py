my_dict = {
    'tuple': (1991, 1992, 1993, 1994, 1995),
    'list': ["Maria", "Daria", "Igor", "Sasha", "Dima"],
    'dict': {'one': 'value1', 'two': 'value2', 'three': 'value3', 'four': 'value4', 'five': 'value5'},
    "set": {1, 2, 3, 4, 5}
}
print(my_dict["tuple"][-1])

my_dict["list"].append("Vasy")
my_dict["list"].pop(1)

del my_dict["dict"]["one"]
my_dict ["dict"][('i am a tuple',)] = 123456



my_dict["set"].add(6)
my_dict["set"].remove(1)
print(my_dict)
