import sys
args = sys.argv[1:]
if len(args) == 0:
    print("none")
else:
    print(f"parameter: {len(args)}") 
    for arg in args:
        print(f"{arg}: {len(arg)}")