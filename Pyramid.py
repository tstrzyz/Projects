def pyramid(base):
    
    
    n = int(base)
    space = 40
    top = 0
    top = int(top)
    
    if (n % 2 == 0):
        while top < n:
            if top == n:
                print ("*" *n) 
            else:
                    top +=1
                    print(" "*space + "*"*top)
                    space -=1
    else:
        while top < n:
            if top == n:
                print ("*" *n) 
            else:
                        top = top + 1
                        print(" "*space + "*"*top)
                        top = top + 1
                        space = space - 1

input = input("Base for triangle:")
pyramid(input)