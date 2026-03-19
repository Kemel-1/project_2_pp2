with open("example.txt", "r") as f:
    content = f.read()
    print(content)

with open("example.txt", "a") as f:
    f.write("New line added\n")