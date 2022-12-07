options = [1, 2, 3, 4, 5]
choice = 10
while choice != 0:
    if choice in options:
        print("You have chosen: {}".format(choice))
        print("-" * 70)
    else:
        print("Please choose an option from the list below: ")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")
    choice = int(input())

