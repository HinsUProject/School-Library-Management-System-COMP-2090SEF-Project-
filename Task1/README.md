# Library-management-system
Team: CHANG Tsz-Hin, Tin Hiu-Yeung, Lau Pak-Yin

This is a group project of COMP2090SEF where we build a library management system using basic Object-Oriented Programming (OOP) concepts.

## Overview
The Library Management System is an application designed to manage book inventories and track student borrowing with user-friendly interface. The system uses a modular structure to keep the data logic separate from the visual interface.

## Introduction video
Link to our project introduction video: https://www.youtube.com/watch?v=xWY8BLdKbAw

## User guide
### How to run
1. Download **ALL FILES (main_program.py, interface.py, library_system.py, booklist.txt, Borrowlog.txt)** and put them in the same folder.
2. Run the **main_program.py** on Integrated Development Environment(IDE) such as Thonny and Visual Code Studio.
### How to use
1. Add books by entering book details in the text boxes in the **left panel** and click the "Add book" button.
2. Delete a book by clicking the "Delete" button next to the book.
3. Add a borrow record, by entering the BID and SID and click the "Borrow book" button.
4. Add a return record, by entering the BID and SID and click the "Return book" button.

## Functions and Features
### Book Inventory System
* Live Status: Displays a real-time count of total, available, and borrowed books.
* Auto-Saving: All changes are automatically saved to booklist.txt.
### Borrow/Return System
History Log: Saves every borrow/return records in Borrowlog.txt and display in the application.
