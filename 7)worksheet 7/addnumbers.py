# addnumbers.py - examples of while loops


def addUpNumbers1():
    total = 0
    moreNumbers = "y"
    while moreNumbers == "y":
        number = int(input("Enter a number "))
        total = total + number
        moreNumbers = input("Any more numbers? ")
    print("The total is", total)


def addUpNumbers2():
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0:
        total = total + number
        number = eval(input("Number (0 to stop): "))
    print("The total is", total)


def addUpNumbers3():
    total = 0
    nStr = input("Number (return to stop): ")
    while nStr != "":
        number = eval(nStr)
        total = total + number
        nStr = input("Number (return to stop): ")
    print("The total is", total)


def namelenth():
    name = 'hina'
    inputName = ''

    while len(inputName) <= len(name)-1:
        inputName += input('Enter name :')
        print(inputName)

    print(inputName)


namelenth()
