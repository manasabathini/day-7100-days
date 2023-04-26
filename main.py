print("Superfan of the same show?")
gameOfThrones = input("Do you like GameOfThrones?: ")
if gameOfThrones == "Yes":
  print("I am also big fan :) ")
  favCharacter = input("Who is your favorite character?: ")
  if favCharacter == "Jon Snow":
    print("your favorite character is", favCharacter, "Cool")
  elif favCharacter == "Catelyn Stark":
    print("your favorite character is", favCharacter, "cool")
  else:
    print("Oh! You like", favCharacter)
else:
  print("Sad you are not like me :( ")