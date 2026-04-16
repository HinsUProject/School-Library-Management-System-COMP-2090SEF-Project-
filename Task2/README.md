# Library borrowing record using Graph & DFS

Team: CHANG Tsz-Hin, Tin Hiu-Yeung, Lau Pak-Yin

This is a self-study project of COMP2090SEF where we study aboout the application of **Graph** Data Structures and the **Depth First Search (DFS)** algorithm.

## Overview
This project demonstrates how complex, multi-connected relationships (like students borrowing multiple books) are better represented using a **Graph** rather than a simple linear list.

## User guide
1. Download the **borrowing record with graph and DFS.py** file and run it on an Integrated Development Environment(IDE) such as Thonny and Visual Code Studio.
2. Enter the "student name" and the "book name" then click the **Add Record** button to add a new record to the system.
3. Input the name of the student name that you want to search and click the **Search connections** button a get all books that were borrowed by the student.
4. Click the **Show All Records** button the show the graph of all records.

## Functions and Features
### Data Management (Graph)
* add_node(): Initializes a new student or book that does not already exist in the records.
* add_edge():Creates a mutual connection between a student and a book to show they are related in the borrowing records, allowing the system to be searched from either direction.
* get_records(): Provides a full overview of every student, book, and connection currently stored in the system's memory.
* get_related(): Return all connections of a specific student or book.
### Searching method (DFS)
* dfs(): Uses Depth First Search algorithm to search for the entire borrowing chain. It can find groups of students and books that are linked together through multiple connections.
