# Fibonacci Time Complexity App

This project consists of a simple desktop application that calculates Fibonacci numbers using a C program and plots the execution time (time complexity) using Python. The application allows users to specify the Fibonacci sequence's stopping point and generates a CSV file with the Fibonacci values and their corresponding execution times, which are then plotted as a graph.

## Features:
- **Fibonacci Calculation**: Computes Fibonacci numbers recursively in C and logs the execution time for each number.
- **Time Complexity Plotting**: Uses Python and Matplotlib to plot the execution time as the sequence grows.
- **User Interface**: Built with Tkinter, allowing users to input the stopping point for the Fibonacci sequence and visualize the performance.

## Project Structure:
```bash
- Fibonacci_stats/                # Python code to plot the data
- fibonacci_exec_time/            # C code for generating Fibonacci data
    - fibonacci.c                 # Main C program for Fibonacci calculation
    - fibonacci_executable        # Compiled C executable
- README.md                       # Project information
- requirements.txt                # Python dependencies
```



## Input:

- Enter the stopping number for the Fibonacci sequence.
- The C program will generate the Fibonacci sequence up to that number, logging the execution time in a CSV file.

## Output:

-The execution times are automatically plotted in a graph.
-CSV file with Fibonacci data and execution times is saved in the project directory.
