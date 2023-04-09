#Random number guess game
import math
import random
upper=int(input("Enter upper range"))
lower=int(input("Enter lower range"))

y=random.randint(lower,upper)
count=0
while count<math.log(upper-lower+1,2):
    count+=1
    x=int(input("Guess"))
    if x==y:
        print("Congratulations, you guessed in", count,"try")
        break
    elif x>y:
        print("You guessed too high")
    elif x<y:
        print("You guessedtoo low")
if count>=math.log(upper-lower+1,2):
    print("The number is",y)