
# general and input------------------------------------------------------

from math import pi

def inputfloatposend(text):       # input control: R+
    while True:
        try: 
            in_t = input(text)
            if in_t.lower() in ["end"]: 
                in_f = None 
                break
            in_f = float(in_t)
            if in_f >= 0:
                break
            print("Please enter a postive decimal number.")
        except ValueError: 
            print("Please enter a float decimal.")
    return in_f

def inputfloatpos(text):
    while True:
        try: 
            in_t = input(text)
            in_f = float(in_t)
            if in_f >= 0:
                break
            print("Please enter a postive decimal number.")
        except ValueError: 
            print("Please enter a float decimal.")
    return in_f

def inputfloat(text):
    while True:
        try: 
            in_t = input(text)
            in_f = float(in_t)
            break
        except ValueError: 
            print("Please enter a float.")
    return in_f

def inputintposend(text):          # input control: N
    while True:
        try: 
            in_t = input(text)
            if in_t.lower() in ["end"]: 
                in_i = None
                break
            in_f = float
            in_i = int(in_t)
            if in_i >= 0:
                break
            print("Input wrong. Please enter a postive integer number.")
        except ValueError: 
            print("Input wrong. Please enter a integer number.")
    return in_i 

def inputintpos(text):
    while True:
        try: 
            in_t = input(text)
            in_i = int(in_t)
            if in_i >= 0:
                break
            print("Input wrong. Please enter a postive integer.")
        except ValueError: 
            print("Input wrong. Please enter a integer.")
    return in_i 

# area ------------------------------------------------------------------

def a_square():
    a = inputfloatpos("Enter the side length of the square: ")
    s = round(pow(a, 2), 2)
    print(f"The area of the square is {s}.")
    return 

def a_rectangle():
    a = inputfloatpos("Enter the first side of the rectangle: ")
    b = inputfloatpos("Enter the second side of the rectangle: ")
    s = round(a*b, 6)
    print(f"The area of the rectangle is {s}.")
    return 

def a_parallelogram():
    a = inputfloatpos("Enter the first side of the rectangle: ")
    b = inputfloatpos("Enter the second side of the rectangle: ")
    s = round(a*b, 6)
    print(f"The area of the parallelogram is {s}.")
    return 

def a_triangle():
    a = inputfloatpos("Enter the hypothenuse of the triangle: ")
    h = inputfloatpos("Enter the height: ")
    s = round((a*h)/2, 2)
    print(f"The area of the triangle is {s}.")
    return 

def a_circle():
    r = inputfloatpos("Enter the radius of the circle: ")
    s = round(pi*pow(r, 2), 2)
    print(f"The area of the circle is {s}.")
    return 

def a_eclipse():
    a = inputfloatpos("Enter the first radius: ")
    b = inputfloatpos("Enter the second radius:")
    s = round(pi*a*b, 6)
    print(f"The area of the eclipse is {s}.")
    return 

def a_trapezoid():
    a = inputfloatpos("Enter the base side of the parallels: ")
    b = inputfloatpos("Enter the opposite side of the base side: ")
    h = inputfloatpos("Enter the height on the base side: ")
    s = round((a + b)/2*h, 6)
    print(f"The area of the trapezoid is {s}.")
    return 

def a_sector():
    r = inputfloatpos("Enter the radius of the sector of a circle: ")
    a = inputfloatpos("Enter the angle of the sector: ")
    s = round(pi*pow(r, 2)*a/360, 6)
    print(f"The the sector area of the circle is {s}.") 
    return 

def a_help():
    print("Shapes: square, rectangle, parallelogram, triangle, circle, eclipse, trapezoid or sector (of a circle).")
    print("Input of variable in positve  decimal number.")
    print("Enter 'end' to end the program.")
    return

def area():
    print("AREA CALCULATOR")
    print("Input 'help' or '?' for help")
    while True:
        x = input("Enter a shape: ")
        if x == "square":
            a_square()
        elif x == "rectangle":
            a_rectangle()
        elif x == "parallelogram":
            a_parallelogram()
        elif x == "triangle":
            a_triangle()
        elif x == "circle":
            a_circle()
        elif x == "elipse":
            a_eclipse()
        elif x == "trapezoid":
            a_trapezoid()
        elif x == "sector":
            a_sector()
        elif x in ["help","?"]:
            a_help()
        elif x == "end":
            break
        else:
            print("Shape not found. Please try again.")
    print("End of area calculator.")
    return

