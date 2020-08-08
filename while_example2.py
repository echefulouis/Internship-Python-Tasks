#Count By Check
#Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num, and calculate break_num the way you did in the last quiz.

#Now in addition, address what would happen if someone gives a start_num that is greater than end_num. If this is the case, set result to  Otherwise, set result to the value of break_num.


start_num = int(input('Enter Start number: '))
end_num = int(input('Enter End Number:: '))
count_by = int(input('Enter Count Number: '))

break_num = int(input('Enter break number: '))
while True:
    if start_num <= end_num:
        for i in range(start_num, end_num + 1, count_by):
            choice = input('do you want to change break number (y/n): ')
            if choice.lower() == 'y':
                break_num = int(input('Enter Number: '))
                if break_num < i:
                    break
            elif choice.lower() == 'n':
                continue
        break
    elif start_num >= end_num:
        print("Oops! Looks like your start value is greater than the end value. Please try again.")
    else:
        result=break_num



# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num



print(result)