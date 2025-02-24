def isPal(n):
    rev =0
    temp =n
    while temp !=0:
        last_digit = temp % 10
        rev  = rev * 10 + last_digit
        temp = temp // 10
    return rev ==n

user = int(input("Enter the number to check:"))
print(isPal(user))