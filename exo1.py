
chaine = input("Entrez une chaine de caractères: ")

majuscules = 0
minuscules = 0

for caractere in chaine:
    if caractere.isupper():
        majuscules += 1
    elif caractere.islower():
        minuscules += 1

print("Nombre de majuscules:", majuscules)
print("Nombre de minuscules:", minuscules)