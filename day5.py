#PyPassword Generator 
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to the PyPassword Generator! Let's make a super secure password for you 😀\n")

letters_count=int(input("How many letters would you like in your password? :"))
digits_count=int(input("How many digits would you like in your password? :"))
symbols_count=int(input("How many symbols would you like in your password? :"))

#Easy Solution

# password =""

# for x in range(0,letters_count):
#     password+=(letters[random.randint(0,len(letters)-1)])

# for x in range(0,digits_count):
#     password+=(digits[random.randint(0,len(digits)-1)])

# for x in range(0,symbols_count):
#     password+=(symbols[random.randint(0,len(symbols)-1)])

# print(password)

#Hard solution
secure_password=[]

for x in range(0,letters_count):
    secure_password.append(random.choice(letters))

for x in range(0,letters_count):
    secure_password.append(random.choice(digits))

for x in range(0,letters_count):
    secure_password.append(random.choice(symbols))

random.shuffle(secure_password)


print(f"Your Super Secure Custom Password is: \n {''.join(secure_password)}")





