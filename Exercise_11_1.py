#!/usr/bin/env python
# coding: utf-8

# In[1]:


def make_word_list(file):
    word_list = open(file)
    list = []
    for line in word_list:
        word = line.strip()
        list += [word]
    return list


# In[2]:


wordlist = make_word_list("words.txt")


# In[3]:


def make_dictionary(list):
    word_dict = dict()
    for word in list:
        word_dict[word] = ''
    return word_dict


# In[4]:


dictlist = make_dictionary(wordlist)


# In[6]:


def check_for_string(word, dictionary):
    if word in dictionary:
        return True
    return False


# In[9]:


print(check_for_string('bike', dictlist))


# In[10]:


print(check_for_string('leleleleelel', dictlist))


# In[ ]:




