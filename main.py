
num = 1 
for num in range (1,1001) :
    if num % 3 == 0 and num % 5 == 0:
       print("Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else : 
        print(num)
        numero= num + 1