with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# a - append file
# w - write over existing file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")
