import random
import string
from colorama import init, Fore
import time
import sys
import ctypes

init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleW("Steam Keys Generator | By Maniac#5005")


txt=("""
   __  ___          _            _________________   __  ___
  /  |/  /__ ____  (_)__ _____  / __/_  __/ __/ _ | /  |/  /
 / /|_/ / _ `/ _ \/ / _ `/ __/ _\ \  / / / _// __ |/ /|_/ / 
/_/  /_/\_,_/_//_/_/\_,_/\__/ /___/ /_/ /___/_/ |_/_/  /_/  
                                                           
""")
print(Fore.CYAN + txt)

q=int(input("How many Steam Codes you want to be generated ?\n> "))

for i in range(q):
    for g in range(1):
        x=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        y=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        z=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    print(Fore.LIGHTBLUE_EX + x + "-" + y + "-" + z)

print(Fore.LIGHTGREEN_EX + "\nYour codes have been generated and saved to the .txt file !")
time.sleep(3)

sys.stdout = open("Steams Keys.txt", "w")

for i in range(q):
    for g in range(1):
        x=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        y=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        z=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    print(x + "-" + y + "-" + z)

sys.stdout.close()