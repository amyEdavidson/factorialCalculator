print("Please provide a number larger than 0")
x = input()
z = 1
while not x.isdigit(): 
    print("Please provide a number larger than 0")
    x = input()
x = int(x)
while not x > 0:
    print("Please provide a number larger than 0")
    x = input()

if x > 0:
    for i in range(1,x+1): 
        z = z * i 
        y = z
        
    print ("The factorial is : ", end="") 
    print(z)
