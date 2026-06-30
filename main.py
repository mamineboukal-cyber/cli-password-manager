from auth import sign_in , sign_up
ans = int(input("do you want to sign_up (1) or sign_in (2): "))
while ans != 1 and ans != 2:
    print("wrong number! - choose between 1 and 2 :")
    ans = int(input("do you want to sign_up (1) or sign_in (2): "))
if ans == 1:
    sign_up()
else:
    sign_in()