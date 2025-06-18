import sys 
if len(sys.argv) ==2:
    user_input = input("what was the parameter? ")
    if user_input == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")    
else:
    print("none")        