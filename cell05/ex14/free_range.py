import sys

if len(sys.argv) != 3:
    print("none")

else:
    try:
        start = int(sys.argv[1])  
        end = int(sys.argv[2]) 
        number = list(range(start, end + 1)) 
        print(number)
    except ValueError:
        print("none")    