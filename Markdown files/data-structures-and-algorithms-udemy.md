# Mastering Data Structures & Algorithms using C and C++

## What You Will Learn

- Learn various Popular Data Structures and their Algorithms.
- Develop your Analytical skills on Data Structure and use then efficiently.
- Learn Recursive Algorithms on Data Structures
- Learn about various Sorting Algorithms
- Implementation of Data Structures using C and C++

---

## Section 1: Before we Start

### Instructor's Note
Learn data structures and algorithms with hands-on coding, whiteboard explanations, a PDF for the program, while practicing time and space analysis and asymptotic notations like big o, omega, and theta.

### Introduction

## Section 2: Essential C and C++ Concepts

### Arrays Basics

### Practice : Arrays Basics
Explore arrays in C and C++, create and initialize arrays, access elements by index, and practice with for loops and for each loops to understand memory usage and zero initialization.

### Structures

### Practice : Structures

### Pointers

### Practice : Pointers
Explore pointers in c and c++, including declaration, address-of, and dereferencing. Demonstrate heap allocation with malloc and new, and deallocation with free and delete; pointer sizes on 64-bit systems.

### Reference in C++

### Practice : Reference

### Pointer to Structure
Access and modify a structure's members using a pointer and the arrow operator. Allocate a structure on the heap with malloc and cast, then set its length and breadth.

### Practice : Pointer to Structure
Demonstrate pointers to a structure by accessing length and breadth with dot and arrow operators. Note heap allocation with malloc and new, and printing with printf or cout.

### Functions
Explore modular programming with functions, including prototypes, declarations, and definitions, and learn about actual versus formal parameters and pass by value, address, and reference.

### Practice : Functions
Learn to implement and use functions in C and C++, including creating an add function that takes two integers, computes a sum, and demonstrates parameter passing and return values.

### Parameter Passing Methods
Explore parameter passing methods in C and C++: pass by value, pass by address with pointers, and pass by reference in C++ with a swap example.

### Practice : Parameter Passing Methods

### Array as Parameter
Learn how arrays are passed as parameters in C and C++ by address. See how a function can modify original array and return array via a pointer allocated on heap.

### Practice : Array as Parameter
Practice array as parameter: learn pass by address, why you pass size, and how pointers and for loops access elements. See memory returns by creating and returning a heap-allocated array.

### Structure as Parameter
Explore passing a structure as a parameter in C and C++. Compare call by value, call by reference, and call by address with rectangle and area calculation, including array handling.

### Practice : Structure as Parameter

### Structures and Functions (Must Watch)

### Converting a C program to a C++ class (Must Watch)
Convert a C program to C++ by turning a rectangle struct into a class with private data and public constructors and methods, enabling object initialization and area computation.

### Practice : Monolithic Program
Demonstrates the monolithic programming style by building a simple C/C++ program that reads length and breadth and computes area and perimeter of a rectangle.

### Practice : Modular Program
Break a monolithic program into modular, procedural components by creating area and perimeter functions that take length and breadth as parameters, return results, and let main handle user interaction.

### Practice : Structure and Functions

### Practice : Object-Oriented Program

### C++ Class and Constructor

### Practice : C++ Class
Demonstrate a C++ rectangle class with private length and breadth, including default and parameterized constructors, area and perimeter methods, mutator and accessor functions, and a destructor.

### Template classes
Explore how template classes enable a single arithmetic class to operate over any data type, performing add and subtract with int, float, or double.

### Practice : Template Class
Convert a concrete arithmetic class into a generic template class in C++, using this pointer and scope resolution to implement template methods, enabling support for int, float, and char types.

## Section 3: Required Setup for Programming

### Online C and C++ compiler

### Setup CodeBlocks and Settings
Install CodeBlocks with MinGW, then create a console C++ project, edit main.cpp, build and run to see a hello world program.

### Setup Dev-C++ and Settings
Learn to download and install Dev-C++, set up MinGW, enable debugging with -G, enable C++11 with -std=c++11, then create a console project and run a Hello World program.

### Debugging using Dev-C++

### Debugging using CodeBlocks
Master using the code blocks debugger to trace a C++ program line by line, set breakpoints and watches, and verify the sum of array elements.

### Setup Visual Studio

### Debugging using Visual Studio

### Setup Xcode

## Section 4: Introduction

### Introduction
Learn What are Data Structures. Comparing 1. Data Structure 2. Database 3. Datawarehouse 4. Big Data

### Stack vs Heap Memory
Learn How program uses Main Memory. How program uses sections of Memory

