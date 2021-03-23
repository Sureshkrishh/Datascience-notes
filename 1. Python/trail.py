#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ud_sum():
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    z = x+y
    print(z)

def ud_sub():
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    if x>y:
        z = x-y
        print(z)
    else:
        z = y-x
        print(z)
    
if __name__ == '__main__':
    ud_sum()
if __name__ == '__main__':
    ud_sub()


# In[ ]:




