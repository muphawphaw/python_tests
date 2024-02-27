person= {}

while True:
    name = input("Enter name : ")
    age = input ("Enter age : ")
    person[name] = age


    another = input("another y/n : ")
    if another == "y":
        continue
    else : 
        break

age = list(person.values())
name =list(person.keys())

for n,a in name,age:
    print(f"{n} is {a} years old")

