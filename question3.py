def capitalise (*arg):
    return phrase.upper()
   
while True:
    phrase = input("Put statement or type q to quit: ")
    print(capitalise(phrase))

    if phrase == "q":
        break    