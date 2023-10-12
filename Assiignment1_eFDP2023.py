#!/usr/bin/env python
# coding: utf-8

# # Assignment-1
# 

# ## Assignment 1: Python Basics

# ### Task 1: Factorial Calculator: Write a Python program that calculates the factorial of a given number.

# In[2]:


def factorial_of (n) :
    
    n = given_number

    fact = 1
    if n == int(abs(n)) :
        for i in range (n) :
            fact = n*fact
            n = n-1
        return (fact)
    else:
        return ("not possible")

given_number = 5

a=factorial_of (given_number)
print(f" Factorial of {given_number} is {a}.")
list("isha")
list(range(0,10))


# ### Task 2: Sum and Average:Create a function that takes a list of numbers as input and returns the sum and average of those numbers.

# In[58]:



def sum_avg_of (l) :
    sum=0
    for i in range (len(l)):
        sum = sum + l[i]

    avg = sum/len(l)
    return (sum,avg)


given_list = [0,1,2,3,4,5,6,7,8]

a=sum_avg_of (given_list)  
print(f" Sum and Average of a given List is {a[0]} and  {a[1]} respectively.")


# In[2]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get user input
num = int(input("Enter a non-negative integer: "))

# Check if the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")


# In[3]:


def calculate_sum_and_average(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return total_sum, average


# In[ ]:




