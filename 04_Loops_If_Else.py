#!/usr/bin/env python
# coding: utf-8

# 1 : Take a variable x and print "Even" if the number is divisible by 2, otherwise print "Odd".

# In[105]:


x= 9

# check if number is divisible by 2
if(x%2==0):
    print("Even")
else:
    print("Odd")


# 2 : Take a variable y and print "Grade A" if y is greater than 90, "Grade B" if y is greater than 60 but less than or equal to 90 and "Grade F" Otherwise.

# In[9]:


y=90

if(y>90):
    print("Grade A")
elif(y>60):
    print("Grade B")
else:
    print("Grade F")


# In[101]:


list = [10, 20, 30, 40, 50]

# reverse list
new_list = reversed(list)

# iterate reversed list
for item in new_list:
    
    print(item, end=" ")


# In[53]:


n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i, 0, -1):
        print(j,end=' ')
    print()


# In[18]:


numbers = [12, 75, 150, 180, 145, 525, 50]

# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
        
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)


# In[55]:


# first two numbers
num1 = 0
num2 =  1

print("Fibonacci sequence:")
# run loop 10 times
for i in range(10):
    
    # print next number of a series
    print(num1, end="  ")
    
    # add last two numbers to get next number
    res = num1 + num2
    
  # update values
    num1 = num2
    num2 = res


# In[46]:


num = 6
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    
    # run loop 5 times
    for i in range(1, num + 1):
        
        # multiply factorial by current number
        factorial = factorial * i
        
    print("The factorial of", num, "is", factorial)


# In[70]:


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for item in my_list:
    if item%20 == 0:
        print(item, end=" ")


# In[75]:


input_number = 6
cube = 1

for i in range(cube, input_number+1):
    cube = i*i*i
    

    print('Current number is :', i, 'and the cube is', cube)



# In[91]:


rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

