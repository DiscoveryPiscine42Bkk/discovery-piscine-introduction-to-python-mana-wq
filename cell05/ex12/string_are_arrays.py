import sys

if len(sys.argv)!= 2:
    print("none")
else: 
    text = sys.argv[1]
    count = 0

    for letter in text:
        if letter == 'z':
            print('z', end='')
            count += 1

    if count == 0:
        print("none")     
    else:
        print()       