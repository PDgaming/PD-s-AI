#imports

import fractions
import math
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import random
import time
from tkinter import *
from time import *
import time
import datetime
from fractions import Fraction
from tkinter import *
from solver import solver

#stuff

    #Time

current_time = datetime.datetime.now()
current_time.hour

day = time.strftime("%A")
date = time.strftime("%B %d")

    #Greeting

g = " "

if current_time.hour < 12:
    g = "good morning"
elif 12 <= current_time.hour:
    g = "Good afternoon"

greetings = g

    #endings
    
e = " "

if current_time.hour > 20 and current_time < 4:
     e = "night"

endings = e

#welcome notes

print("Hey there,", greetings, "welcome to this program, I am PD, an AI made by PD.")
print("I can help you with many things related to maths and many other things other things soon in the future")
print("but right now i can only do a few things so whatever it is that you need to get done whether it is arithmatics or other maths related things just type in the keyword and i will definetly help you with whatever you need")
print("also right now i am in the development process so i don't have a lot a features but soon in the future many new features are gonna come like text to speech")
print("currently i have the the following fuctions: ")
print("1. Simple conversation")
print("2. add")
print("3. subtract")
print("4. multiply")
print("5. devide")
print("6. find the perimeter of a square")
print("7. find the perimeter of a rectangle")
print("8.find the area of a square")
print("9. find the area of a rectangle")
print("10. find the area of circle")
print("11. open calculator")
print("12. find the lcm of")
print("13. check if my number is prime")
print("14. show me the fibonachi number")
print("15. show me the cllatz conjecture")
print("16. find the percentage")
print("17. addition maths quiz")
print("18. let's play tic tac toe")
print("19. show me the time")
print("20. questions")
print("21. what day is it today")
print("22. what is today's date")
print("23. find the speed")
print("24. find the time taken")
print("25. find the distance travelled")
print("and many more in the future")
print("ok now enough talk you can type in the keyword from above to use the fuctions associated with them. Have a great day, Thank you")

#talk fuction

def talk():
    global r
    r = input("type your message: ")
    r = r.lower()

talk()

#main loop for the program

while True:
    #conversation
    if r == "hello":
        print("hello")
        talk()
    elif r == "how are you":
        print("I am fine thank you")
        r = input("and how are you ")
        if r == "i am fine":
            print("that's so good")
            talk()
        elif r == "i am not fine":
            r = input("oh that's really sad what happened")
            talk()
    elif r == "ok":
        print("i am glad to help")
        talk()
    elif r == "thanks":
        print("i am glad to help")
        talk()
    elif r == "thank you":
        print("i am glad to help")
        talk()
    
    #Questions

    elif r == "what day is it today":
        print("Today is", day)
        talk()
    
    elif r == "what is today's date":
        print("Today's date is", date)
        talk()
    
    elif r == "what is your name":
        print("my name is PD")
        talk()

    elif r == "":
        print("sorry no messages was typed")
        r = input("can you type that again: ")
    elif r == "":
        print("sorry no messages was typed")
        r = input("can you type that again: ")

