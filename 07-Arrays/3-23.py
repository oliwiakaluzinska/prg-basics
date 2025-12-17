text = "An apple a day keeps the doctor away"

words = text.split()
print(len(words))

words.sort(key=len, reverse=True)
print(words)

words.sort()
print(words)