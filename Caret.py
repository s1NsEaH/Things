def move (y, x):
    print("\033[%d;%dH" % (y, x))
    

print("\n\n"+"="*15)
move(0,0)
input("input ur data: ")
