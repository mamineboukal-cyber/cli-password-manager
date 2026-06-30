from database import user_save , check_email , check_password
from utils import validate_email
from generator import password_generator 
def sign_up():
    print("--- sign up ---")
    while True:
        email = input("enter an email: ")
        if validate_email(email):
            break
        print("Invalid email format, try again")
    ans = int(input("enter a password (1) or generate a strong password (2): "))
    while ans != 1 and ans != 2:
        ans = int(input("enter a password (1) or generate a strong password (2): "))
    if ans == 1:
        password = input("enter a password:")
        user_save(email,password)
        print("Account created successfully")
        sign_in()
    elif ans == 2:
        ln = int(input("enter the length of the password:"))
        password = password_generator(ln)
        print("your password is:",password)
        user_save(email,password)
        print("Account created successfully")
        sign_in()
def sign_in():
    count1 =count2 = 0
    print("--- sign in ---")
    while True:
        email = input("enter your email: ")
        if validate_email(email):
            break
        print("Invalid email format, try again")
    while True:
        if count1 >= 3 or count2 >= 3:
            print("Access denied")
            break
        if check_email(email):
            password = input("your account's password:")
            if check_password(email,password):
                print("Signed in successfully")
                break
            else:
                count2 += 1
                print("wrong password try again - ",3-count2,"chances left")
        else:
            count1+=1
            print("wrong email try again - ",3-count1,"chances left")
            email = input("enter your email: ")
def sign_in_flask(email, password):
    if check_email(email):
        if check_password(email, password):
            return "Signed in successfully"
        else:
            return "Wrong password"
    else:
        return "Email not found"


    
