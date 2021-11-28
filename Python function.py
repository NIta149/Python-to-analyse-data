#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Functions 

def Sales():
    Total_Sales = 200 *100
    print (Total_Sales)

Sales()


# In[5]:



def sales(Qty):
    Total_sales = Qty * 100
    print (Total_sales)

sales(50)


# In[6]:


def sales (Qty = 10):
    Total_sales = Qty * 100
    print (Total_sales)

sales(50)
sales ()


# In[7]:


def Sales(Qty,Prc):
    Total_Sales = Qty *Prc
    print (Total_Sales)

Sales (50,100)


# In[11]:


def sales(Prc, Qty=90):
    Total_Sales = (Qty*Prc)
    print (Total_Sales)

sales(25,90)


# In[13]:



def Sales(Qty =10,Prc =50):
    Total_Sales = Qty *Prc
    print (Total_Sales)

print (Sales ())
print (Sales(200,100))


# In[14]:


def sales(Prc= 100, Qty =50):
    Total_Sales = (Qty*Prc)
    return (Total_Sales)

x= sales (200,200)
print (x)


# In[15]:


def financials (revenue,expenses):
    """ This function is used to calculate profit and profit ratio"""
    profit = revenue -expenses
    profit_ratio = profit/revenue 
    new_financials = (profit ,profit_ratio)
    return (new_financials)

financials (1000,900)


# In[16]:



def financials (revenue,expenses):
    """ This function is used to calculate profit and profit ratio"""
    profit = revenue -expenses
    profit_ratio = profit/revenue 
    new_financials = (profit ,profit_ratio)
    return (new_financials)

x = financials (1000,900)
print ('Profit ', x[0] )
print ('Profit Ratio ', x[1] )


# In[17]:



#celsius to fahrenheit
#(0°C × 9/5) + 32 = 32°F

def convertto (deg):
    F= (deg*9/5)+32
    return (F)

temp = 38
temp= convertto (temp)
print (temp)


# In[ ]:




