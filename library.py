#!/usr/bin/env python
# coding: utf-8

# In[20]:


import sqlite3                 
from My_book import Book
#Add Book: Add a new book to the library.
#Remove Book: Remove an existing book from the library.
#Update Book: Update the details of an existing book.
#Search Book: Search for books by title, author, or genre.
#List All Books: Display all books in the library.
#Mark as Read/Unread: Update the read/unread status of a book.


# In[42]:


"""class Library:
    def __init__(self,db_name='library.db'):                        
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                author TEXT,
                                publication_year INTEGER,
                                genre TEXT,
                                status TEXT)''')
        self.conn.commit()
    def add_book(self,book):
        self.cursor.execute('insert into books(title,author,publication_year,genre,status) Values(?,?,?,?,?)',
                            (book.title,book.author,book.publication_year.book.genre,book.status))
        self.conn.commit()

    #Remove Book: Remove an existing book from the library.
    def remove_book(sel,book_id):
        self.cursor.exucute('Delete from books where book_id=')

"""


# In[52]:


import sqlite3
from book import book

class Library:
    def __init__(self, db_name='library.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                author TEXT,
                                publication_year INTEGER,
                                genre TEXT,
                                status TEXT)''')
        self.conn.commit()

    def add_book(self, book):
        self.cursor.execute("INSERT INTO books (title, author, publication_year, genre, status) VALUES (?, ?, ?, ?, ?)",
                            (book.title, book.author, book.publication_year, book.genre, book.status))
        self.conn.commit()

    def remove_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        self.conn.commit()

    def update_book(self, book_id, **kwargs):
        for key, value in kwargs.items():
            self.cursor.execute(f"UPDATE books SET {key}=? WHERE id=?", (value, book_id))
        self.conn.commit()

    def search_books(self, **kwargs):
        query = "SELECT * FROM books WHERE " + " AND ".join([f"{k}=?" for k in kwargs.keys()])
        self.cursor.execute(query, tuple(kwargs.values()))
        return self.cursor.fetchall()

    def list_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def mark_as_read(self, book_id):
        self.update_book(book_id, status='read')

    def mark_as_unread(self, book_id):
        self.update_book(book_id, status='unread')

    def __del__(self):
        self.conn.close()


# In[24]:





# In[25]:





# In[ ]:




