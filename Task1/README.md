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
1. Add books by entering book detail in the text boxes in the **left panel** and click the "Add book" button.
2. Delete
3. Click the **Show All Records** button the show the graph of all records.

## Functions and Features
### Data Management (Graph)
* add_node(): Initializes a new student or book that does not already exist in the records.
* add_edge():Creates a mutual connection between a student and a book to show they are related in the borrowing records, allowing the system to be searched from either direction.
* get_records(): Provides a full overview of every student, book, and connection currently stored in the system's memory.
* get_related(): Return all connections of a specific student or book.
### Searching method (DFS)
* dfs(): Uses Depth First Search algorithm to search for the entire borrowing chain. It can find groups of students and books that are linked together through multiple connections.
