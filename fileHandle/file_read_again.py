try:
    file = open("abc.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("This file does not exist!")
