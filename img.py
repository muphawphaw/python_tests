from urllib.request import urlretrieve

link = input("User input : ")
file_name = input("Filename : ")

urlretrieve(link,"image/"+ file_name + ".png")