# volume-----------------------------------------------------------------

def v_cube():
    a = inputfloatpos("Enter a side of the cube: ")
    s = round(pow(a, 3), 6)
    print(f"The volume of the cube is {s}.")
    return

def v_box():
    print("Enter all three sides of the box")
    a = inputfloatpos("Site a: ")
    b = inputfloatpos("Site b: ")
    c = inputfloatpos("Site c: ")
    s = round(a*b*c, 6)
    print(f"The volume of the box is {s}.")
    return 

def v_cylinder():
    h = inputfloatpos("Enter the height of the cylinder: ")
    r = inputfloatpos("Enter the radius of the cylinder: ")
    s = round(h*pi*pow(r, 2), 6)
    print(f"The volume of the cylinder is {s}.")
    return 

def v_sphere():
    r = inputfloatpos("Enter the radius of the sphere: ")
    s = round(4/3*pi*pow(r, 3), 6)
    print(f"The volume of the sphere is {s}.")
    return 

def v_cone():
    h = inputfloatpos("Enter the height of the cone: ")
    r = inputfloatpos("Enter the radius of the cone: ")
    s = round((h*pi*pow(r, 2))/3, 6)
    print(f"The volume of the cone is {s}.")
    return 

def v_trangularprism():
    h = inputfloatpos("Enter the height of the trangular prism: ")
    a = inputfloatpos("Enter the base of the trangular prism: ")
    b = inputfloatpos("Enter the length of the trangular prism: ")
    s = round((h*a*b)/2, 6)
    print(f"The volume of the trangular prism is {s}.")
    return 

def v_help():
    print("Figures: cube, box, cylinder, sphere, cone, trangular prism.")
    print("Input of variable in positve decimal number.")
    print("Enter 'end' to end the program.")
    return

def volume():
    print("VOLUME CALCULATOR")
    print("Input 'help' or '?' for help")
    while True:
        x = input("Enter a figure: ")
        if x == "cube":
            v_cube()
        elif x == "box":
            v_box()
        elif x == "cylinder":
            v_cylinder()
        elif x == "sphere":
            v_sphere()
        elif x == "cone":
            v_cone()
        elif x == "trangular prism":
            v_trangularprism()
        elif x in ["help, ?"]:
            v_help()
        elif x == "end":
            break
        else:
            print("Figure not found. Please try again.")
    return

# derivates -------------------------------------------------------------

def function_in_text(k,name):
    function_f = name+"(x) ="           # build f(x)= ...
    for i in range(len(k)-1,-1,-1):     # from "top" to "bottom"
        if k[i] < 0:    # for negative value 
            function_f = function_f + " " + str(k[i]) + "x^" + str(i)
        elif k[i] > 0:  # add the "+" sign to a positive value
            function_f = function_f + " +" + str(k[i]) + "x^" + str(i)
    if len(function_f) <= len(name)+5:  # if all 0.0, then add 0
        function_f = function_f+" 0"
    # Improvement : x instead of x^1, "" instead of x^0, ...
    return function_f

def degree(k):                  # deg(f)=... | degree = highest exponent of the polynomial
    grad = 0                    # if someone enters zero for coefficients
    for i in range(len(k)):     # the highest non-zero number is the degree
        if k[i] != 0:
            grad = i
    return grad

