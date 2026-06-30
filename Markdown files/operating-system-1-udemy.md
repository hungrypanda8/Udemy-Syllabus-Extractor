# Operating Systems from scratch - Part 1

## What You Will Learn

- You will become very  familiar with the core concepts of Operating Systems
- You will be able to challenge the interviewer on questions related to Operating Systems
- You will view Computer Science in a different dimension
- You will be able to answer all questions of exams like GATE,PGEE,ISRO (after completing all parts of OS course
- You will be able to get a top grade in your Operating systems course in your Bachelor's degree
- Understand how Operating Systems work
- Understand how a process is created
- Understand how CPU scheduling is done in Operating Systems
- Understand the various scheduling algorithms we have in Operating Systems
- Understand how CPU , Memory and Disk work together
- Understand Memory managment in Operating Systems
- Understand how a process is moved from hard disk to RAM
- understand memory allocation strategies used by operating systems

---

## Section 1: Introduction

### Introduction : Very Important

### Important Tip

## Section 2: Introduction to Operating Systems

### Important : Introduction to Computer Systems
Define a computer system as hardware, software, and data that solve human problems, and explain how the CPU fetches programs from RAM for fast processing and permanent storage.

### How hardware devices work together

### Need for Operating Systems from scratch

### How Input and Output devices work together

## Section 3: Operating System Concepts

### Program vs Process, States of a process

### Degree of Multiprogramming

### Types of Operating Systems

### An Important point to note
Demonstrate the three OS types—batch OS, multiprogramming OS, and multi-processing OS—and explain that the course defaults to multiprogramming OS, with a single CPU and multiple processes in RAM.

### Process Control block, Attributes of a process

## Section 4: CPU Scheduling Algorithms - SJF, SRTF, FCFS

### Types of scheduler, Context switching

### Various times of a process

### Types of Scheduling Algorithms

### SJF Scheduling Algorithm

### SJF Example 1

### SJF Example 2
Demonstrates a non-preemptive SJF scheduling with five processes, using a Gantt chart to compute completion, turnaround, and waiting times, then determine the schedule length and throughput.

### Shortest Remaining Time First Scheduling Algorithm

### Response time explained with example

### SRTF assignment problem

### SRTF assignment problem solution
Apply the SRTF scheduling algorithm to an arrival-based set of processes, construct a Gantt chart, compute completion times and turnaround times, and derive the average waiting time.

### Response Time example 2

### SRTF assignment problem 2

### SRTF assignment problem 2 solution
Learn to solve an SRTF scheduling problem by building a Gantt chart, calculating completion times, turn around times, and waiting times, and deriving the average waiting time.

### First Come First Served Scheduling Algorithm

### FCFS with Context Switching overhead
Learn how FCFS scheduling with a 1 time unit context switching overhead affects completion times, CPU efficiency, and waiting, turnaround, and response times in non-preemptive, multi-process systems.

## Section 5: Comparision of FCFS, SJF and SRTF - Advantages and Disadvantages

### Starvation

### Convoy Effect

### Practical Implementation
Explore the practical implementation of SJF, SRTF, and FCFS, and compare throughput, noting that SJF and SRTF offer higher throughput but are hard to implement due to burst time prediction.

### Throughput

## Section 6: CPU Scheduling Algorithms - LJF, LRTF, Priority-based, HRRN

### Longest Job First Scheduling Algorithm
Explains the longest job first scheduling algorithm, a non-preemptive, priority-based approach opposite to shortest job first; highlights starvation, convoy effects, low throughput, and burst-time prediction challenges.

### LJF Example 1
Explore the longest job first non-preemptive scheduler using a Gantt chart to compute completion times, turnaround times, waiting times, response times, and throughput for five processes.

### Longest Remaining Time First Scheduling Algorithm

### LRTF Example 1
Explore the longest remaining time first scheduling algorithm, with tie-breaking by arrival time and process id, illustrated through a step-by-step Gantt chart of three processes.

### LRTF Example 2
Demonstrates the longest remaining job first scheduling algorithm, with tie-breaking by earliest arrival, illustrated by a step-by-step Gantt chart of P1, P2, and P3 and idle cpu time.

### LRTF Example 2 continuation
Compute completion times 9, 10, and 11 in a non-preemptive schedule for three processes, derive turnaround times 8 and waiting times 6, 4, and 4, with throughput 3 by 10.

### Round Robin Scheduling Algorithm

### RR Example 1
Explore round robin scheduling with a time quantum of 2, showing how arrivals enter the ready queue, how the CPU preempts running processes, and how a Gantt chart tracks progress.

### RR Example 2

### RR Important Observations
Increasing time quantum may decrease context switches, but not always, affecting overhead and CPU efficiency. As time quantum grows, the response time increases, reducing interactivity.

### Advantages and Limitations of RR Algorithm

### Non Preemptive Priority based Scheduling Algorithm

### Preemptive Priority based Scheduling Algorithm

### Preemptive Priority based Scheduling Algorithm Continuation

### SRTF with processes requiring CPU and IO time 2
Apply SRTF scheduling to processes with CPU and IO bursts, trace a detailed Gantt chart, and compute CPU efficiency as 14 out of 16 time units.

### Priority based scheduling with processes requiring CPU and IO time
Apply preemptive priority-based scheduling to a set of processes with CPU and IO bursts, determine highest-priority arrivals, and construct a Gantt chart to analyze CPU idle time and efficiency.

### Highest Response Ratio Next Scheduling Algorithm

### HRRN Example
Explore the highest response ratio next non-preemptive scheduling example, illustrated with a Gantt chart and calculations of waiting time, burst time, and response ratios.

### Process State Diagram

### Suspend Ready State and Suspend IO state

### Dispatcher

## Section 7: Basics of Number System

### Basics of Binary Numbers

### Basics of Binary Numbers

## Section 8: Memory Allocation Techniques

### Basics of Memory Allocation

### Contiguous Allocation vs Non Contiguous Allocation

### Fixed Partitioning
Explore fixed partitioning, or static partitioning, where RAM is divided into fixed-size partitions; understand its one-process-per-partition rule, internal fragmentation, and limits on process size and multiprogramming.

### Variable Partitioning

### Memory Allocation Algorithms

### Problem

### Problem continued

### Important point to note

### Problem

### Binary addressing revisited

### Example to explain binary addressing concepts

### Need for paging
Explore memory management in operating systems, contrasting fixed and dynamic partitioning, internal and external fragmentation, and the shift to paging and segmentation for non-contiguous allocation.

## Section 9: Bonus : How to proceed further

### Special Bonus
