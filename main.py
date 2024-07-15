import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcom to the PPG (PyPassword Genetartor)!")
letters_in_pass = int(input("How many letters would you like in your password?\n"))
symbols_in_pass = int(input("How many symbols would you like in your password?\n"))
numbers_in_pass = int(input("How many numbers would you like in your password?\n"))

letter = ""
number= ""
symboll = ""

for i in range(0, letters_in_pass+1):
    letter +=random.choice(letters)

for i in range(0, numbers_in_pass+1):
    number +=random.choice(numbers)

for i in range(0, symbols_in_pass+1):
    symboll +=random.choice(symbols)

generated_password = letter + number + symboll
generated_password = ''.join(random.sample(generated_password,len(generated_password)))

print(f"Here is your password {generated_password}")





