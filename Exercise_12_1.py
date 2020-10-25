#!/usr/bin/env python
# coding: utf-8

# In[56]:


def most_frequent(string):
    d = {}
    for letter in string:
        d[letter] = 1 + d.get(letter, 0)
  
    
    letters = []
    
    for letter, num in d.items():
        letters += [(num, letter)]
    letters.sort(reverse = True)
    
    for num, letter in letters:
        print(letter, num)


# In[57]:


print(most_frequent('football'))


# In[ ]:




