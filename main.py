print ("Hello, i will help you calculate the roots of a quadratic :)")

def solve1(a,b,c):
    y =((-b-(((b**2)-4*(a*c))**(1/2)))/(2*a))
    return y
def solve2(a,b,c):
    z = ((-b + (((b ** 2) - 4 * (a * c)) ** (1 / 2))) / (2 * a))
    return z

a=int(input("enter the a:"))
b=int(input("enter the b:"))
c=int(input("enter the c:"))

e=(solve1(a,b,c))
g=(solve2(a,b,c))
print("the first root is",e,"the secound root is",g,".")
print("goodbye")
exit()
