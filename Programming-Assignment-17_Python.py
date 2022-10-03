#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python 3 program to find the sum of numbers
# divisible by M in the given range

# Function to find the sum of numbers
# divisible by M in the given range
def sumDivisibles(A, B, M):

	# Variable to store the sum
	sum = 0

	# Running a loop from A to B and check
	# if a number is divisible by i.
	for i in range(A, B + 1):

		# If the number is divisible,
		# then add it to sum
		if (i % M == 0):
			sum += i

	# Return the sum
	return sum

# Driver code
if __name__=="__main__":
	
	# A and B define the range
	# M is the dividend
	A = 6
	B = 15
	M = 3

	# Printing the result
	print(sumDivisibles(A, B, M))
	


# In[6]:


# definition  

# inequality function 

def check(s):

    regex=eval(s)

    if regex:

        return True

    else:
        return False 

# printing result 

print(check("2 < 7 < 15"))

print(check("30 > 45 > 21 > 9"))

print(check("4 < 7 < 8< 12 > 2"))


# In[8]:


# Function to Replace each vowel in
# the string with a specified character
def replaceVowelsWithK(test_str, K):

	# string of vowels
	vowels = 'AEIOUaeiou'

	# iterating to check vowels in string
	for ele in vowels:

		# replacing vowel with the specified character
		test_str = test_str.replace(ele, K)

	return test_str



# Driver Code
# input string
input_str = "Medha Vashisth"

# specified character
K = "#"

# printing input
print("Given String:", input_str)
print("Given Specified Character:", K)

# printing output
print("After replacing vowels with the specified character:",
	replaceVowelsWithK(input_str, K))


# In[9]:


# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# In[10]:


# Python3 program to find
# hamming distance b/w two
# string

# Function to calculate
# Hamming distance
def hammingDist(str1, str2):
	i = 0
	count = 0

	while(i < len(str1)):
		if(str1[i] != str2[i]):
			count += 1
		i += 1
	return count

# Driver code
str1 = "geekspractice"
str2 = "nerdspractise"

# function call
print(hammingDist(str1, str2))

# This code is contributed by avanitrachhadiya2155


# In[ ]:




