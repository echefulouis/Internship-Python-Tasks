# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

#It would be nice to keep track of both the number of fruits and other items in the basket.

#Use this environment below to try out this second part
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit,num in basket_items.items():
#if the key is in the list of fruits, add to fruit_count.
    if fruit in fruits:
        fruit_count+=1
#if the key is not in the list, then add to the not_fruit_count
    elif fruit not in fruits:
        not_fruit_count+=1

print(fruit_count, not_fruit_count)