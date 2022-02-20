#Calculate the gradient of f(x,y) = x**2y - xy**2 where x,y are the inputs given by users 
# In FindGradient , I have calculated the f(x) and f(y) which I got on paper. 
# grad is a varaible which gives the gradient of the function by taking input from the user 
#first, the try part will get executed and it will take 2 inputs from user in form of Int/Float then these values will be given to the FindGradient Function
 

def FindGradient(x,y):
        fx = 2*y*x-y**2
        fy = x**2 - 2*x*y
        grad= (fx,fy)
        print("Grandient of x^2y - xy^2 at",(x,y), "are",grad)
        
try:
    print("This is a program to find the Gradient of x^2y - xy^2 ")
    x = float(input("Enter a value for x to calculate the gradient : "))
    y = float(input("Enter the value of y to calculate the gradient : "))
    FindGradient(x,y)
        
except:
    print("Please enter a valid integer or a float value" )

