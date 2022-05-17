''' This code works by taking values from a list
    and adding them to a variable to then output
'''
#assigns a list to a variable called digit_list
digit_list = [8,3,5,1]

#multiplies each digit in the list by its place value, eg. 8 * 1000 to make 8000
#then adds together all the values to create the final number to print
final_number = digit_list[0]*1000 + digit_list[1]*100 + digit_list[2]*10 + digit_list[3]

#prints the final number
print(final_number)