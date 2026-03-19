import shutil

shutil.copy("example.txt", "backup.txt")
print("Файл көшірілді! backup.txt пайда болды")


import shutil
import os

if os.path.exists("backup.txt"):
    os.remove("backup.txt")