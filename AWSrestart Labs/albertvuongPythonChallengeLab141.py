# Python Challenge Lab 141
# Display all prime numbers between 1 and 250
# Store results in a file called results.txt

'''
TODO
1. Find the prime numbers between 1 and 250 
    (1 is not a prime number)
2. Store the results in the string or list
3. Add the results to a new or existing file called results.txt
'''

# Declare variables
# List to store prime numbers, 2 is a prime number
prime = [2]
max = 250
check = False

# Iterate through numbers 3 - 250
# range goes up to, but not including the last number
for i in range(3, max + 1):
    check = False

    # inner for loop to check if number is prime or not
    # 1 is added to int(i/2) as it rounds down and for loops can't go range(2,2)
    for j in range(2, int(i/2) + 1):

# Line used for debugging         
#        k = i % j
        if i % j == 0:
            check = True
            break

    # append list if number is prime
    if check == False:
        prime.append(i)

# Line used for debugging
# print(prime)

# Create a file, results.txt, and add the prime numbers
with open('results.txt', 'w') as f:
    for i in prime:
        f.write(str(i) + '\n')