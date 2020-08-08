#Multiples of Three
#Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.

multiples_3 = [num for num in range(1,21) if num%3==0 ]
print(multiples_3)