### Stack vs Heap.  Continued...
Learn How function uses Stack, how memory is allocated when the function is called. Learn how Heap is used with the help of Pointers

### Physical vs Logical Data Structures
Difference between Physical and Logical Data Structures Physical : Array and Linked List Logical : Stack,Queues, Trees, Graphs, Hashtables

### ADT
Learn what does it mean by Abstract Datatypes

### Time and Space Complexity
Learn How to Analyse Time and Space of any Algorithm on Data Structures, based on working of Algorithm

### Time and Space Complexity from Code
Learn How to Analyse based on Code of Algorithm

## Section 5: Recursion

### How Recursion Works ( Tracing )
Learn how to trace a Recursion

### Generalising Recursion
General form of Recursion and its phases 1. Ascending Phase 2. Descending Phase

### How Recursion uses Stack
Learn how Recursion uses Stack

### Recurrence Relation - Time Complexity of Recursion
Learn how to find the Time complexity of Recursion using Recurrence Relation

### Lets Code Recursion
Explore recursion in C by implementing a tail recursive function and comparing it with head recursion, observing stack usage, debugging with breakpoints, and printing behavior on return.

### Static and Global Variables in Recursion
Learn how Static and Global variables are used in Recursion

### Let's Code Static and Global in Recursion

### Tail Recursion
Learn What does it mean by Tail Recursion, a recursion processing at calling time

### Head Recursion
Learn what does it mean by Head Recursion, a recursion processing at returning time

### Tree Recursion
Learn Tree Recursion, a Recursion calling itself more than one time

### Let's Code Tree Recursion

### Indirect Recursion
Learn Indirect Recursion. two or more functions calling each other recursively.

### Let's Code Indirect Recursion

### Nested Recursion
Learn Nested Recursion. a Function call is passed as parameter to itself.

### Let's Code Nested Recursion

### Sum of Natural Number using Recursion
Finding Sum of first n natural numbers using Recursion and Iteration

### Let's Code Sum of N using Recursion

### Factorial using Recursion
Finding Factorial using Recursion.

### Let's Code Factorial using Recursion

### Power using Recursion
Finding Power using Recursion and computing using less number of multiplications

### Let's Code Power Recursion

### Taylor Series using Recursion
Recursive function for Taylor Series using Static variables

### Let's Code Taylor Series using Recursion
Code a recursive Taylor series for e^x in C/C++, using p and f to manage powers and factorials. Show improved accuracy with more terms and validate against a calculator.

### Taylor Series using Horner's Rule
Apply Horner's Rule to reduce number of multiplications in Taylor Series.

### Let's Code Taylor Series Horner's Rule - Recursion
Implement a recursive Taylor series for e^x using Horner's rule in C and C++. Handle double precision and avoid integer division with typecasting, and verify results by printing the output.

### Let's Code Taylor Series Iterative

### Fibonacci Series using Recursion - Memoization
Learn about Fibonacci Series. 1. Iterative method for Fibonacci Series. 2. Recursive Method. 3. Using Memoization

### Let's Code Fibonacci

### nCr using Recursion
Learn how to devise a Recursive function for nCr formula using Pascals Triangle

### Let's Code nCr using Recursion
implement factorial-based and recursive nCr calculations in c and c++, building a factorial function, a nonrecursive nCr, and a recursive nCr with integer results.

### Tower of Hanoi Problem
Devising a Recursive function for Tower of Hanoi

### Let's Code Tower of Hanoi

### Recursion

### Quiz 1 Solutions

## Section 6: Arrays Representations

### Introduction to Array
1. What is an Array 2. Declaring and Initialising Array 3. Accessing Elements of an Array

### Declarations of Array

### Demo - Array Declaration

### Static vs Dynamic Arrays
Learn how to create Array in Stack and Heap.

### Demo - Static vs Dynamic Array

### How to Increase Array Size
How to change Size of an Array

### Demo - Increasing Array Size
This demo shows increasing a heap array by allocating a larger block with malloc, copying values from p to q, freeing p, and reassigning p to q with q null.

### 2D Arrays
Learn various methods of creating 2D Array

### Demo - 2D Array
Explore three ways to create two-dimensional arrays in C: stack-allocated 3x4 arrays, heap-allocated rows via an array of pointers, and a double-pointer approach with malloc, including printing and garbage values.

### Array Representation by Compiler
How Compiler manage Arrays, How compilers use Relative addresses

### Row Major Formula for 2D Arrays
Learn how Compilers use Relative address for Representing 2D arrays

