# Virtual Memory & Page Replacement Simulator

**Course:** Computer Architecture  
**Semester:** 5th Semester  

## Overview
This repository contains a Python-based simulation evaluating the computational efficiency of three standard operating system page replacement algorithms:
* **FIFO** (First-In-First-Out)
* **LRU** (Least Recently Used)
* **Optimal**

The simulator programmatically translates logical addresses into virtual pages and monitors physical memory frame allocation to track and compare page fault 
frequencies.

## How to Run
1. Ensure Python 3.x is installed on your system.
2. Run the script from the terminal:
   ```bash
   python simulator.py
3. When prompted, enter a space-separated string of logical addresses (e.g., 1 7 3 9 1 1 3 7 6 3 1 1 9 5 4 2 3 2 1 0), the page size, and the number of
   physical frames.

## Features
* **Dynamic Translation:** Calculates logical to physical mappings based on user-defined page sizes.
* **Algorithmic Evaluation:** Steps through physical frame states (Hits vs. Page Faults).
* **Performance Output:** Automatically determines the most resource-efficient replacement strategy for the provided reference string.
