text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
words = text.split()

for word in words:
    if (word[-1] == ","
            or word[-1] == "."):
        modified_word = word[:-1] + "ing" + word[-1]
    else:
        modified_word = word + "ing"
    print(modified_word, end=" ")
