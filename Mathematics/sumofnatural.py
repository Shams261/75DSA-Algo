def sum_natural_number(n):
    return n*(n+1)//2

user_input = int(input("Enter the number"))
final_result = sum_natural_number(user_input)
print(final_result)