Hufflepuff = 0
Slytherin = 0
Ravenclaw = 0
Gryffindor = 0
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
answer = int(input())
if answer == 1:
  Gryffindor += 1
elif answer == 2:
  Hufflepuff += 1
else:
  print("Wrong input.")
print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
answer2 = int(input())
if answer2 == 1:
  Hufflepuff += 2
elif answer2 == 2:
  Slytherin += 2
elif answer2 == 3:
  Ravenclaw += 2
elif answer2 == 4:
  Gryffindor += 2
else:
  print("Wrong input")
print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
answer3 = int(input())
if answer3 == 1:
  Hufflepuff += 4
elif answer3 == 2:
  Slytherin += 4
elif answer3 == 3:
  Ravenclaw += 4
elif answer3 == 4:
  Gryffindor += 4
else:
  print("Wrong input")
print("Slytherin =", Slytherin)
print("Hufflepuff =", Hufflepuff)
print("Ravenclaw =", Ravenclaw)
print("Gryffindor=", Gryffindor)