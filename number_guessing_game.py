import random
boom=random.randint(1,100)

guess=int(input("guess the number between 1 to 100🤔:"))
counter=1

while guess!=boom:
    if guess<boom:
        print("wrong guess higher👎")
    else:
        print("wrong guess lower👎")    

    guess=int(input("guess the number🤔:"))     
    counter+=1
else:
        print("correct guess👊")   
        print("attempts:",counter)
 



