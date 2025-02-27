def main():
    is_prime(7)
    is_prime(10)
    is_prime(2)


def is_prime(num):
    counter = 0
    for i in range(1,num+1):
        if num % i == 0:
            counter += 1
            
    if counter == 2:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


main()