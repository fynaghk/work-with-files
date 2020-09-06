with open("group info.txt", "a") as file:
    size = int(input("Enter number "))
    for n in range(size):
        person_ = input(f"Enter {n + 1}. person: ")
        file.write(person_ + "\n")
        print()
with open("group info.txt", "r") as file:
    for _ in range(size):
        print(file.read())