### Column Major Formula for 2D Arrays
Learn how Compilers use Relative address for Representing 2D arrays

### Formulas for nD Arrays
Learn how Compilers use Relative address for Representing nD arrays

### Formulas for 3D Arrays
Learn how Compilers use Relative address for Representing 3D arrays

### Arrays Representation

### Solutions for Quiz 2
Explore array addressing in two-dimensional layouts, including base address calculations, pointer arithmetic, and row-major versus column-major mapping, with deducing data type and dimensions from stepwise evaluation.

## Section 7: Array ADT

### Array ADT
Learn how to represent Array as Abstract Datatype

### Demo - Array ADT
Demonstrates implementing an array ADT in C and C++ by defining a structure with size, length, and a heap-allocated A, reading elements, and displaying them.

### Inserting in an Array
Learn How to Insert an element in an Array at a given index by shifting elements find the time complexity

### Let's Code Insert

### Deleting from Array
Deleting an Element from given index Time complexity Best and Worst case Analysis

### Let's Code Delete
Implement a delete operation on an array by index, shifting elements and updating the length. Return the deleted value and validate the index, illustrating the process in main.

### Linear Search
Linear Search and its Analysis Find Best Worst and Average Case Time

### Improving Linear Search
How to improve Linear Search for future Searches.

### Let's Code Linear Search

### Binary Search
Learn how to Devise Binary Search

### Binary Search Algorithm
Write an Algorithm for Binary Search Recursive Algorithm Iterative Algorithm

### Let's Code Binary Search

### Analysis of Binary Search
Learn how to Analyse Binary Search Best Case Analysis Worst Case Analysis

### Average Case Analysis of Binary Search
Learn how to do Average Case of Binary Search using Tree method

### Get( ) Set( ) Avg( ) Max( ) functions on Array
Learn How to perform Get() / Set()/ Max() / Min()  Operations on an Array

### Let's Code Get() Set() Max() on Array

### Reverse and Shift an Array
Learn Methods to Reverse elements of an Array Learn what does it mean by Shifting elements

### Lest's Code Reversing an Array

### Check if Array is Sorted
Learn how to Check if Array is Already Sorted Learn How to insert an element in a Sorted position Learn how to arrange All negatives on one side and Positives another side.

### Let's Code to check if Array is Sorted
Learn to insert an element into a sorted array, verify if an array is sorted, and rearrange negatives and positives using a single in-place algorithm in C and C++.

### Merging Arrays
Merge two sorted lists into a single sorted array using i, j, and k pointers, handle remaining elements, and achieve theta(m+n) time complexity.

### Let's Code to Merge Arrays
Demonstrate merging two arrays into a new heap-allocated array using a merge function, comparing elements and appending leftovers to produce a sorted result.

### Set operations on Array - Union, Intersection and Difference

### Let's Code Set operations on Array
Demonstrate union, intersection, and difference on sorted and unsorted arrays using a merge-based approach, with a single C and C++ project implementing set operations.

### Let's Code a Menu Driver program for Arrays

### Let's convert C program for Array to C++
Convert a C array program into a C++ class named Array, using dynamic memory, constructors, and destructor. Organize code with private data and public member functions for array operations.

### Let's Put all together in C++ program for Array
Learn to implement a dynamic C++ array as a class with constructors, destructor, and insert, delete, display functions, then convert it to a template for generic types.

### Student Challenge : Finding Single Missing Element in an Array

### Student Challenge : Finding Multiple Missing Elements in an Array

### Student Challenge : Finding Missing Element in an Array Method 2
Study method 2 for finding missing elements by marking a hash-like array (bitset) of size equal to the max element, then scanning for zeros to reveal absent numbers.

### Student Challenge Finding Duplicates in a Sorted Array

### Student Challenge : Finding Duplicates in Sorted Array using Hashing
Master how to find duplicates in a sorted array using a hash table, counting each element's occurrences, and display duplicates with their counts in linear time.

### Student Challenge : Finding Duplicates in a Unsorted Array

### Student Challenge : Finding a Pair of Elements with sum K

### Student Challenge : Finding a Pair of Elements with sum K in Sorted Array
Find pairs in a sorted array whose sum equals a target using left and right pointers. Move pointers based on the sum, print matches, and run in linear time.

### Student Challenge : Finding Max and Min in a single Scan
Find max and min in a single scan by updating min and max per element and skipping the max check when a value is smaller than min. Demonstrates linear time.

### Array ADT

### Solutions for Quiz 3

## Section 8: Strings

### Introduction to Strings
Explore how ASCII codes define characters and how C handles character arrays and strings with a null terminator. Learn to declare, initialize, print, and read strings.

