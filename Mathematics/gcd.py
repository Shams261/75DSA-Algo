## Eucledian Algorithm 
# def gcd(a,b):
#     while a!=b:
#         if a>b:
#             a=a-b
#         else:
#             b=b-a
#     return a 

# userInput1=(int(input("Enter the number:")))
# userInput2=(int(input("Enter the number:")))
# print(gcd(userInput1,userInput2))


## optimized Eucledian Algorithm 

def gcd(a,b):
    if b==0:
        return a 
    return gcd(b,b%a)
userInput1=(int(input("Enter the number:")))
userInput2=(int(input("Enter the number:")))
print(gcd(userInput1,userInput2))
