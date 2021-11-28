#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Write a program which will find factors of given number and find whether the factor is even or odd.
num=50
for i in range(1,num+1):
    rem=num%i

    if(rem==0):
        if(i%2==0):
            print("Factor is even:",i)
        else:
            print("factor is odd: ",i)

    else:
        pass



# In[4]:


#Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
my_str = "Welcome to Python"

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)


# In[5]:


#Write a program, which will find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line
values = []
for i in range(1000,3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)

print (",".join(values))


# In[6]:


#Write a program that accepts a sentence and calculate the number of letters and digits

s = "aac34520"
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])


# In[7]:


#Design a code which will find the given number is Palindrome number or not.

# change this value for a different output
my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")


# In[ ]:




