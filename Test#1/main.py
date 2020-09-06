import os

remove_ = False
with open("group info.txt", "a") as file:
    size = int(input("Enter number "))
    for n in range(size):
        person_ = input(f"Enter {n + 1}. person: ")
        file.write(person_ + "\n")
        print()

enter = input("Do you want to delete this file? ")
if (enter.lower() == "yes"):
    os.remove("group info.txt")
    print("You deleted file!")
else:
    with open("group info.txt", "r") as file:
        for _ in range(size):
            print(file.read())
