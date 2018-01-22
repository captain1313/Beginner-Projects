def pyth(s1, s2):
    s3=((s1**2)+(s2**2))**.5
    return s3

print("All values must be positive whole numbers")
print("Enter length of side 1")
s1=int(input())
print("Enter length of side 2")
s2=int(input())

print("side 1 is "+str(s1))
print(("side 2 is "+str(s2)))
if s1 < 0 or s2 < 0:
    print("Invalid Input")
if s1 == 0 or s2 == 0:
    print("Invalid Input")
else:
    pyth(s1,s2)
    print("side 3 is "+str(pyth(s1,s2)))


