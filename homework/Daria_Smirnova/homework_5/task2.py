result1 = "результат операции: 42"
result2 = "результат операции: 514"
result3 = "результат работы программы: 9"

b = result1.index("4")
a = int(result1[b:])

c = result2.index("5")
d = int(result2[c:])

e = result3.index("9")
f = int(result3[e])
print(a + 10)
print(d + 10)
print(f + 10)
