
words = ["apple","orange","kiwi","lemon","banana"]
from random import randint
def random_generator(word):
    random_index = randint(0,len(words)-1)
    return f"{words[random_index]} {word}"

with open("./test.txt")as read_file:
    para = read_file.read()
    wordList= para.split()
    sentenceList = list(map(random_generator,wordList))

    paraCount = int(input("Enter your para count: "))
    for count in range(paraCount):
        with open("./write.txt","a")as write_file:
            write_file.write("".join(sentenceList)+"\n\n")