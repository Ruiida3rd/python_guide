while True:
    try:

        print(45 * "=")
        print(15 * " " , "PYTHON TUTORIAL" , 15 * " ")
        print(45 * "=")
        print("")
        print(" -PICK A LESSON THAT YOU WOULD LIKE TO LEARN-")
        print("")
        print("")
        print(15 * "#" , "PRELIM LESSONS" , 15 * "#")
        print("\n1 - Introduction to Programming")
        print("2 - Basic Syntax")
        print("3 - Printing Output")
        print("4 - Python Comments")
        print("5 - Variables & Data Types")
        print("6 - Basic Data Types")
        print("7 - Arithmethic Operators and Expressions")
        print("8 - Basic Input & Output\n")
        print(15 * "#" , "MIDTERM LESSONS" , 15 * "#")
        print("\n9 - Conditional Statement")
        print("10 - Logical Operators\n")
        print(15 * "#" , "FINAL LESSONS" , 15 * "#")
        print("\n11 - Introduction to Iterations & Loops")
        print("")
        print("")
        print("Type 0 = exit program")
        print(45 * "=")
        choice = int(input("Pick a Number :"))
        if choice == 0:
            exit()
        elif choice == 1:
            print("\n1 - Introduction to Programming")
        elif choice == 2:
            print("\n2 - Basic Syntax")
        elif choice == 3:
            print("\n3 - Printing Output")
        elif choice == 4:
            print("\n4 - Python Comments")
        elif choice == 5:
            print("\n5 - Variables & Data Types")
        elif choice == 6:
            print("\n6 - Basic Data Types")
        elif choice == 7:
            print("\n7 - Arithmethic Operators and Expressions")
        elif choice == 8:
            print("\n8 - Basic Input & Output")
        elif choice == 9:
            print("\n9 - Conditional Statement")
        elif choice == 10:
            print("\n10 - Logical Operators")
        elif choice == 11:
            print("\n11 - Introduction to Iterations & Loops")
        elif choice <0 or choice >11:
            print("\n INVALID INPUT!! \n")
        while True:
            print("")
            back = input("Go back? or stop program(y/n) :")
            if back == "y":
                break
            elif back == "n":
                exit()
            else:
                print("INVALID INPUT!!!")
    except ValueError:
        print("INVALID INPUT! Please enter a number.")
