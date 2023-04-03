"""
Fizz - buzz

kérj be a felhasználótól egy számot n, számolj el 1-tól n-ig,
ha egy szám osztható 3-mal írd ki "Fizz", ha 5-el "Buzz", ha
mindkettővel akkor "FizzBuzz", ha egyikkel sem akkor csak a számot

"""

n = int(input())

for fizzbuzz in range(1,n):
    if fizzbuzz % 15 == 0:
        print("Fizzbuzz")

    elif fizzbuzz % 3 == 0:
        print("Fizz")

    elif fizzbuzz % 5 == 0:
        print("Buzz")

    else:
        print(fizzbuzz)
        
