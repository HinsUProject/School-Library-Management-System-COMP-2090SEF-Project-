# Library borrowing record using Graph & DFS

Team: CHANG Tsz-Hin, Tin Hiu-Yeung, Lau Pak-Yin

This is a self-study project of COMP2090SEF where we study aboout the application of **Graph** Data Structures and the **Depth First Search (DFS)** algorithm.

## Overview
This project demonstrates how complex, multi-connected relationships (like students borrowing multiple books) are better represented using a **Graph** rather than a simple linear list.

## Functions and Features
### Data Management (Graph)
add_node(): Initializes a new student or book that does not already exist in the records.
add_edge():Creates a mutual connection between a student and a book to show they are related in the borrowing records,   allowing the system to be searched from either direction.
