#!/usr/bin/env python3
"""
a function that converts a number into binary, and checks for the length binary gap
a binary gap is th zeros between two ones. if there are two, the largest gap is selected
"""
def binary_gap(integer):
    #convert the integer to binary
    to_binary = bin(integer)[2:]

    #initialize variable, one to track  the max gap and other to check current gap
    active_gap = 0
    longest_gap = 0

    #loop through ech binary character
    for b in to_binary:
        #check if digit is zero and add to the variable representing current gap
        if b == '0':
            active_gap += 1
        else:
            #if the digit is one compare current gap update the longest gap
            longest_gap = max(longest_gap, active_gap)
            #reset current gap
            active_gap = 0
    #return max gap at the end of the loop
    return longest_gap


print(binary_gap(0))