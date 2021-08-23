user_name = str.lower(input("Print your name: "))
user_surname = str.lower(input("Print your surname: "))

user_fullname = str.title(user_name + ' ' + user_surname)
print(user_fullname)