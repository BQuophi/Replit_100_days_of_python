# Day 5 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python

# Build an Akinator Style Game
# Determine your marvel character

print("MARVEL MOVIE CHARACTER CREATOR")
print("------------------------------")
print()
print("Answer with lowercase yes or no")
spiderman = input("Do you like 'hanging around'?: ")
if spiderman == "yes":
  print("You're Spider-man!")
else:
  print("Then you're not Spider-man")

thor = input("Do you like thunder?: ")
if thor == "yes":
  print("Then you're Thor!")
else:
  print("Then you're not Thor")

ironman = input("Do you like technology?: ")
if ironman == "yes":
  print("Yay! You're Iron-man!")
else :
  print("Then you're not Iron-man")

captain = input("Do you feel 'Marvelous'?")
if captain == "yes":
  print("Voila, you're Captain America!")
else:
  print("Then you're not Captain America")

anyother = input("Are you not any of the above?: ")
if anyother == "yes":
  print("Then let's find out who you are!")

newcharacter = input("What is your character?: ")
print("Hmm, great choice!, Nice to meet you", newcharacter)
