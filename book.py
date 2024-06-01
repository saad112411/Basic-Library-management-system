#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[37]:


class Book:
  def  __init__(self,title,author,publication_year,genre,status='Unread'):
      self.title=title
      self.author=author
      self.publication_year=publication_year
      self.genre=genre
      self.status=status


  def __repr__(self):
      return f"Book({self.title}, {self.author}, {self.publication_year}, {self.genre}, {self.status})"


# In[36]:


#book = Book('1984', 'George Orwell', 1949, 'Dystopian', 'read')
#print(repr(book))


# In[ ]:




