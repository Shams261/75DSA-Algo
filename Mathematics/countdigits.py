def count_digits(n):
    res =0
    while n >0:
        n =n // 10
        res +=1
        
    return res

userinput = int(input("Enter the number:"))
final_result = count_digits(userinput)
print(final_result)