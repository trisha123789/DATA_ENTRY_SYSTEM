import database

welcome =  "WELCOME TO DATA ENTRY SYSTEM"
print(welcome)
database.create_table()
menu = """
1.ADD A USER
2.UPDATE A USER
3.DELETE A USER
4.VIEW ALL USERS
5 EXIT
ENTER YOUR SELECTION :
"""
while (user_input := input(menu))!="5":
    if user_input == "1":
        name = input("enter thr name :")
        age = int(input("enter the age :"))
        department = input("enter the department :")
        database.add_user(name,age,department)
        print("added successfully....")
    elif user_input == "2":
        id = int(input(("enter an id to update:")))
        name = input("enter thr name :")
        age = int(input("enter the age :"))
        department = input("enter the department :")
        print("updated successfully")
        database.update_user(id,name,age,department)
    elif user_input == "3":
        id = int(input(("enter an id to delete:")))
        database.delete_users(id)
        print("deleated successfully")
    elif user_input == "4":
        print("Viewing all users")
        database.view_users()
    else:
        print("INVALID INPUT .....")

