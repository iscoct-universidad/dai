import re

chain = input("Introduzca la cadena: ")
words = chain.split(" ")

print("Words")

for i in range(len(words)):
    if (re.search("[A-Z]{1}", words[i])):
        print(words[i])