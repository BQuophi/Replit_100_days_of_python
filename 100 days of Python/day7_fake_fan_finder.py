print("Fake Fan Finder 😊") 
print("-----------------")
print()
print("""Are you a superfan of Barcelona Football Club?

Alright, then let's find out!""")
players = input("When was the last time Barca won a Champions League? ")
if players == "2015":
  print("Correct!, but you got that by pure chance.")
  messi = input("Who is the greatest player in Barca's history? ")
  if messi == "messi" or messi == "Messi":
    print("You got that by pure chance again, but you're proving yourself !")
    ballon = input("Who won the most Ballon D'or in the history of FC Barcelona? ")
    if ballon == "messi" or ballon == "Messi":
      print("You're slightly a true fan of Barca!")
      coach = input("Who was the coach of Barca in 2023? ")
      if coach == "xavi" or coach == "Xavi":
        print("You're a true fan of Barca!")
elif players == "2014":
  print("""Close, but not quite. You need to up your game. 
  
        Come back when you become a superfan 😊
""")
else:
  print("Nope. Come back when you become a superfan 😊 ")