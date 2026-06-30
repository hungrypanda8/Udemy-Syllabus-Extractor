# Operating Systems Part 3 : Synchronization and Deadlock

## What You Will Learn

- You will become very  familiar with the core concepts of Operating Systems
- You will be able to challenge the interviewer on questions related to Synchronization and Deadlock
- You will view Computer Science in a different dimension
- You will be able to answer all questions of exams like GATE,PGEE,ISRO (after completing all parts of OS course
- You will be able to get a top grade in your Operating systems course in your Bachelor's degree
- Understand how Operating Systems work
- Understand how Process synchronization works
- Understand about Deadlocks
- Understand various synchronization mechanisms in Operating Systems

---

## Section 1: Introduction

### Concept of Shared Memory

### Need for Synchronization Mechanism - 1

### Need for Synchronization Mechanism - 2

## Section 2: Critical Section and Non Critical Section

### Critical Section and Race Condition Explained

### Why Race Condition happens

### More on Critical Section and Non Critical Section

### Synchronization explained

## Section 3: Various Conditions of a Synchronization Mechanism

### Basic Idea of Mutual Exclusion

### Basic Idea of Progress

### Basic Idea of Bounded Waiting

## Section 4: Lock Synchronization Mechanism

### Synchronization with Lock variable and its disadvantage

### Progress Condition for Lock variable
Evaluate whether the lock variable satisfies progress, noting it does not satisfy mutual exclusion, and that only a process in the critical section may block others; therefore, progress is satisfied.

### Bounded Waiting Condition for Lock variable
Analyze a lock variable to see if bounded waiting holds: it provides progress but fails mutual exclusion and bounded waiting, causing possible starvation as one process repeatedly enters critical sections.

### Features of Lock Synchronization

## Section 5: TSL Synchronization Mechanism

### Important : Basics of Assembly Code

### When Mutual Exclusion can be violated in Lock synchronization mechanism

### Need for special instruction - TSL
Explore the test and set lock (TSL) as an atomic instruction that prevents preemption between load and store, ensuring mutual exclusion during entry to the critical section, and discussing disadvantages.

### TSL Synchronization Mechanism Explained
Explain the TSL synchronization mechanism (test and set lock) that achieves mutual exclusion without preemption, its hardware dependent nature, and how initial and updated lock values control entry.

### TSL - Mutual Exclusion, Progress, Bounded Waiting

### Features of TSL Synchronization Mechanism
Explore the TSL synchronization mechanism as a busy-waiting solution for multiple processes, using entry and exit sections, and requiring hardware support unlike the lock variable.

## Section 6: Problems on TSL

### Checking of Starvation Problem

### Checking of FIFO order

### Checking of Mutual Exclusion and Deadlock

## Section 7: Strict Alternation Synchronization Mechanism

### Strict Alternation Synchronization - Mutual Exclusion, Progress
The strict alternation synchronization for two processes uses a turn variable with entry and exit sections to enforce mutual exclusion in the critical section, but progress is not guaranteed.

### Strict Alternation - Bounded Waiting
Explore strict alternation as a synchronization mechanism, showing that bounded waiting and mutual exclusion are guaranteed, but progress is not guaranteed.

### Features of Strict Alternation Synchronization Mechanism

### Problem on Strict Alternation

## Section 8: Disable Interrupts Synchronization Mechanism

### Disabling Interrupts Synchronization Explained Completely

### Features of Disabling Interrupts and its disadvantage

## Section 9: Interested Variables Synchronization Mechanism

### Interested Synchronization Mechanism Explained

### Interested Synchronization - Mutual Exclusion

### Interested Synchronization - Deadlock

### Interested Synchronization - Progress

### Interested Synchronization - Progress Continued

### Interested Synchronization - Bounded Waiting

## Section 10: Peterson Synchronization Mechanism

### Peterson Synchronization Mechanism intro

### Difference between Local and Global Variables

### Peterson Synchronization Mechanism Explained

### Peterson Synchronization Mechanism Continued

### Peterson Synchronization Mechanism - Mutual Exclusion

### Peterson Synchronization Mechanism - Progress
Analyze the Peterson synchronization mechanism to show progress is guaranteed under all values of P0 and P1, by satisfying the first and second conditions for entering the critical section.

### Peterson Synchronization Mechanism - Bounded Waiting

### Features of Peterson Synchronization Mechanism
