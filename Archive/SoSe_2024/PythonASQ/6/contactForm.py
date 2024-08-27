infos = []
name = input("Enter your name: ")
infos.append("Name: " + name)
age = input("Enter your age: ")
infos.append("Age: " + age)
placeOfBirth = input("Enter your place of birth: ")
infos.append("Place of Birth: " + placeOfBirth)
favoriteFood = input("Enter your favorite food: ")
infos.append("Favorite Food: " + favoriteFood)

with open("ContactForm.txt", "w") as f:
    for info in infos:
        f.write(info)
        f.write("\n")
    f.flush()
    infos = []
    favoriteColor = input("Enter your favorite color: ")
    infos.append("Favorite Color: " + favoriteColor)
    hobby = input("Enter your hobby: ")
    infos.append("Hobby: " + hobby)
    nameOfPet = input("Enter the name of your pet: ")
    infos.append("Name of Pet: " + nameOfPet)
    for info in infos:
        f.write(info)
        f.write("\n")

print()
with open("ContactForm.txt", "r") as f:
    print(f.read())