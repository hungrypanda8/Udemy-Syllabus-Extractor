# Operating Systems from scratch - Part 2

## What You Will Learn

- You will master Memory Management in Operating Systems
- You will be very comfortable with advanced topics like Paging
- You will be able to have a good grasp over computer science
- You will be able to understand other advanced topics of computer science like Distributed Systems
- You will be able to understand other advanced topics of computer science like Computer Organization
- You will be able to understand other advanced topics of computer science like Database Systems
- understand memory allocation strategies used by operating systems

---

## Section 1: Introduction

### About the course

### Important Tips

## Section 2: Basics of Memory Management (Cover it only if you have not watched part 1)

### Important point

### Important : Basics of Binary numbers

### Basics of Memory Management

### Address Space and Types of allocation

### Fixed Partitioning

### Variable Partitioning

### Memory Allocation Algorithms

### Problem

### Problem continued

### Important point to note

### Problem

### Binary addressing revisited

### Example to explain binary addressing concepts

## Section 3: Paging

### Need for paging
Explore why paging and segmentation solve memory management challenges in operating systems. Compare fixed and dynamic partitions, internal and external fragmentation, and how paging enables non-contiguous allocation.

### How CPU executes a process in contiguous allocation

### Basics of paging (Just an intro)

### Paging explained with example 1

### Paging explained with example 1 continued

### Paging explained with example 2

### Internal Fragmentation Revisited
Revisit internal fragmentation in paging, showing it can occur when the process size is not a multiple of the page size or when the page table is smaller than a page, while paging avoids external fragmentation.

### Relation between LA,LAS and PA,PAS

### Problem on number of frames

### Important points to observe
Compute ram size as 2^(m-n) frames times 2^n bytes per frame, giving 2^m bytes. Relate processes to paging: 2^l pages with 2^k bytes per page yield total size 2^(l+k) bytes.

### Problem on number of pages

## Section 4: Problems on Paging

### Problem 1 on Paging

### Problem 2 on Paging

### Problem 3 on Paging

### Problem 4 on Paging

### Problem 5 on Paging

### Problem 6 on Paging

## Section 5: Multilevel Paging

### Summary of Paging

### Need for Multilevel Paging

### Contiguous vs Single level paging vs Multilevel paging

### Contiguous vs Single level paging vs Multilevel paging continued

### Multilevel Paging Intro
Introduce multilevel paging to handle non-contiguous process pages by using level 0 and level 1 page tables stored in RAM frames, with pointers, simple indexing, and awareness of internal fragmentation.

### Multilevel Paging Intro continued

## Section 6: Multilevel Paging Problems

### Problem 1 on Multilevel Paging

### Problem 2 on Multilevel Paging

### Problem 2 on Multilevel Paging continued

### Problem 3 on Multilevel Paging

### Problem 4 on Multilevel Paging

### Problem 5 on Multilevel Paging

### Problem 6 on Multilevel Paging

### Problem 7 on Multilevel Paging
The lecture analyzes a three-level paging system, derives 2^10 outer page table entries, 2^20 level-two page table entries, and 2^30 level-one entries, yielding an 8 tb address space.

### Problem 8 on Multilevel Paging
solve a single-level paging problem by computing 2^10 page table entries from an 8 KB outer page table with 8-byte entries, yielding a process size of 2^23 bytes.

## Section 7: Page Table Entry

### Important point to note

### Frame number field and Referenced bit

### Present/Absent bit and Dirty bit

### Protection bits

### Summary of Page Table Entry

### Advantage of Dirty bit field in Page Table entry
The dirty bit in a page table entry signals whether a page was modified and must be written back during page replacement, avoiding unnecessary writes to disk and saving time.

## Section 8: Page Table Entry Problems

### Problem 1 on Page Table Entry

### Problem 2 on Page Table Entry
Compute the page table size in a 32-bit, byte-addressable system with 4 KB pages and 4-byte entries, showing that 2^20 entries yield 2^22 bytes or 4 MB.

### Problem 3 on Page Table Entry

### Problem 4 on Page Table Entry

### Problem 5 on Page Table Entry

## Section 9: Virtual Memory

### Locality of Reference and Virtual Memory explained
Explain locality of reference and virtual memory, showing how the cpu uses only a few pages at a time to boost degree of multiprogramming, via ram frames and disk storage.

### Advantages of Virtual Memory

## Section 10: Average Memory Access Time (AMAT)

### Page Hit and Page Fault Explained

### Average Memory Access Time Explained

### Another way of looking at AMAT

### AMAT explained with example
Explore average memory access time for a two-level paging system with 10 ns ram and 1000 ns disk, 90% page hit rate, yielding 1030 ns and 130 ns.

### Relation between Number of levels of Paging and Number of RAM Accesses
