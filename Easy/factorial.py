def factorial(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    else :
        return (n*factorial(n-1))



n=int(input("Enter the number : "))
print(factorial(n))
def factorial_list_recursive(numbers):
    factorial_list = []
    for num in numbers:
        factorial_list.append(factorial(num))
    return factorial_list

# Example usage:

numbers = [16, 3, 7, 2]
factorials = factorial_list_recursive(numbers)
print("Factorials of", numbers, "are:", factorials)





