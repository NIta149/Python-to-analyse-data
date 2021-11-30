#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = [10,20,30,40,50,60,70]


# In[2]:


list1 = [10,20,30,40,'Sam',40.5, 'A',0,60,70]


# In[3]:


len(list1)


# In[5]:


list1 = [10,20,30,[50,50,'Sam'],40,'Sam',40.5, 'A',0,60,70]
list1


# In[6]:


list1 [3]


# In[8]:


list1 [3].append(30)
list1


# In[ ]:


list = 


# In[9]:


list1 = [10,20,30,[50,50,'Sam'],40,'Sam',40.5,[20], 'A',0,60,70]
list1


# In[10]:


list1[7]


# In[11]:


print (type(list1[7]))


# In[12]:


list1 = [10,20,30,[50,50,'Sam'],40,'Sam',40.5, 'A',0,60,70]
list1


# In[13]:


list1 [3].append(50)
list1


# In[14]:


print (list1[0:3])


# In[15]:


print (list1[:5])


# In[ ]:


print (list1[:5])


# In[16]:


print (list1[5:])


# In[17]:


print (list1[5:8])


# In[18]:


list1


# In[19]:


list1[-1]


# In[20]:


list1[-3:]


# In[21]:


print (list1[-4 : -2])


# In[22]:


print (list1[-4 : ])


# In[23]:


list1


# In[ ]:


for 


# In[24]:


list1


# In[25]:


list1[:3]


# In[26]:


list1[5:7]


# In[27]:


list1[5:-2]


# In[29]:


list2 = [100,110,120]
list3 = [50,51,52]


# In[31]:


list4 =  list2+list3
print (list4 )


# In[32]:


list5 =  list2+list3+[60,60,62]
list5


# In[34]:


list2 = [100,110,120]
print (list2 * 3)


# In[35]:


print (150 in list2)


# In[36]:


print (100 in list2)


# In[ ]:


list1 = ['John','Sam','Rick', 'Jim']


# In[37]:


l1 = [10,20,30]


# In[39]:


l1[0]*3


# In[47]:


l2 = []
l1 = [10,20,30]
for i in l1:
    l2.append(i*3)
print (l2)
 


# In[48]:


list1 = ['John','Sam','Rick', 'Jim']


# In[49]:


del (list1)
list1 


# In[50]:


l2 = []
l1 = [10,20,30]
for i in l1:
    l2.append(i*3)
print (l2)


# In[51]:


list2 = [100,110,120]
print (list2 * 3)


# In[52]:


list1 = ['John','Sam','Rick', 'Jim']


# In[53]:


del(list1)


# In[54]:


print (list1)


# In[55]:


list1 = ['John','Sam','Rick', 'Jim']


# In[56]:


list1.clear()


# In[57]:


list1


# In[59]:


list1 = ['John','Sam','Rick', 'Jim']
del(list1[1])
list1


# In[60]:


del(list1[1])
list1


# In[61]:


del(list1[1])
list1


# In[62]:


del(list1[1])
list1


# In[63]:


list1 = ['John','Sam','Rick', 'Jim']
del (list1[:])
list1


# In[64]:


list1 = ['John','Sam','Rick', 'Jim']
del (list1[1:3])
list1


# In[ ]:





# In[65]:


l1=[10,20,30,40,50]

for i in l1:
    i=i*10
    print(i)


# In[66]:


list1 = ['John','Sam','Rick', 'Jim']
a = list1.pop(2)
print (a)


# In[67]:


list1


# In[69]:


list1 = ['John','Sam','Rick', 'Jim']
a = list1.remove ('John')
list1


# In[70]:


print (a)


# In[71]:


list1 = [1,2,3,4,5,6]
list1.append (7)
list1


# In[73]:


list1 = [1,2,3,4,5,6]
list1.append (7)
list1


# In[74]:


list1 = [1,2,3,4,5,6]
list1.append ('Day')
list1


# In[ ]:


list1 = [1,2,3,4,5,6]
list1.append ('Day')
list1


# In[75]:


l1 = [1,2,3,4,5,6]+[10,20,30]
l1


# In[77]:


l1 = [1,2,3,4,5,6]
l1.append([10,20,30])
l1


# In[78]:


l1 = [1,2,3,4,5,6]
l1.append((10,20,30))
l1


# In[80]:


list1 = []
for x in [1,2,3,4,5]:
    list1.append (x * 2)
print (list1)


# In[81]:


list1 = [x * 2 for x in [1,2,3,4,5]]
print (list1)


# In[82]:



for x in [1,2,3,4,5]:
    n.append (x * 2)
print (list1)


# In[83]:


list10 = [10,20,30,40]
list1 = [x * 2 for x in list10 ]
print (list1)


# In[84]:


