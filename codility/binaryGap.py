#!/usr/bin/env python3
"""
a function that converts a number into binary, and checks for the length binary gap
a binary gap is th zeros between two ones. if there are two, the largest gap is selected
"""
#convert the integer to binary
#initialize variable, one to track  the max gap and other to check current gap
#loop through ech binary character
#check if digit is zero and add to the variable representing current gap
#if the digit is one update the longest gap to current gap
#reset current gap
#return max gap at the end of the loop