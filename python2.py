# function that returns a number
def num():
    return int(input("Enter a number: "))

# calculator function
def my_calculator(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 4:
        return 4
    elif n == 5:
        return 5
    else:
        return "Number not supported"

# call calculator with num() function
result = my_calculator(num())
print(result)