#Find the prime number
#Prime number is the number divisible by that number and 1

number = int(input("Please enter a number greater than 2: "))

is_prime_number = True

for n in range(2, int(number/2)+1):
    if number%n == 0:
        is_prime_number = False
        break

if is_prime_number:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")