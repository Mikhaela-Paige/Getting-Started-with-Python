"""
Check whether the given number is prime.

Argument(s): n (integer)
Returns: None
"""
# Defining a function that will check if the given number is prime
def isAPrime(n):
    for num in range(2, n):
        if(n % num == 0):
            print("Nope! Not a prime.")
            break
    else:
        print("Yay! It's a prime!")

if __name__ == "__main__":
    while True:
        N = input("Enter an integer (type 'exit' or 'quit' to close the program): ")
        if N == 'exit' or N == 'quit':
            break
        else:
            N = int(N)
            isAPrime(N)
