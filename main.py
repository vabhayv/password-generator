import random
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z''A','B','C','D','E','F','G','H','I','J',
'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','&','*','(',')','_','+',';',':','%','?','/']

input("Welcome to the password generator!!\ntap enter to continue")

symbol = int(input("How many symbols you need in your password?"))
number = int(input("How many numbers you need in your password?"))
alphabet = int(input("How many alphabets you need in your password?"))


password_list = []

for alpha in range(1,alphabet+1):
    password_list += random.choice(alphabets)

for num in range(1,number+1):
    password_list += random.choice(numbers)

for sym in range(1,symbol+1):
    password_list += random.choice(symbols)
    

random.shuffle(password_list)

password = ""

for elements in password_list:
    password += elements
    
    
print(f"Your password is : {password}")




















    
