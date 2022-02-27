import random#library for random numbers(no need fr pip)

def main():#defines function
    while True:#infinite loop
        x = random.randint(1,100)#chooses random number from 1 to 100
        y = random.randint(1,100)# same as x
        p = x/y#devides x by y
        if (p).is_integer()==True:#checks if p (x/y) is a whole number
            print(str(x)+"/"+str(y)+"="+str(p))#will print a random num1/random num2 = the equation
            break#stops the loop
        else:#if there isn't a whole number
            print(str(x)+"/"+str(y)+"="+str(p))#will print a random num1/random num2 = the equation

main()#calls function
