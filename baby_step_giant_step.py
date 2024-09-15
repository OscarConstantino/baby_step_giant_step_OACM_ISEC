from math import ceil, sqrt, floor

def show_table(tbl, name):
    print("\n--",name," table--",end="\n\n")
    print(tbl,end="\n\n")
    print("-------------------",end="\n\n")

def check_prime(p):
    if p==2 or p==3: return True
    if p%2==0 or p<2: return False
    for i in range(3, int(pow(p,0.5))+1, 2):
        if p%i==0:
            return False
    return True

def giant_step_iteration(g,p,bbstbl, mode, c = 0,h = 0, b=0):
    gstbl = {}
    for j in range(b):
        if mode == 1:
            gsv = (g**b)**j % p
        else:
            gsv = (h * pow(c, j, p)) % p
        gstbl[gsv] = j
        if gsv in bbstbl:
            show_table(gstbl, "Giant step")
            print("B: ",j)
            print("q:", b)
            print("r: ",bbstbl[gsv])
            return j * b + bbstbl[gsv]

def bsgs(g, h, p):
    B = floor(sqrt(p)) #Calculating B to determine the number of operations, p must be a prime number
    
    #Calculating g^-1 mod p which I will call nh for the further iterations
    nh = pow(g,-1,p)
    print ("NH: ",nh,end="\n\n")

    #Baby Step. Creating a dictionary with the values iterations
    bbstbl = {h*nh**i % p: i for i in range(B)}
    show_table(bbstbl, "Baby step")
    
    print("******************************************************************",end="\n\n")
    #Giant steps. Calculating the giant step value an comparing if it exitst in the baby step dictionary
    return giant_step_iteration(g=g,p=p,bbstbl=bbstbl,mode=1,b=B)

def bsgs2(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(N)}
    show_table(tbl, "Baby step")

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)
    print("Fermat Little Theorem value: ", c,end="\n\n")

    print("**********")

    # Search for an equivalence in the table. Giant step.
    return giant_step_iteration(g,p,bbstbl=tbl,mode=2,c=c,h=h,b=N)

def input_values():
    try :
        g = int(input("Insert the g value: "))
        if g < 0:
            raise ValueError()
        h = int(input("Insert the a value: "))
        if h < 0:
            raise ValueError()
        p = int(input("Insert the p value (make sure p is a prime value):"))
        if p < 0:
            raise ValueError()
        mode = int(input("Inser which mode would you like to choose, 1 for normal option or 2 you want to use Precompute Fermat's Little Theorem, type 3 if you want to verify that p is prime: "))
        print("Thanks!! Processing ...")
        if mode == 1:
            print("k: ", bsgs(g,h,p))
        elif mode == 2:
            print("k: ", bsgs2(g,h,p))
        elif mode == 3:
            if check_prime(p):
                print("The chosen p is prime...")
            else:
                print("The chose p is not a prime number :( it can not be used in this program... Make sure to choose a valid prime number.")
        else:
            raise ValueError("The mode value can only be 1 or 2")
    except ValueError:
        print ("The values must be an intefer and cannot be negative.")
    except Exception:
        print ("Something went wrong during the process... :(")

input_values()
