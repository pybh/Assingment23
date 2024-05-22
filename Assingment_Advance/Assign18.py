file = open("python.txt", "r")
j=""
for m in file:
    j+=m
l = j.split()
b = []
length = 0
for word in l:
    word = word.strip()
    word_length = len(word)
    if word_length > length:
        b = [word]
        length = word_length
print(b)
file.close()