

print("Welcome To Jay's Computer Programming Appreciation App")

Answer = input("Do you like Computer Programming? (Y/N):")
print(Answer)

if Answer == "Y" or Answer == "y":
    Adjective = input("In one adjective, how do you describe computer programming?: ")
    Verb1 = input("In one verb, state what you like to do along with programming?: ")
    Verb2 = input("In one verb, state what you like to do along with staying hyderated?: ")
    FamousPerson = input("Name a Famous Person who inspires you?: ")
    MadLib = f"Computer Programming is so {Adjective}! It makes me so excited all the time because I love to {Verb1}. Stay Hydrated and {Verb2} like you are {FamousPerson}!"
    print(MadLib)
elif Answer == "N" or Answer == "n":
    print("This is not the correct application for you")
else:
    print("Invalid Response")