def polynom_dash():
    # calculations of derivatives of polynoms
    # f(x)  = a x^n
    # f'(x) = n a x^(n-1)
    # with  f(x)=x --> f'(x)=0
    print("DERIVATIVE OF POLYNOM FUNCTION CALCULATOR")
    print("   f(x) = a_n x^n + ... + a_2 x^2 + a_1 x + a_0")
    while True:
        n = inputintposend("Degree of Polynom-Function or 'end': ") 
        if n == None: break     # input of end 
        a = []      # f(x)= a[n]x^n + a[2]x^2 + a[1]x + a[0]
                    # coefficients a_n, position is the index n and degree of the exponent 
        a_dash = [] # f'(x) = na[n]x^(n-1) + 2a[2]x + a[1] 
                    # a_dash[n-1] = n*a[n] ... a_dash[1]=2a[2] ... a_dash[0]=a[1]
        # input of the coefficients of the polynomial
        for i in range(n+1):    
            in_float = inputfloat("Input a_"+str(i)+" : ")
            a.append(in_float)
        # Calculate the coefficients of the derivative polynomial
        for i in range(n):
            a_dash.append(round(( a[i+1] * (i+1) ), 12))     # f'(x) = n a x^(n-1)
        # Output of the input and the derivative in almost natural notation
        print("Your input:  ", function_in_text(a,"f"), "  with the degree", degree(a))
        print("Derivation:  ", function_in_text(a_dash,"f'"), "  with the degree",degree(a_dash))
    return

# tax of list------------------------------------------------------------

def tax_of_list():
    list = []
    total = 0
    gst = 0.05
    pst = 0.07
    print("TAX CALCULATOR OF A LIST")
    print("Enter 'end' to end the program.")
    while True:
        n = inputintposend("Enter the amount of items: ")   
        if n == None:
            break
        for i in range(n):    
            in_float = inputfloat(f"Input the price of {i+1}. item: ") 
            list.append(round(in_float, 6))
        summe = sum(list)
        GST = round(summe*gst, 2)
        PST = round(summe*pst, 2)
        total = round(summe + gst + pst, 6)
        print(f"Subtotal: {summe}")
        print(f"GST     : {GST}")
        print(f"PST     : {PST}")
        print("---------------------")
        print(f"Total   : {total}")
        print("---------------------")
    return

# tax of amount ---------------------------------------------------------

def tax_of_amount():
    total = 0
    gst = 0.05
    pst = 0.07
    print("TAX AMOUNT CALCULATOR")
    print("Enter 'end' to end the program.")
    while True:
        amount = inputfloatposend("Enter the price: ")
        if amount == None:
            break
        total        = round(amount*(1+gst+pst), 6)
        total_tax    = round(total-amount, 6)
        subtotal     = round(amount/(1+gst+pst), 6)
        subtotal_tax = round(amount-subtotal, 6)
        amount       = round(amount, 6)                 
        print(f"For a price of {amount} without tax:")
        print(f"Tax  : {total_tax}")
        print(f"Total: {total}")
        print("-----------------------")
        print(f"For a price of {amount} including tax:")
        print(f"Tax     : {subtotal_tax}")
        print(f"Subtotal: {subtotal}")
    return

# interest ----------------------------------------------------------------------------

def interest():
    print("INTEREST COMPOUNDS CALCULATOR")
    print("Enter 'end' to end the program.")
    while True:
        p = inputfloatposend("Enter the principal amount: ")
        if p == None:
            break
        r = inputfloatpos("Enter the annual interest rate in percent: ")
        t = inputintpos("Enter the number of years: ")
        i = round(p*pow((1 + r/100), t), 6)
        print(f"The final amount is {i}.")
    return


# main ------------------------------------------------------------------
def main():
    print("WELLCOME USER")
    while True:
        print("THIS IS A AREA CALCULATOR (1), VOLUME CALCULATOR (2), TAX CALCULATOR OF A LIST (3), TAX CALCULATOR OF A AMOUNT (4), POLYNOM DASH (5) AND INTEREST CALCULATOR (6). PLEASE CHOOSE A NUMBER.")
        print("Enter 'end' to end the program.")
        x = input("ENTER BETWEEN 1 TO 6: ")
        print("-------------------------------")
        if x == "1":
            area()
        elif x == "2":
            volume()
        elif x == "3":
            tax_of_list()
        elif x == "4":
            tax_of_amount()
        elif x == "5":
            polynom_dash()
        elif x == "6":
            interest()
        elif x == "end":
            break
        else:
            print("Input wrong. Please try again.")
    print("See you!")
    return
    
# main starter -------------------------------------------------------------- 
if __name__ == "__main__":
    main()