#functions
    
    #basic arithmatic functions   
    
    elif r == "add":
        def addition(a,b):
            return a+b
        x=int(input(print("Enter the first number ")))
        y=int(input(print("Enter the second number ")))
        z = addition(x,y)
        print("The result is",z)
        talk()
    
    elif r == "subtract":
        def subtraction(a,b):
            return a-b
        x=int(input(print("Enter the first number ")))
        y=int(input(print("Enter the second number ")))
        z = subtraction(x,y)
        print("The result is",z)
        talk()
            
    elif r == "multiply":
        def multiplication(a,b):
            return a*b
        x=int(input(print("Enter the first number ")))
        y=int(input(print("Enter the second number ")))
        z = multiplication(x,y)
        print("The result is",z)
        talk()
            
    elif r == "devide":
        def division(a,b):
            return a/b
        x=int(input(print("Enter the first number ")))
        y=int(input(print("Enter the second number ")))
        z = division(x,y)
        print("The result is",z)
        talk()                
        
    #fuctions to find the perimeter and circumference of a shape
     
    elif r == "find the perimeter of a square":
        l = int(input("length of one side of the square = "))
        perimeter_of_square = l*4
        print("Perimeter =", perimeter_of_square)
        talk()
    
    elif r == "find the perimeter of a rectangle":
        l = int(input("length of the rectangle = "))
        b = int(input("breadth of the rectangle = "))
        perimeter_of_rectangle = 2*(l+b)
        print("Perimeter =", perimeter_of_rectangle)
        talk()
    
    elif r == "find the circumference of a circle":
        r = float(input("Enter the radius of the circle "))
        c = 2 * math.pi * r
        c = round(c)
        print("The circumference of your circle is", c)
        talk()        

    elif r == "find the perimeter of a triangle":
        a = input("Is the trianle a equilateral triangle? ")
        a = a.lower()
        if a == "yes":
            s = int("Enter the length of a side of the triangle")
            perimeter_of_trianle = s * 3
            print("The perimeter of the triangle is", perimeter_of_trianle)
        elif a == "no":
            a = int("Enter the length of the first side of the triangle")
            b = int("Enter the length of the second side of the triangle")
            c = int("Enter the length of the third side of the triangle") 
            perimeter_of_trianle = a + b + c
            print("The perimeter of the triangle is", perimeter_of_trianle)
        else:
            print("please answer only in yes or no next time")
            talk()

    elif r == "find the perimeter of a regular polygon":
        s = int(input("Enter the number of sides the polygon has "))
        l_of_s = int(input("Enter the length of a side of the polygon"))
        perimeter_of_polygon = s * l_of_s
        print("The perimeter of this polygon is", perimeter_of_polygon)
        talk()

    #fuctions to find areas of a shape
        
    elif r == "find the area of a square":
        l = int(input("length of one side of the square = "))
        area = l*l
        print("Area =", area)
        talk()
    
    elif r == "find the area of a rectangle":
        l = int(input("length of the rectangle = "))
        b = int(input("breadth of the rectangle = "))
        area = l*b
        print("Area =", area)
        talk()
        
    elif r == "find the area of a circle":
        r = float(input("radius = "))

        c = 2 * math.pi * r
        area = math.pi * pow(r, 2)

        c = round(c)
        area = round(area)
                
        print("circumference =", c)
        print("Area =", area)
        talk()
    
    #3D shapes
        #functions to find volume of a shape

    elif r == "find volume of a cube":
        l = int(input("Enter the length of a side of the cube "))
        v = l * l * l
        print("The volume is", v)
        talk()
    
    elif r == "find volume of a cuboid":
        l = int(input("Enter the length of the cuboid "))
        b = int(input("Enter the breadth of the cuboid "))
        h = int(input("Enter the height of the cuboid "))
        v = l * b * h
        print("The volume is", v)
        talk()

        #functions to find surface area of a shape

    elif r == "find surface area of a cuboid":
        l = int(input("Enter the length of the cuboid "))
        b = int(input("Enter the breadth of the cuboid "))
        h = int(input("Enter the height of the cuboid "))
        sa1 = l * h  + b * h + l * b
        sa2 = 2 * sa1  
        print("The surface area is", sa2)
        talk()

    #Motion

    elif r == "find the speed":
        d = int(input("Enter the distance travelled in km "))
        t = int(input("Enter the time taken to cover the distance in hours "))
        s = d / t
        print("The speed is", s)
        talk()
    
    elif r == "find the time taken":
        d = int(input("Enter the distance travelled in km "))
        s = int(input("Enter the speed in km/h "))
        t = d / s
        print("The time taken is", t)
        talk()

    elif r == "find the distance travelled":
        s = int(input("Enter the speed in km/h "))
        t = int(input("Enter the time taken "))
        d = s * t
        print("The distance travelled is", d)
        talk()
    
    #Temperature

    elif r == "Convert Celcius to Kelvin":
        c = int(input("Enter the temperature in Celcius "))
        temperature_in_Kelvin_from_Celcius = c + 273
        print("The temerature in Kelvin is", temperature_in_Kelvin_from_Celcius)
        talk()
    
    elif r == "Convert Kelvin to Celcius":
        k = int(input("Enter the temperature in Kelvin "))
        temperature_in_Celcius_from_Kelvin = c - 273
        print("The temerature in Kelvin is", temperature_in_Celcius_from_Kelvin)
        talk()
    
    elif r == "Convert Farenheit to Celcius":
        f = int(input("Enter the temperature in Farenheit "))
        fraction = Fraction(5, 9)
        p1_of_F_to_C = f - 32
        temperature_in_Celcius_from_Farenheit = p1_of_F_to_C * fraction
        print("The temerature in Celsius is", temperature_in_Celcius_from_Farenheit)
        talk()
    
    elif r == "Convert Celcius to Farenheit":
        c = int(input("Enter the temperature in Celcius "))
        fraction_for_c_to_F = Fraction(9, 5)
        p1_of_C_to_F = c * fraction
        temperature_in_Farenheit_from_Celcius = p1_of_C_to_F + 32
        print("The temerature in Farenheit is", temperature_in_Farenheit_from_Celcius)
        talk()

    #calculator    
    
    elif r == "open calculator":
        print("END as an operation sign "
                "will terminate the program")
        while True:
            s = input("Sign (+,-,*,/,END): ")
            s = s.lower()
            if s == 'end': break
            if s in ('+','-','*','/'):
                x = float(input("x= "))
                y = float(input("y= "))
                if s == '+':
                    print("%.2f" % (x+y))
                elif s == '-':
                    print("%.2f" % (x-y))
                elif s == '*':
                    print("%.2f" % (x*y))
                elif s == '/':
                    if y != 0:
                        print("%.2f" % (x/y))
                    else:
                        print("Division by zero!")
        else:
            print("Invalid operation sign")
        talk()

    #LCM

    elif r == "find the lcm of":
        def lcm(a, b):
            m = a * b
            while a != 0 and b != 0:
                if a > b:
                    a %= b
                else:
                    b %= a
            return m // (a + b)
                    
        x = int(input("a = "))
        y = int(input("b = "))
        print("LCM: ", lcm(x, y))
        talk()

    #Prime numbers

    elif r == "check if my number is prime":                
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            limit = sqrt(n)
            i = 2
            while i <= limit:
                if n % i == 0:
                    return False
                i += 1
                return True
                    
        for i in range(1):
            num = int(input("Enter the number to be checked: "))
            print(is_prime(num))
        talk()
    
    #fibonachi numbers    
        
    elif r == "show me the fibonachi numbers":
        num = int(input("Enter the number of fibonacci numbers you want "))
        n1 , n2 = 0, 1
        sum = 0
        if num<=0:
            print("Please enter a number greater than 0")
        else:
            for i in range(0, num):
                print(sum, end=" ")
                n1 = n2
                n2 = sum
                sum = n1 + n2
        talk()
    
    #Conjectures    
    
    elif r == "show me the collatz conjecture":
        N = int(input("Enter a number: "))
        iteration = 0
        listNumbers = [N]

        while N !=1:
            iteration += 1
            if (N % 2) == 0:
                N = N/2
            else:
                N = (3*N) + 1
            listNumbers.append(N)
                
        print("Number of iterations: ", iteration)
        print(listNumbers)
        x = np.arange(0, iteration + 1)
        plt.plot(x, listNumbers)
        plt.title("Collatz Conjecture")
        plt.xlabel("Number of iterations")
        plt.ylabel("Numbers")
        plt.grid()
        plt.show()
        talk()

    #Percentage

    elif r == "find the percentage":
        v = int(input("Enter the value: "))
        t = int(input("Enter the total value: "))
        p = v / t
        percentage = p*100
        print("the percentage is ", percentage)
    
    #Check divisibility

    elif r == "Check divisibility":
        n = int(input(" Enter the number you want me to check: "))
        dn = int(input("Enter the number you want me to check your number with(currently available numbers are 2, 3, 4, 5, 6, 9, 10 and 11): "))
        if dn == "2":
            pass
        if dn == "3":
            pass
        if dn == "4":
            pass
        if dn == "5":
            pass
        if dn == "6":
            pass
        if dn == "8":
            pass
        if dn == "9":
            pass
        if dn == "10":
            pass
        if dn == "11":
            pass
        else:
            print("sorry i don't have the code to understand the number you entered. Please enter a number that is mentioned in the earlier text")
        talk()
    
    #Finding loss or profit

    elif r == "find loss":
        cp = int(input("Enter the cost of the object "))
        sp = int(input("Enter the selling price of the object "))
        l = cp - sp
        print("The loss is", l)
        talk()
    
    elif r == "find profit":
        sp = int(input("Enter the selling price of the object "))
        cp = int(input("Enter the cost of the object "))
        l = sp - cp
        print("The profit is", l)
        talk()
    
    #find force

    elif r == "find force of a object":
        m = input("Enter the mass of the object")
        a = input("Enter the acceleration of the object ")
        f = m * a
        print("The force of  the object is", f)

    #Multiplication table
    
    elif r == "print multiplication table":
        x = int(input("Enter the number for which you want the multiplication table for "))

        for i in range(1, 11):
            print(x, "x", i, "=", i*x)
        
    #Games
        #quiz

    #incomplete(continue from max well 365 inventions and inventors page 24)
    elif r == "name the inventors":
        invention = input("Enter the name of the invention ")
        invention = invention.lower()
        if invention == "ac motor":
            print("The AC Motor was invented by Nicola Tesla")
        if invention == "aeroplane":
            print("The Aeroplane was invented by Karl Jatho")
        if invention == "air conditioning":
            print("The Air Conditioning was invented by Willis Carrier")
        if invention == "airplane":
            print("The Airplane was invented by Orville and Wilbur Wright")
        if invention == "Airship":
            print("The Airship was invented by Henri Giffard")
        if invention == "ambulance":
            print("The Ambulance was invented by the Knights of St. John")
        if invention == "artificial heart":
            print("The Artificial Heart was invented by Willem Kolff")
        if invention == "artificial limbs":
            print("The Artificial Limbs was invented by Ambrose Pare")
        if invention == "atm":
            print("The ATM was invented by John Shepherd Barron")
        if invention == "atomic bomb":
            print("The Atomic Bomb was invented by J. Robert Oppenheimer")
        if invention == "audio tape":
            print("The Audio Tape was invented by Fritz Pfleumer")
        if invention == "ballpoint pen":
            print("The Ballpont pen was invented by Ladislao and George Biro")
        else:
            print("I am so sorry but i don't know the answer to that as i don't have the code to do so")
        talk()

    elif r == "addition maths quiz":
        pattern = input("Are you ready to start? ")
        if pattern == "":
            pattern = "+"
        if "+" in pattern:
            op = "+"
        rights = 0
        wrongs = 0
        while True:
            x = random.randint(1, 49)
            y = random.randint(1, 49)
            if op == "+":
                result = x + y
            question = "\n" + " ".join([str(x), op, str(y), "= "])
            answer = input(question)
            if int(answer) == result:
                rights += 1
                print("Right!")
            else:
                wrongs += 1
                print("Wrong!")
            again = input("Again? ")
            if again.lower() in ["no", "n"]:
                score = str(rights) + " right, " + str(wrongs) + "wrong."
                print("\n Your score: ", score)
                break
        
        #Tic Tac Toe
    elif r == "let's play tic tac toe":
        def next_turn(row, column):
            global player
            if buttons[row][column]["text"] == "" and check_winner() is False:
                if player == players[0]:
                    buttons[row][column]["text"] = player

                    if check_winner() is False:
                        player = players[1]
                        label.config(text = (players[1] + "'s turn"))
                    
                    elif check_winner() is True:
                        label.config(text = (players[0] + "wins"))
                    
                    elif check_winner() == "Tie":
                        label.config(text = ("Tie"))
                    
                else:
                    buttons[row][column]["text"] = player

                    if check_winner() is False:
                        player = players[0]
                        label.config(text = (players[0] + "'s turn"))
                    
                    elif check_winner() is True:
                        label.config(text = (players[1] + " wins"))
                    
                    elif check_winner() == "Tie":
                        label.config(text = ("Tie"))

        def check_winner():
            for row in range(3):
                if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
                    buttons[row][0].config(bg = "green")
                    buttons[row][1].config(bg = "green")
                    buttons[row][2].config(bg = "green")
                    return True
            
            for column in range(3):
                if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
                    buttons[0][column].config(bg = "green")
                    buttons[1][column].config(bg = "green")
                    buttons[2][column].config(bg = "green")
                    return True
            if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
                buttons[0][0].config(bg = "green")
                buttons[1][1].config(bg = "green")
                buttons[2][2].config(bg = "green")
                return True

            elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
                buttons[0][2].config(bg = "green")
                buttons[1][1].config(bg = "green")
                buttons[2][0].config(bg = "green")
                return True
            
            elif empty_spaces() is False:
                for row in range(3):
                    for column in range(3):
                        buttons[row][column].config(bg = "yellow")
                return "Tie"
            
            else:
                return False

        def empty_spaces():
            spaces = 9

            for row in range(3):
                for column in range(3):
                    if buttons[row][column]["text"] != "":
                        spaces -= 1
            
            if spaces == 0:
                return False
            
            else:
                return True

        def new_game():
            global player
            player = random.choice(players)
            label.config(text = player + "'s turn")

            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(text = "", bg = "#F0F0F0")

        window = Tk()
        window.title("Tic-Tack-Toe")
        players = ["X", "O"]
        player = random.choice(players)
        buttons = [[0,0,0],
                [0,0,0],
                [0,0,0]]

        label = Label(text = player + "'s turn", font = ("consolas", 40))
        label.pack(side = "top")

        reset_button = Button(text = "Restart", font = ("consolas", 20), command = new_game)
        reset_button.pack(side = "top")

        frame = Frame(window)
        frame.pack()

        for row in range(3):
            for column in range(3):
                buttons[row][column] = Button(frame, text = "", font = ("consolas", 40), width = 5, height = 2, command = lambda row = row, column = column: next_turn(row, column))

                buttons[row][column].grid(row = row, column = column)

        window.mainloop()
        talk()

    #Other things

    elif r == "show me the time":
        def update():
            time_string = strftime("%I:%M:%S %p")
            time_label.config(text = time_string)
            window.after(1000, update)
        window = Tk()
        #Time
        time_label = Label(window, font = ("Arial", 50), fg = "#00FF00", bg = "Black")
        time_label.pack()
        update()
        window.mainloop()
        talk() 
    
    elif r  == "open the time counter":
        my_time = int(input("Enter the time to be counted(in seconds): "))
        for x in range(my_time, 0, -1):
            seconds = x % 60
            minutes = int(x / 60)
            hours = int(x / 3600)
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)
            talk()

    #Gui Sudoku Solver

    elif r == "sudoku solver":
        root = Tk()
        root.title("GUI Sudoku Solver")
        root.geometry("324x550")

        label = Label(root, text = "Fill in the numbers and click solve").grid(row = 0, column = 1, columnspan = 10)

        errLabel = Label(root, text = "", fg = "red")
        errLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

        solvedLabel = Label(root, text = "", fg = "green")
        solvedLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

        cells = {}

        def ValidateNumber(P):
            out = (P.isdigit() or P == "") and len(P) < 2
            return out

        reg = root.register(ValidateNumber)

        def draw_3_x_3_Grid(row, column, bgcolor):
            for i in range(3):
                for j in range(3):
                    e = Entry(root, width = 5, bg = bgcolor, justify = "center", validate = "key", validatecommand = (reg, "%P"))
                    e.grid(row = row + i +1, column = column + j + 1, sticky = "nsew", padx = 1, pady = 1, ipady = 5)
                    cells[(row + i + 1, column + j + 1)] = e

        def draw_9_x_9_Grid():
            color = "#D0ffff"
            for rowNo in range(1, 10, 3):
                for colNo in range(0, 9, 3):
                    draw_3_x_3_Grid(rowNo, colNo, color)
                    if color == "#D0ffff":
                        color = "#ffffd0"
                    else:
                        color = "#D0ffff"

        def clearValue():
            errLabel.configure(text = "")
            solvedLabel.configure(text = "")
            for row in range(2, 11):
                for col in range(1, 10):
                    cell = cells[(row, col)]
                    cell.delete(0, "end")

        def getValues():
            board = []
            errLabel.configure(text = "")
            solvedLabel.configure(text = "")
            for row in range(2, 11):
                rows = []
                for col in range(1, 10):
                    val = cells[(row, col)].get()
                    if val == "":
                        rows.append(0)
                    else:
                        rows.append(int(val))

                board.append(rows)
            updateValue(board)

        btn = Button(root, command = getValues, text = "Solve", width = 10)
        btn.grid(row = 20, column = 1, columnspan = 5, pady = 20)

        btn = Button(root, command = clearValue, text = "Clear", width = 10)
        btn.grid(row = 20, column = 4, columnspan = 5, pady = 20)

        def updateValue(s):
            sol = solver(s)
            if sol != "no":
                for rows in range(2, 11):
                    for col in range(1, 10):
                        cells[(rows, col)].delete(0, "end")
                        cells[(rows, col)].insert(0, sol[rows - 1][col - 1])
                solvedLabel.configure(text = "Sudoku Solved")
            else:
                errLabel.configure(text = "No solution exists for this sudoku")

        draw_9_x_9_Grid()
        root.mainloop()
        talk()

    elif r == "end":
        print("OK have a good", endings)
        break

    else:
        print("I am sorry i don't understand your message as i don't have the code to understand your message")
        talk()