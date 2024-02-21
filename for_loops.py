import random
run = int(input("What code would you like to run 1-10: "))
# One
if run == 1:
    for L in range(1001):
        print(L)

# Two
elif run ==2:
    for Q in range(1,1000,2):
        print(Q)

# Three
elif run == 3:
    for H in range(1001):
        if H % 3 == 0:
            print(H)

# Four
elif run == 4:
    for P in range(1,1001,1):
        if P % 3 == 0:
            print(P)
        elif P % 5 == 0:
            print(P)
        else:
            continue

    

# Five
elif run == 5:
    num = int(input("Enter a number greater than 200: "))
    while num <= 200:
       if num < 200:
           num = int(input("Bigger than 200 please! Enter a new number: "))
       elif num == 200:
           num = int(input("Bigger than not equal to please! Enter a new number: "))

    for K in range(1,num):
        if K % 11 == 0:
          print(K)
        elif K % 15 == 0:
          print(K)


# Six
elif run == 6:
    word = input("Give me a word or phrase: ")
    for I in range(len(word)):
        print(word[I])


# Seven
elif run == 7:
    newWord = input("Give me a word or phrase longer than 10 characters: ")
    while len(newWord) <= 10:
        newWord = input("Try again with one longer than 10 characters: ")
    for J in range(0,len(newWord),2):
        print(newWord[J])



# Eight
elif run == 8:
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    for roll in range(1001):
        dice = random.randint(1,6)
        if dice == 1:
            one += 1
        elif dice == 2:
            two += 1
        elif dice == 3:
            three += 1
        elif dice == 4:
            four += 1
        elif dice == 5:
            five += 1
        else:
            six += 1
    print(f"The computer rolled {one} ones, {two} twos, {three} threes, {four} fours, {five} fives, and {six} sixes")


# Nine
elif run == 9:
    primemaybe = 0
    number = int(input("Enter a number: "))
    
    for prime in range(2,number+1):
        if number % prime == 0 and prime != number:
            primemaybe += 1

    if number <= 2:
        print(number, " is not a prime number")
    elif primemaybe != 0:
        print(number, " is not a prime number")
    elif primemaybe == 0:
        print(number, " is a prime number")


# Ten
#        10. Write a program that prints out the prime numbers less than 1000. (+20 points)
        
elif run == 10:
    primemaybe = True
        
    for round in range(2,1001):
        primemaybe = True
         
        for prime in range(2,round+1):
            if round % prime == 0 and prime != round:
                primemaybe = False
                break  
        if primemaybe == True:
            print(round, " is a prime number")






