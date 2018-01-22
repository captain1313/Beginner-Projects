print('Welcome to the Distance Calculator')
print("Please enter two points that do not lie on the same vertical line")

print("First x ")
x1=int(input())

print("First y ")
y1=int(input())

print("Second x ")
x2=int(input())

print("Second y ")
y2=int(input())

def slope(x1,y1,x2,y2):
        m=(y2-y1)/(x2-x1)
        return m

if x1==x2:
    print("Slope is undefined")
elif y1==y2:
    print("Slope is 0")
elif x1!=x2 and y1!=y2:
    print ("Slope Value is: "+ str(slope(x1, y1, x2, y2)))
