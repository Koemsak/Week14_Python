def splitByspace(text):
    words = []
    currentWord = ""
    for i in text:
        if i == " ":
            words.append(currentWord)
            currentWord = ""
        else:
            currentWord += i
    if len(currentWord) > 0:
        words.append(currentWord)
    return words
word = input()
print(splitByspace(word))