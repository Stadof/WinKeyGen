import random

# Made by Stadof
# Github: https://github.com/stadof/

print()
print("             ------------------------------------------")
print("             ~~~~~~~~ WINDOWS 10 KEY GENERATOR ~~~~~~~~")
print("             ------------------------------------------")
print()
print("This program uses Microsoft's algorithm to generate random Windows 10 keys")
print("   Feel free tu run the program several times to find a working key")
print("                  --- NOT ALL KEYS WILL WORK ---")



characters = "123456789abcdefghijklmnopqrstuvwxyz".upper()

print()
print()
print(" - Keys - \n")
for pwd in range(25):
    final_key = ''
    for number_chact in range(25):
        final_key += random.choice(characters)
        final_key_1 = '-'.join(final_key[i:i+5] for i in range(0, 25, 5))
    print("",final_key_1)
   
