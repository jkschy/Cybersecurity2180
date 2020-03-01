def main():
    getInput()

def getInput():
    try:
        num1 = int(input("Enter First Number "))
        num2 = int(input("Enter Second Number "))
        print("What action (1- Addition, 2-Subtraction, 3-Multiplication, 4-Division)")
        action = int(input("Action(1,2,3,4, 6 to quit) "))
        Calculate(action, num1, num2)
    except ValueError as e:
       print("Incorrect Value... Try Again Please")
       getInput()
    except SyntaxError as e:
        print("Incorrect Value... Try Again Please")
        getInput()
def Calculate(Operation, num1, num2):
    running = True
    if Operation == 1:
        print(num1 + num2)
    elif Operation == 2:
        print(num1 - num2)
    elif Operation == 3:
        print(num1 * num2)
    elif Operation == 4:
        print(num1 / num2)
    elif Operation == 6:
        print("Thanks for Using the Calculator!")
        running = False
    else:
        action = input("Err Action Not Found \n Action(1,2,3,4, 6 to quit)")
        Calculate(action)
    if running:
        getInput()




if __name__ == '__main__':
    main()
