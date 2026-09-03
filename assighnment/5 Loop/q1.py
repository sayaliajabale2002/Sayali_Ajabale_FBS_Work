original_id = "sayali07"
original_password = "sayali@07"

for i in range(3):
    id = input("Enter ID: ")
    password = input("Enter password: ")
    if(id==original_id and password==original_password):
        print("Correct ID and Password")
        break
    else:
        print(f'Enter correct ID & password.\n{2-i} trial left')