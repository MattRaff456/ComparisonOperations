def find_largest(numbers):
    # Start with first number as the largest
    largest = numbers[0]

    #Loop through or iterate through the rest of the numbers
    for num in numbers[1:]:
        #Compare each number with the largest so far
        if num > largest:
            #If the number is greater, update the largest
            largest = num

    return largest

def find_smallest(numbers): #Start witht he first number as the smallest
    smallest = numbers[0]
    #Loop through the rest of the numbers
    for num in numbers[1:]:
        #Compare each number with the smallest so far
        if num < smallest:
            #If it's smaller, update thee smallest
            smallest = num
    return smallest

numbers = [1, 10, 30, 12, 0]

largest = find_largest(numbers)
smallest = find_smallest(numbers)

print("The largest number is " + str(largest) + ".")
print("The smallest number is " + str(smallest) + ".")