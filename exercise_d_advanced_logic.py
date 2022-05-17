# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_number = [x for x in numbers if x % 2 == 0]
print(even_number) 

# 2. Print the difference between the largest and smallest value:
largest = max(numbers)
print(largest)
smallest = min(numbers)
print(smallest)
difference = (largest) - (smallest)
print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
for x in numbers:
    if ((numbers[x] == 2) and (numbers[x+1] == 2)):
        print(True)
    else:
        print(False) 

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total_sum = 0
add = True
for x in numbers:
    while add:
        if numbers != 6:
            total_sum += x
            break
        else:
            add = False
    while not add:
        if x != 7:
            break
        else:
            add = True
            break
print(total_sum)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
total_sum_13 = 0
x = 0
while x <len(numbers):
    if numbers[x] == 13:
        x += 2
        continue
    total_sum_13 += numbers[x]
    x += 1
print(total_sum_13)