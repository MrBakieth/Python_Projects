import random
letters  = ['a','b','c','d','e','f','g','i','h','j','k','l','m','n','o','p','q','r'
            ,'s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I'
            ,'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','V','Z'] 
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','%','&','(',')','*','+']
password = ""
print("Welcome to password generator!")
while True: 
    nr_letters = int(input("How many letters would you like?\n"))
    if nr_letters <= 16:
        while True:
             nr_symbols= int(input("How many symbols would you like?\n"))
             if nr_symbols < 10:
                 nr_numbers = int(input("How many numbers would you like?\n"))
                 if nr_numbers <= 10:
                     for char in range (1, nr_letters + 1):
                         password += random.choice(letters)
                     for char in range (1,nr_symbols + 1):
                         password += random.choice(symbols)
                     for char in range (1, nr_numbers + 1):
                         password += random.choice(numbers)   
                     print(password)
                 else:
                     print("Invalid Value")
                     continue
                 break
             else:
                 print("Invalid value!")
                 continue
        break 
    else:
        print("Invalid value!")
        continue 





