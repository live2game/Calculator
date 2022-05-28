def calculate():
    while True:
        operator = input("What operator do you wanna use(*,/,+,-)? ")
        possible_op = "+-*/"

        if operator not in possible_op:
            continue
        try:
            number_1 = float(input("What is your first number? "))
            number_2 = float(input("What is your second number? "))
            if operator == "/" and number_2 == 0:
                print("You can't devide by Zero! ")
                continue
        except ValueError:
            print("Invalid operation")
            continue

        if operator == "+":
            print(number_1 + number_2) 
        elif operator == "-":
            print(number_1 - number_2) 
        elif operator == "*":
            print(number_1 *  number_2) 
        elif operator == "/":
            print(number_1 / number_2) 

        while True:
            answer = input("Do you wanna calculate again? \n(Y/N) ").lower()
            if answer == "y":
                break
            elif answer == "n":
                quit()
            else: 
                print("Wrong Input")
                continue 

calculate()