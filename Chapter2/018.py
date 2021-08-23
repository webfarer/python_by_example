user_numb = int(input("Input your number pls: "))

if user_numb < 10:
    print("Too low")
elif user_numb >= 10 and user_numb <= 20:
    print("Correct")
else:
    print("Too high")