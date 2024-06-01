#!/usr/bin/env python
# coding: utf-8

# In[8]:


from library import Library
from book import Book

def main():
    library = Library()

    while True:
        print("\nPersonal Library Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Update Book")
        print("4. Search Book")
        print("5. List All Books")
        print("6. Mark as Read")
        print("7. Mark as Unread")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            publication_year = input("Enter publication year: ")
            genre = input("Enter genre: ")
            book = Book(title, author, publication_year, genre)
            library.add_book(book)
            print("Book added successfully.")
        
        elif choice == '2':
            book_id = int(input("Enter book ID to remove: "))
            library.remove_book(book_id)
            print("Book removed successfully.")
        
        elif choice == '3':
            book_id = int(input("Enter book ID to update: "))
            print("Enter new details (leave blank to keep current value):")
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            publication_year = input("Enter new publication year: ")
            genre = input("Enter new genre: ")
            status = input("Enter new status (read/unread): ")
            
            updates = {k: v for k, v in 
                       {'title': title, 'author': author, 'publication_year': publication_year, 'genre': genre, 'status': status}.items() 
                       if v}
            library.update_book(book_id, **updates)
            print("Book updated successfully.")
        
        elif choice == '4':
            search_field = input("Search by (title/author/genre): ").lower()
            search_value = input(f"Enter {search_field}: ")
            results = library.search_books(**{search_field: search_value})
            for row in results:
                print(row)
        
        elif choice == '5':
            books = library.list_books()
            for book in books:
                print(book)
        
        elif choice == '6':
            book_id = int(input("Enter book ID to mark as read: "))
            library.mark_as_read(book_id)
            print("Book marked as read.")
        
        elif choice == '7':
            book_id = int(input("Enter book ID to mark as unread: "))
            library.mark_as_unread(book_id)
            print("Book marked as unread.")
        
        elif choice == '8':
            break
        
        else:
            print("Invalid choice. Please try again.")

#if __name__ == "__main__":
  #  main()


# In[ ]:




