text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')
words = text.split()

for w in words:
    if (w[-1] == ","
            or w[-1] == "."):
        mod_word = w[:-1] + "ing" + w[-1]
    else:
        mod_word = w + "ing"
    print(mod_word, end=" ")
