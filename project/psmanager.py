import random
import string 
import hashlib
import getpass

def PasswordGenerator(length:int=10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet)for i in range(length))
    print(f"Generated Password is :{password}")


password_maanger = {}
#dictionary

def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter the password: ")
    hashed_password= hashlib.sha256(password.encode()).hexdigest()
    #hexadecimal string 32 byte(256bits)
    password_maanger[username]= hashed_password
    print("Account Created Sucessfully\n")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password:" )
    hashed_password= hashlib.sha256(password.encode()).hexdigest()
    if username in password_maanger.keys() and password_maanger[username]== hashed_password:
        print("Login Sucessfull!\n")
    else:
        print("Invalid Username or Password\n")

def main():
    while True:
        choice = input("Enter the choice you want to select: 1->Create Account, 2->Login, 3->To generate Password, 0->Exit: ")
        
        if choice == '1':
            create_account() 
        elif choice == '2':
            login()
        elif choice == '3':
            PasswordGenerator()
        elif choice == '0':
            break
        else:
            print("Invalid Choice.")


if __name__  == "__main__":
    main()

    


