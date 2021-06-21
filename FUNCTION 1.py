#A function to check whether a number is in a given range of numbers.

def range_test(n):
    if n in range(1,10):      
        print("number is in range")      #if the selected number is between 1 and 10, the function will let us know   
    else:
        print("number is not in range")       #if the selected number is not between 1 and 10, the function will let us know

print(range_test(6))