list1


# In[85]:


list1 = [10,20,30,[50,50,'Sam'],40,'Sam',40.5, 'A',0,60,70]
list1


# In[87]:


list1[3].append(60)
list1


# In[88]:


list1[2].append(60)
list1


# In[89]:


list1 = [x * 2 for x in [1,2,3,4,5]]
print (list1)


# In[90]:


list10 = [10,20,30,40]
list1 = [x * 2 for x in list10 ]
print (list1)


# In[91]:


list1= []
list10 = [10,20,30,40]
for x in list10:
    list1.append (x * 2)
print (list1)


# In[92]:


list10 = [10,20,30,40]
list1 = [(x * 2)+2 for x in list10 ]
print (list1)


# In[93]:


list1= []
list10 = [10,20,30,40]
for x in list10:
    list1.append ((x * 2)+2)
print (list1)


# In[95]:


list1 = [1,2,3,4,5,6]
list1.extend (['A','B','C'])


# In[96]:


list1 


# In[100]:


len(list1 )


# In[101]:


list1 = [1,2,3,4,5,6]
list1.append (['A','B','C'])
list1


# In[ ]:





# In[ ]:





# In[98]:


list1 = [1,2,3,4,5,6]
list1.insert (2, 'M')
list1


# In[99]:


list1.insert (2, 'M')
list1


# In[ ]:


list1 = [1,2,3,4,5,6]
list1.extend (['A','B','C'])


# In[ ]:


list1= []
list10 = [10,20,30,40]
for x in list10:
    list1.append ((x * 2)+2)
print (list1)


# In[105]:


list1 = [1,2,3,4,5,6]
list1.insert (2, 'M')
list1


# In[ ]:





# In[ ]:





# In[ ]:





# In[106]:


list1.insert (4, 'M')
list1


# In[111]:


list1 = [1,2,3,4,5,6]
for i in (range (2,8,2)):
    list1.insert (i, 'M')
list1


# In[112]:


list1.insert (2, ['P','Q','R'])
print (list1)


# In[ ]:


list1 = ['Rick','Jim','Mark','Jack','Ken']
list2 = sorted (list1)
print (list1)
print (list2)


# In[115]:


list1 = [1,2,3,4,5,6]
list1.insert (2, 5.5**2)
list1


# In[117]:


list1 = ['Rick','Jim','Mark','Jack','Ken']
list2 = sorted (list1)
list2


# In[118]:


print (list1[::-1])


# In[119]:


print (list1[4:2:-1])


# In[122]:


print (list1[4:0:-2])


# In[123]:


list1 = [1,2,3,4,5,6]
for i in (range (2,8,2)):
    print (i)
    list1.insert (i, 'M')
list1


# In[124]:


list1 = [50,10,30,60,40,50,10,5,70]
list2 = sorted (list1)
list2


# In[125]:


list1 = [50,10,30,60,40,50,10,5,70]
list2 = sorted (list1, reverse=True)
list2


# In[126]:


colors = ['Red', 'Blue', 'Green', 'Black', 'White']


# In[129]:


second_col = colors[1]
second_col


# In[131]:


newest_col = colors[-1]
newest_col


# In[132]:


colors


# In[133]:


colors[2]= 'Yellow'
colors


# In[135]:


colors


# In[136]:


num_colors = len(colors)
print("We have " + str(num_colors) + " colors.")


# In[141]:


x = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
min(x)


# In[142]:


max(x)


# In[144]:


sum(x)


# In[145]:


squr = [x**2 for x in range(1, 11)]
print (squr)


# In[146]:


colors


# In[149]:


colors.upper


# In[153]:


colors = ['Red', 'Blue', 'Green', 'Black', 'White']
upper_cols = []
for cols in colors:
    upper_cols.append(cols.upper())
upper_cols


# In[154]:


colors = ['Red', 'Blue', 'Green', 'Black', 'White']
upper_cols = []
for cols in colors:
    upper_cols.append(cols.lower())
upper_cols


# In[163]:


colors = ['Red', 'Blue', 'Green', 'Black', 'White']
m= []
for col in colors:
    m.append(col.upper())
m


# In[164]:


print (m)
n=[]
for col in m:
    n.append(col.title())
n


# In[165]:


import datetime
now = datetime.datetime.now()
now 


# In[ ]:


7
77
777


# In[ ]:


8
88
888


# In[ ]:


a = 8
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)


# In[178]:


a = 8
n1 = int( "%s" % a )
print (n1)
n2 = int( "%s%s" % (a,a) )
print (n2)


# In[167]:


a = str(8)
n1 = int( "%s" % a )
n1


# In[168]:


n2 = int( "%s%s" % (a,a) )
n2


# In[169]:


