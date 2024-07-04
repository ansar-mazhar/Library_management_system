# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 07:35:36 2024

@author: STAR LAPTOP
"""
#LIBRARY MANAGEMENT SYSTEM
class Library:
    
    def __init__(self,name,booklist):
        self.booklist = booklist
        self.name = name
        self.lend = {}
    def display_books(self):
        print(f"We have following books in our library: {self.name}")
        for i in self.booklist:
            print(i)
        
    def lend_book(self, user, book):
         if book in self.booklist:
            if book not in self.lend.keys():
                self.lend[book] = user
                print("Lender-Database has been updated. Now you can take your book")
            else:
               print(f"Book '{book}' is already taken by {self.lend[book]}")
         else:
            print(f"Book {book} is not available in library")
            
    def add_book(self, book):
        self.booklist.append(book)
        print("Book is successfully added")     
    def return_book(self, book):
        if book in self.lend.keys():
            del self.lend[book]
            print("Lender-Database has been updated. Book returned successfully.")
        else:
            print("This book was not borrowed from this library.")

if __name__ == "__main__":
    lib = Library("Ansar's library", ["Python", "C++", "DSA", "Life", "Tafheem Ul Quran"])
    
    while (True):
        print("Welcome to library named Ansar's library")
        print("1. Display Books ")
        print("2. Lend a book ")
        print("3. Add a book ")
        print("4. Return a book ")
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            lib.display_books()
        elif user_choice == 2:
            book = input("Enter name of book you want to lend: ")
            user = input("Enter your name: ")
            lib.lend_book(user, book)
        elif user_choice == 3:
            book = input("Enter name of book you want to add: ")
            lib.add_book(book)
        elif user_choice == 4:
            book = input("Enter the book you want to return")
            lib.return_book(book)
        else:
            print("Invalid choice ")
        user2 = ""
        print("Enter q if you want to quit: ")
        print("Enter c if you want to continue: ")
        user2 = input("Enter your choice").strip().lower()
        if user2 == "q":
                  break
        elif user2 == "c":
                 continue
        else:
                print("Invalid input!!")
                
            
                
            
            
            
            
            
            
            