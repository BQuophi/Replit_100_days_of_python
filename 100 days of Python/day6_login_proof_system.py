# Day 6 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python

# A basic login proof system that checks the credentials of user during a login process

print("""
MY LOGIN SYSTEM
+++++++++++++++""")
print()
username = input("Username > ")
password = input("Password > ")
if username == "David" and password == "totallyNotBald":
  print("Why hello there David, what a lovely accent you have, you could have charmed your way in here even without a password")
elif username == "Kweku" and password == "Kwekuisbald":
  print("A warm welcome to you Kweku, you are a lovely person")
elif username == "Lauren" and password == "Laurenisalady":
  print("Nice to have to here Lauren")
else : 
  print("Get outta here pls. System doesn't recognize you")
