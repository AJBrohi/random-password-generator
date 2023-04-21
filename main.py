import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to my Random Password Generator!")
choice = int(input('There are 4 types of combinations to have in your password.\n1. Type 1 for "Only Letters and Numbers"\n2. Type 2 for "Only Letters and Symbol"\n3. Type 3 for "Only Numbers and Symbol"\n4. Type 4 for "Letters, Numbers and Symbol"\nWhich combination you want? : '))

password = ""

if choice == 1:
    nr_letters= int(input("\nHow many letters would you like in your password?\n"))
    nr_numbers = int(input("\nHow many numbers would you like?\n"))

    for _ in range(nr_letters):
        password += letters[random.randint(0, len(letters)-1)]

    for _ in range(nr_numbers):
        password += numbers[random.randint(0, len(numbers)-1)]

elif choice == 2:
    nr_letters= int(input("\nHow many letters would you like in your password?\n"))
    nr_symbols = int(input("\nHow many symbols would you like?\n"))

    for _ in range(nr_letters):
        password += letters[random.randint(0, len(letters)-1)]

    for _ in range(nr_symbols):
        password += symbols[random.randint(0, len(symbols)-1)]

elif choice == 3:
    nr_numbers = int(input("\nHow many numbers would you like?\n"))
    nr_symbols = int(input("\nHow many symbols would you like?\n"))

    for _ in range(nr_numbers):
        password += numbers[random.randint(0, len(numbers)-1)]

    for _ in range(nr_symbols):
        password += symbols[random.randint(0, len(symbols)-1)]
elif choice == 4:
    nr_letters= int(input("\nHow many letters would you like in your password?\n"))
    nr_numbers = int(input("\nHow many numbers would you like?\n"))
    nr_symbols = int(input("\nHow many symbols would you like?\n"))

    for _ in range(nr_letters):
        password += letters[random.randint(0, len(letters)-1)]

    for _ in range(nr_numbers):
        password += numbers[random.randint(0, len(numbers)-1)]

    for _ in range(nr_symbols):
        password += symbols[random.randint(0, len(symbols)-1)]
else:
    print("\nYou typed a wrong number. Please TRY AGIAN!")
    exit()

print(f"\nTotal character of your password is: {len(password)}")
if len(password) >= 8:
    password = ''.join(random.sample(password, len(password)))
    print(f"Your password is: {password}")
    print("Congratulations for generating a STRONG password!")    
else:
    print("\nIt's highly recommended to have atleast 8 characters in your password to have a stronger password. Please TRY AGIAN!")