string = "string"


def func1():
    x = 1
    print(x)


def func2():
    x = 2
    print(x)


def printString():
    print(string)

    def printString2():
        string2 = "another string"
        print(string2)

    printString2()


func1()
func2()
printString()
