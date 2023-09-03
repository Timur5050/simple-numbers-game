import random


def guesser_number(value):
    counter = 1
    if int(value) == choice:
        print("Congrats. You guessed on the first try the number :)")

    while int(value) != choice:
        if int(value) > choice:
            print("Too close.  ")
            value = int(input("Try a little lower : "))
            counter += 1
        elif int(value) < choice:
            print("Too close.  ")
            value = int(input("Try a little bigger : "))
            counter += 1
    print("-----------------------------------------------------------")
    print("Congrats. You guessed the number :)", "number of attempts : ", counter)
    print("-----------------------------------------------------------")


print("Hello, that is my new random game ")
while True:
    print("Do you want to play? \nYes - print yes \nNo - print no :")
    answ = input("So? : ")
    if answ.lower() == 'yes':
        A = int(input("Choose the start : "))
        B = int(input("Choose the end: "))
        choice = random.randint(A, B)
        value = input("OK, now guess the number I just guessed : ")
        while not value.isdigit() or int(value) < A or int(value) > B:
            print("Wrong answer, try to write digit between", A, "and", B)
            value = input("Write here : ")
        guesser_number(value)
    elif answ.lower() == 'no':
        break
    else:
        print("You should write only yes or no")