### Finding Length of a String

### Changing Case of a String
Learn to change string case using ascii codes, converting uppercase to lowercase and vice versa, and toggling case with a for loop and 32 difference.

### Counting Words and Vowels in a String

### Validating a String
Validate a string by ensuring only alphabets and digits are allowed, rejecting any special characters. Learn two methods—simple character checks and regular expressions—in C and C++.

### Reversing a String
Explore two methods to reverse a string in C and C++: copy into a separate array using a reverse loop, and perform in-place swapping with two indices.

### Comparing Strings and Checking Palindrome
Learn how to compare two strings, determine dictionary order, and check palindromes using character-by-character comparison and case-insensitive options, with practical C/C++ examples.

### Finding Duplicates in a String
Identify duplicates of letters in a string by comparing characters and counting with a 26-slot hash table using ASCII codes; note a bit-based method is coming next.

### Finding Duplicates in a String using Bitwise Operations

### Checking if 2 Strings are Anagram (distinct letters)

### Permutation of String

## Section 9: Matrices

### Section Introduction
Introduction to Section

### Diagonal Matrix
Learn How to Represent Diagonal Matrix in a Single Dimension Array by storing only non-zero elements

### Let's Code Diagonal Matrix

### C++ class for Diagonal Matrix

### Let's Code C++ class for Diagonal matrix

### Lower Triangular Matrix Row-Major Mapping
Learn How to Represent Lower Triangular Matrix in a Single Dimension Array by storing only non-zero elements Row-by-Row Representation

### Lower Triangular Matrix Column-Major Mapping
Learn How to Represent Lower Triangular Matrix in a Single Dimension Array by storing only non-zero elements Column-by-Column Representation

### Let's Code Lower Triangular Matrix in C
Implement a lower triangular matrix in C using row major and column major representations, with dynamic memory, set, get, and display functions, and keyboard input for dimensions and elements.

### Let's Code Lower Triangular Matrix in C++

### Upper Triangular Matrix Row-Major Mapping
Learn How to Represent Upper Triangular Matrix in a Single Dimension Array by storing only non-zero elements Row-by-Row Representation

### Upper Triangular Matrix Column-Major Mapping
Learn How to Represent Upper Triangular Matrix in a Single Dimension Array by storing only non-zero elements Column-by-Column Representation

### Symmetric Matrix
Learn How to Represent Symmetric Matrix in a Single Dimension Array by storing only non-zero elements

### Tri-Diagonal and Tri-Band Matrix
Learn How to Represent Trim-Diagonal and Trim-Band Matrix in a Single Dimension Array by storing only non-zero elements

### Toeplitz Matrix
Learn How to Represent Toeplitz Matrix in a Single Dimension Array by storing only non-zero elements

### Menu Driven Program for Matrices

### Menu Driven Program for Matrices using Functions
The lecture demonstrates how to build a menu driven matrix program using functions, with create, get, set, and display operations, using an array and a dimension n.

### How to Write C++ Classes for All Matrices
Learn to implement C++ classes for diagonal and lower triangular matrices, with heap-allocated storage, constructors/destructors, and a menu-driven program to create, display, and access elements.

### Matrices

## Section 10: Sparse Matrix and Polynomial Representation

### Sparse Matrix Representation
Learn How to Represent a Sparse Matrix 1. 3-Column Representation 2. Compressed Sparse Row Representation

### Addition of Sparse Matrices
Learn How to Add 2 Sparse Matrices using Representation

### Array Representation of Sparse Matrix
Learn how to Create a Data Structure for storing Sparse Matrix

### Let's Code to Create Sparse Matrix
Learn to implement a sparse matrix in C by defining element and sparse structures, reading dimensions and non-zero elements, allocating memory, and displaying the full matrix.

### Program for Adding Sparse Matrix

### Let's Code to Add Sparse Matrix
Implement a C function add that sums two sparse matrices by address, allocates the sum on the heap with malloc, and merges nonzero elements by row and column.

### Let's Code Sparse Matrix using C++

### Let's Code Sparse Matrix using C++ Continued.....

### Polynomial Representation
Learn about Polynomial Representation

### Polynomial Evaluation
Learn how to Evaluate Polynomial using its Representation

### Polynomial Addition
Learn how to Add 2 Polynomials using representation

### Let's Code Polynomial
Explore polynomial representation and evaluation in C and C++ by defining term and poly structures, dynamically allocating memory, and reading, displaying, and adding polynomials with pointer-based functions.
