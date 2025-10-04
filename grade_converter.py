# FILE NAME - grade_converter.py

# NAME: Josh Fielding
# DATE: 10/4/25
# BRIEF DESCRIPTION: Convert a percentage grade to a letter grade based on a table 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Grade Converter =====")

grade = int(input("Enter a numerical grade (1-100): "))

if grade < 65:
   print("F")
if 65 <= grade < 70:
   print("D")
if 70 <= grade < 80:
   print("C")
if 80 <= grade < 90:
   print("B")
if 90 <= grade <= 100:
   print("A")
if grade > 100:
   print("A+")

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

Make sure to NOT put the '=' symbol next to the greater than and less than symbols in 'if grade < 65:' and 'if grade > 100'
because it will overlap. When you type 65 or 100, you'll print two letters instead of one.





'''
