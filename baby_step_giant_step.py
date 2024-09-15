#!/usr/bin/env python3
#The program is meant to calculate the value of 𝑘 which solves the expression: 𝑎 ≡ 𝑔^𝑘
#This Discrete Logarithm Problem is used to find values in cryptographic algorithms.
# The bsgs2 implementation was taken from 0xTowel/bsgs.py repository.

#The math package is used for methods necessary for calculations.
#Both ceil and floor functions are used for calculating the number of iterations performed in the baby step process.
from math import ceil, floor

def show_table(tbl, name):
    #show_table function used for displaying the elements of the generated table with a custom format
    #Params:
        # tbl -> It's a dictionary with the data generated either by baby or giant steps
        # name -> It's a string that shows the type of table either baby or giant step

    print("--",name," table--",end="\n\n")
    print(tbl,end="\n\n")
    print("-------------------",end="\n\n")

def check_prime(p):
    #check_prime function used for verifying if the p parameter is actually a prime number
    #Parameters:
        # p -> It's an integer that will be verified if it's prime or not
    #Description:
        # If p is even it can't be a primer number.
        # If p is 2 or 3 it is a prime number, no calculations needed.
        # If p is even it can't be a primer number.
        # The iterations are shortened by using the integer value of the sqrt of the number plus one and checking only odd numbers.
        # If there is another number that has a zero module then it is not a prime number, since it is divisible by another number than itself.

    if p==2 or p==3: return True
    if p%2==0: return False 
    for i in range(3, int(pow(p,0.5))+1, 2): 
        if p%i==0: 
            return False
    return True 

def giant_step_iteration(g,p,bbstbl, b, mode, c = 0,a = 0):
    #giant_step_iteration function generates a value that is compared with the baby steps table values. If one value is on the baby step, 
    # then iteration is stopped and the k value is calculated
    #Parameters
        #g -> This is an integer value representing the primitive root modulo of 𝑝.
        #p -> This is an integer prime value used for the calculation
        #bbstbl -> This is a dictionary value with the elements of the baby step generation process
        #b -> This is an integer with the top value for the iterations
        #mode -> This is an integer value used to select the calculation method using either with Fermat's Little theorem or not
        #c -> This is an integer value with the Fermat's Little Problem precompute value
        #a -> This is an integer value used for the calculation
    #Description:
        # The gstbl dictionary variable is used to save the values generated in the giant steps process.
        # Depending on the mode the giant step value is calculated diferently, if 1 is choose then it will be calculated without Fermat's Little Problem value
        # The value j is the iteration where the giant step value exists in the baby step table.
        # The value r is the teration where the baby step value mathces with the giant step table.
        # If there is a match then 𝑘 value is calculated using the formula 𝑘 = j · b + r

    gstbl = {}
    for j in range(b):
        if mode == 1:
            gsv = (g**b)**j % p # (𝑔^𝐵)^𝑞 mod 𝑝
        else:
            gsv = (a * pow(c, j, p)) % p # a * (c^j mod 𝑝) mod 𝑝
        gstbl[gsv] = j
        if gsv in bbstbl:
            show_table(gstbl, "Giant step")
            print("B: ",j)
            print("q:", b)
            print("r: ",bbstbl[gsv])
            return j * b + bbstbl[gsv]
        else:
            return "No value found ... :("

def bsgs(g, a, p):
    #bsgs function calculates the 𝑘 value using 𝑔, 𝑎 and 𝑝 values using the Discrete Logarithm Problem with the baby steps and giant steps iteration.
    # This option calculates it without the Fermat's Little theorem value.
    #Parameters
        #g -> This is an integer value representing the primitive root modulo of 𝑝.
        #a -> This is an integer value used for the calculation
        #p -> This is an integer prime value used for the calculation
    #Description:
        #Calculating B to determine the number of operations, p must be a prime number
        #Calculating nh through g^-1 mod p which will be used for the further iterations

    B = floor(pow(p, 0.5))
    nh = pow(g,-1,p)

    bbstbl = {a*nh**i % p: i for i in range(B)} # Baby Step value generator
    show_table(bbstbl, "Baby step")
    
    print("******************************************************************",end="\n\n")

    return giant_step_iteration(g=g,p=p,bbstbl=bbstbl,mode=1,b=B) # Calculating giant steps

def bsgs2(g, a, p):
    #bsgs function calculates the 𝑘 value using 𝑔, 𝑎 and 𝑝 values using the Discrete Logarithm Problem with the baby steps and giant steps iteration.
    # This option calculates it using the Fermat's Little theorem value.
    #Parameters
        #g -> This is an integer value representing the primitive root modulo of 𝑝.
        #a -> This is an integer value used for the calculation
        #p -> This is an integer prime value used for the calculation
    #Description:
        #Calculating N to determine the number of operations, p must be a prime number
        #Calculating nh through g^-1 mod p which will be used for the further iterations

    N = ceil(pow(p - 1, 0.5))  # Notice that this option use ceiling value instead of floor

    tbl = {pow(g, i, p): i for i in range(N)} # Baby Step value generator
    show_table(tbl, "Baby step")

    c = pow(g, N * (p - 2), p) # Precompute via Fermat's Little Theorem
    print("Fermat Little Theorem value: ", c,end="\n\n")

    print("**********")

    return giant_step_iteration(g,p,bbstbl=tbl,mode=2,c=c,a=a,b=N) # Calculating giant steps

def input_values():
    #input_values function asks for the parameters g, a and p necessary for k calculation. It lets you choose the between using 
    # Fermat's Little Theorem and verify that p is a prime number. Only positive integer values are valid. 
    #Description:
        #Each value is verified.
        #There are three modes:
            # 1.- Calculate k without Fermat's Little Theorem
            # 2.- Calculate k using Fermat's Little Theorem
            # 3.- Verify that p is a prime number

    try :
        g = int(input("Insert the g value: "))
        if g < 0:
            raise ValueError()
        a = int(input("Insert the a value: "))
        if a < 0:
            raise ValueError()
        p = int(input("Insert the p value (make sure p is a prime value):"))
        if p < 2:
            raise ValueError()
        mode = int(input("Inser which mode would you like to choose, 1 for normal option or 2 you want to use Precompute Fermat's Little Theorem, type 3 if you want to verify that p is prime: "))
        print("Thanks!! Processing ...")
        if mode == 1:
            print("k: ", bsgs(g,a,p))
        elif mode == 2:
            print("k: ", bsgs2(g,a,p))
        elif mode == 3:
            if check_prime(p):
                print("The chosen p is prime...")
            else:
                print("The chose p is not a prime number :( it can not be used in this program... Make sure to choose a valid prime number.")
        else:
            raise ValueError("The mode value can only be 1, 2 or 3")
    except ValueError:
        print ("The values must be an intefer and cannot be negative.")
    except Exception:
        print ("Something went wrong during the process... :(")

input_values()