n3 = int( "%s%s%s" % (a,a,a) )
n3


# In[170]:


n1


# In[172]:


n2 =a+a
n2


# In[173]:


n3 =a+a+a
n3


# In[174]:


int (n1)+int(n2)+int(n3)


# In[ ]:


for 


# In[179]:


n1 = str(8)
n1


# In[180]:


n2 = str(8)*2
n2


# In[181]:


n3 = str(8)*3
n3


# In[183]:


rows=6
for num in range(rows):
    print(num,end="")


# In[ ]:


pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)


# In[186]:


r = 7
import math 
p = math.pi 
v = (4/3) *p*r **3
v


# In[191]:


print (math.)


# In[ ]:





# In[ ]:





# In[ ]:


a=8
b()
for i in the range (1,3):
b = str(a)**i
print (b)


# In[187]:


dir (math)


# In[193]:


math.log(10)


# In[202]:


a=8
for i in ( range (1,3)):
    b += int(str(a)*i)
print (b)


# In[205]:


rows = 6

for num in range(rows):

    for i in range(num):

        print(num, end="")

    print("")


# In[221]:


def list_count_4(nums):
    count= 0
    for num in nums:
        if num == 4:
            count +=1
    return count


# In[222]:


list_count_4([1, 4, 6, 7, 4])


# In[223]:


print(list_count_4([1, 4, 6, 4, 7, 4]))


# In[225]:


def is_vowel(m5):
    all_vowels = 'aeiou'
    return m5 in all_vowels


# In[226]:


print(is_vowel('c'))
print(is_vowel('e'))


# In[227]:


all_vowels = 'aeiou'
print ('e' in all_vowels)


# In[228]:


all_vowels = 'aeiou'
print ('p' in all_vowels)


# In[230]:


def is_vowel(m5):
    all_vowels = ['a','e','i','o','u']
    return m5 in all_vowels


# In[231]:


print(is_vowel('c'))
print(is_vowel('e'))


# In[232]:


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


# In[233]:


my_str = "Welcome to Python"


# In[235]:


words = my_str.split()
words 


# In[238]:


print("The sorted words are:")
for word in words:
    print(word)


# In[239]:


words = my_str.split()


# In[241]:


x = words.sort()
print (x)


# In[ ]:


values = []
for i in range(1000,3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)

print (",".join(values))


# In[243]:


i = 2426


# In[244]:


s= str(i)
s


# In[251]:


int (s[0])%2


# In[1]:


#Write a Python program to sum all the items in a list.


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers


print(sum_list([1,2,-8]))


# In[2]:


#Write a Python program to multiplies all the items in a list


def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot



print(multiply_list([1,2,-8]))


# In[3]:


#Write a Python program to get the largest number from a list. 

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max



print(max_num_in_list([1, 2, -8, 0]))


# In[4]:


#Write a Python program to get the smallest number from a list.

def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([1, 2, -8, 0]))


# In[5]:



#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.  

def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))


# In[6]:


#Parameters for the sorted() function

x = [2, 8, 1, 4, 6, 3, 7] 
  
print ("Sorted List returned :"), 
print (sorted(x))


# In[7]:



print ("\nReverse sort :"), 
print (sorted(x, reverse = True))


# In[8]:


# Dictionary
x = {'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6}
print (sorted(x))


# In[9]:


# Set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print (sorted(x))
  


# In[10]:


# Frozen Set
x = frozenset(('q', 'w', 'e', 'r', 't', 'y'))
print (sorted(x))


# In[11]:


#sort based on length of string 

L = ["cccc", "b", "dd", "aaa"]
  
print ("Normal sort :", sorted(L))
  
print ("Sort with len :", sorted(L, key = len))


# In[12]:


#sort based on user defined function  


def func(x):
    return x % 7
  
L = [15, 3, 11, 7]
  
print ("Normal sort:", sorted(L))
print ("Sorted with key:", sorted (L, key = func))


# In[13]:


#Write a Python program to remove duplicates from a list.

a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)


# In[14]:


#Write a Python program to check a list is empty or not.

l = []
if not l:
  print("List is empty")


# In[15]:


#Write a Python program to clone or copy a list.


original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)


# In[16]:


#Alternate Answer
original_list = [10, 22, 44, 23, 4]
new_list = original_list.copy()
print(original_list)
print(new_list)


# In[17]:


#Write a Python program to find the list of words that are longer than n from a given list of words.

def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len



print(long_words(3, "The quick brown fox jumps over the lazy dog"))


# In[19]:


#Write a Python function that takes two lists and returns True if they have at least one common member

def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
     return result


print(common_data([1,2,3,4,5], [5,6,7,8,9]))

print(common_data([1,2,3,4,5], [6,7,8,9]))


# In[ ]:




