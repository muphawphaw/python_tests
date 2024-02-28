words = ["apple","orange","kiwi","mango","pineapple"]

from random import randint
def random_sentence(w):
    random_index = randint(0,len(words)-1)
    return f"{words[random_index]}{w}"

with open('./generator.txt') as file:
    paragraph = file.read()
    paragraph_list=paragraph.split()
    sentence_list=list(map(random_sentence,paragraph_list))
    para_count = int(input("Count: "))

    for count in range(para_count):
        with open('./generator_1.txt','a') as para_c :
            para_c.write("-".join(sentence_list) + "\n\n")