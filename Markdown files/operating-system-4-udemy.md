# Operating Systems Final Part (4) : File Systems & Threads

## What You Will Learn

- You will become very  familiar with the core concepts of Operating Systems
- You will be able to challenge the interviewer on questions related to Operating Systems
- You will view Computer Science in a different dimension
- You will be able to answer all questions of exams like GATE,PGEE,ISRO (after completing all parts of OS course
- Understand how Operating Systems work
- Understand File Systems
- Understand Disk Scheduling Works
- Understand how Hard Disks work

---

## Section 1: Introduction

### Important : What is a File System

### Attributes of a file

### Logical Block Number, Physical Block number, Important points about Hard disk

## Section 2: Understanding File Access using System Calls

### create () system call

### Finding Logical Block Number and Physical Block Number using Logical Byte Number
Map a logical byte to its logical block using floor division by a 512-byte block in contiguous allocation, then locate the physical block from the first block.

### open () system call

### read () and write () system call

### Operations of a File

## Section 3: File Allocation Methods - Contiguous Allocation

### Contiguous Allocation with advantages

### Important point to note

### Disadvantages of Contiguous Allocation - Size Declaration Problem
Explore the size declaration problem in contiguous file allocation, where predefining exact disk blocks limits file growth and prevents seamless expansion.

### Disadvantages of Contiguous Allocation - External Fragmentation Problem

### Disadvantages of Contiguous Allocation - Internal Fragmentation Problem

## Section 4: File Allocation Methods - Linked List Allocation

### Linked List Allocation

### Advantages of Non Contiguous Allocation

### Disadvantages of Linked List Allocation Method
Examine the disadvantages of linked list allocation, highlighting non-contiguous blocks causing slow reads and seeks, pointer overhead, and persistent internal fragmentation when file sizes differ from block size.

### Size of pointer in a block

## Section 5: File Allocation Methods - FAT Allocation

### Understanding FAT Allocation Method

### Advantage of FAT Allocation Method over Linked List Allocation

### Calculating the size of FAT

### Problem on FAT Allocation Method

## Section 6: Indexed Allocation Method

### Understanding Indexes of a file
Explore indexed allocation as an alternative to maintaining a single table by using a per-file index that maps each file block to its disk block, enabling direct random access.

### Indexed Allocation - Complete Picture

### Placing Index across multiple disk blocks using Linked List

### Placing Index across multiple disk blocks using Multi level Index

### Placing Index across multiple disk blocks using Hybrid method

### Very Important Point to Note
Relate block size and index entry size to index entries per block, and show direct pointers reach one block while indirect pointers yield x, x^2, and x^3 blocks.

### Problem 1 on Inode

### Problem 2 on Inode

## Section 7: Free Space Management

### Free Space Management using 2 data structures
Discover free space management with bitmap and linked list to track free disk blocks in RAM, allocate blocks to files, and delete from the free list efficiently.

## Section 8: Understanding the structure of Hard disk

### Why we need Disk Scheduling Algorithms
Explore disk scheduling and why the cpu is faster than io, showing how ordering disk io among multiple processes affects total io time, and compare first-come-first-served with least-io-time strategies.

### Hard Disk Structure , Seek Time, Rotational Latency, Data Transfer Time

### How order of processing disk requests can change the total seek time

### Difference between track and cylinder

## Section 9: Basic Disk Scheduling Algorithms - FCFS, SSTF

### FCFS Disk Scheduling Basics

### FCFS explained with example
Explore fcfs disk scheduling with a practical example, showing requests served in their arrival order and calculating 421 cylinder movements and 421 nanoseconds of seek time.

### SSTF explained with example

### Why SSTF suffers from Starvation problem

### Why FCFS and SSTF are not the best disk scheduling algorithms

## Section 10: Popular Disk Scheduling Algorithms - SCAN, C-SCAN, LOOK, C-LOOK

### SCAN Disk Scheduling Algorithm

### C-SCAN Disk Scheduling Algorithm

### Why the name "Circular SCAN" ?

### LOOK Disk Scheduling Algorithm

### C-LOOK Disk Scheduling Algorithm
Learn the C-LOOK disk scheduling algorithm, a circular LOOK that combines LOOK and C-SCAN, starting at cylinder 53 and moving in one direction to the outermost request.

### Problem on C-LOOK Algorithm

### Problem on LOOK Algorithm

### Problem on C-SCAN Algorithm

### Problem on SCAN Algorithm
