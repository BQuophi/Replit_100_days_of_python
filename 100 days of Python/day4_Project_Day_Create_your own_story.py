# Create an Adventure Simulator using input from users.
# Add colors to the output.

print("Welcome to your Adventure Story Simulator.")
print("""
  You'll be asked a bunch of questions then we'll make   you up an amazing story with YOU as the star. 
                Ready?""")

name = input("What's your name : ")
superpower = input("What's your superpower : ")
enemy = input("What's your worst enemy's name : ")
enemypower = input("What's your enemy's name : ")

print("In the land of myth, a great warrior named", "\033[32m", name,
      "\033[0m", "was born with the power of", superpower)
print()

print("For years, a great evil called", "\033[31m", enemy,
      "\033[0m had caused havoc in the land. The evil", enemy,
      "had the power of", enemypower, "and was using it to destroy the land.")

print()
print("But the warrior", name, "who had the power of", superpower,
      "and was able to defeat the evil one ")
print()
print(
    "During the battle, the enemy said",
    "\033[31m I will destroy the land and the world! \033[0m and the warrior said",
    "\033[34m I will defeat you! \033[0m")
print()

print(
    "A great battle ensued but the enemy who underestimated the warrior was defeated and the land was saved."
)

print("""
You are the warrior. Thanks for saving the land.The people greatly appreciated your dedication and strength to defend the land.
""")
