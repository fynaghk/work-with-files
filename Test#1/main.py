with open("group info.txt", "a") as file:


    file.write("Someone : 124")
    file.close()

    newFile = open("group info.txt", "r")
    print(newFile.read())


