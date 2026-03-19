#1
def square_generator(N):
    for i in range(1, N+1):
        yield i ** 2  # Yield the square of i

N = int(input("Enter N: "))

# Using the generator to print squares
for square in square_generator(N):
    print(square, end=" ")  
#2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i  # Yield only even numbers

n = int(input("Enter n: "))

# Print even numbers in comma-separated form
print(*even_numbers(n), sep=", ")


#3 Generator function for numbers divisible by both 3 and 4
def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter n: "))

# Print numbers divisible by 3 and 4
print(*divisible(n), sep=" ")

#4 Generator function for squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2  # Yield the square of i

a = int(input("Enter start (a): "))
b = int(input("Enter end (b): "))

# Test generator with a for loop
for sq in squares(a, b):
    print(sq)

#5 Generator function for numbers from n down to 0
def countdown(n):
    for i in range(n, -1, -1):  # Start at n, go down to 0
        yield i

n = int(input("Enter n: "))

# Print numbers in countdown
for num in countdown(n):
    print(num, end=" ")