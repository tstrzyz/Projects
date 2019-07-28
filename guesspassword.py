import sys
tries = 3
while tries < 4:
    name = str(input("What is the  password?"))
    if name != " ":
            if name.lower() in ['password', 'Password']:
                print("Welcome back!")
                break
            else:    
                print ("That password is incorrect. You have %s login attempts remaining." % (tries))
                tries -= 1
                if tries == 0:
                    break
else: print ("Welcome back!")
    #my code is so cool ikr
        

             
    
    
