#Thursday12March.py
#Simple login simulation with specific feedback messages

#Default inputs
username = "admin"
password = "admin@2026"

user_input = input("Please enter username")
pass_input = input("Please enter password")

if user_input != username and pass_input != password:
    print("wrong details")
elif user_input != username:
    print("Username is wrong")
elif pass_input != username:
    print("password is wrong")
else: user_input == "admin" and pass_input == "admin@2026"
print("You have been successfully logged in")




