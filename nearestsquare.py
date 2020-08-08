#Nearest Square
#Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

#For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40

# write your while loop here
while True:
    num=0
    for i in range(1,limit+1):
        if (i*i) in range(1,limit+1):
            num=i
    break

nearest_square=num*num

print(nearest_square)