import os

os.makedirs("folder/subfolder", exist_ok=True)



files = os.listdir(".")
print(files)

for file in os.listdir("."):
    if file.endswith(".txt"):
        print(file)