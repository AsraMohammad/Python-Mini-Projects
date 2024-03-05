print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play: ) ")
score = 0

answer = input("what does CPU stand for? ").lower()
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does RAM stands for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does PSU stands for? ")
if answer.lower() == "power supply unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct !")

print("You got " + str((score / 4) * 100) + "%.")
