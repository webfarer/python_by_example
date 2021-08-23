user_rainy = str.lower(input("Tell me pls - is a rainy: "))

if user_rainy == 'yes':
    user_umbrella = str.lower(input("It is too windy for an umbrella?: "))
    if user_umbrella == 'yes':
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")