print("bienvenue dans mon quiz !")
jeu = input ("voulez vous jouez ? ")

if jeu.lower() != "oui":
    quit()
print ("ok c'est parti !")
score = 0

answer = input("Quel est la marque qui utilise AMG pour définir un modéle ")
if answer.lower() == "mercedes":
    print("Parfait !")
    score += 1
else:
    print("Mauvaise réponse")

answer = input("Quel est la marque qui à pour symbole 4 anneaux ")
if answer.lower() == "audi":
    print("Super !")
    score += 1
else:
    print("réflechis encore un peu")

continuer = input("voulez vous continuez de jouer ? ")
if continuer.lower() != "oui":
    quit()
print ("ok continuons !!!")

answer = input ("Quel marque à été crée par Phill Knight ? ")
if answer.lower() == "nike":
    print("Vous êtes fort !")
    score += 1
else:
    print("la prochaine fois...vous l'aurez")

print("vous avez " + str(score) + " questions correct ! ")
print("ce qui fait un score de " + str((score/3)*100) + " % ")
