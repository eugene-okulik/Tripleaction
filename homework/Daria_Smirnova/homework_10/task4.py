PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

words = PRICE_LIST.split()
# print(words)
price_dict = {words[i]: int(words[i + 1][:-1]) for i in range(0, len(words), 2)}
print(price_dict)
