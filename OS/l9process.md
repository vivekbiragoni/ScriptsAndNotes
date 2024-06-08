### Lecture 9: Introduction to Process

Understanding the concepts of a program and a process is fundamental to comprehending how an operating system manages resources and executes tasks.

### What is a Program?

**Program:**
- A program is a static set of instructions written in a programming language designed to perform a specific task when executed.
- It resides on disk (e.g., executable file) and is not active until loaded into memory and executed.
- **Example:** An executable file such as `example.exe` on Windows or `example.out` on Linux.

### What is a Process?

**Process:**
- A process is an active instance of a program in execution.
- It includes the program code, current activity (represented by the value of the Program Counter and the contents of the processor's registers), stack, data section, and heap.
- A process is a dynamic entity, often referred to as a "job" or "task."

### How OS Creates a Process

The creation of a process involves several steps that the OS undertakes to prepare and execute a program. Here’s an outline of the process creation steps:

1. **Load the Program and Static Data into Memory:**
   - The OS loads the program's executable file from secondary storage (e.g., HDD, SSD) into main memory (RAM).
   - The program's code and static data (global variables) are loaded into specific memory segments.

2. **Allocate Runtime Tags:**
   - The OS allocates memory for the process's runtime data, including the stack and heap.
   - The stack is used for function calls and local variables, while the heap is used for dynamically allocated memory.

3. **Initialize Process Control Block (PCB):**
   - The OS creates a PCB, a data structure that contains information about the process.
   - Attributes in the PCB include process ID, process state, CPU registers, memory management information, I/O status information, and accounting information.

4. **Initialize I/O Tasks:**
   - The OS sets up I/O resources required by the process, such as file descriptors and device buffers.

5. **OS Handoffs Control to Main:**
   - The OS initializes the CPU registers and sets the Program Counter to the entry point of the program (usually the `main` function in many programming languages).
   - Control is handed off to the process, and the CPU begins executing the process's instructions.

### Architecture of a Process

A process typically consists of the following segments in memory:

1. **Text Segment:**
   - Contains the compiled program code (instructions).

2. **Data Segment:**
   - Contains global and static variables initialized by the programmer.

3. **Heap Segment:**
   - Used for dynamic memory allocation (e.g., via `malloc` in C or `new` in C++).

4. **Stack Segment:**
   - Used for function calls, local variables, and control flow (e.g., return addresses).

### Attributes of a Process

Key attributes of a process are stored in its Process Control Block (PCB):

1. **Process ID (PID):**
   - A unique identifier assigned to each process.

2. **Process State:**
   - The current state of the process (e.g., new, ready, running, waiting, terminated).

3. **Program Counter (PC):**
   - The address of the next instruction to be executed.

4. **CPU Registers:**
   - The contents of all the CPU registers used by the process.

5. **Memory Management Information:**
   - Details about the process's memory allocation, including pointers to the text, data, stack, and heap segments.

6. **I/O Status Information:**
   - Information about the I/O devices allocated to the process and the status of I/O operations.

7. **Accounting Information:**
   - Process execution time, CPU usage, user and group identifiers, etc.

### PCB Structure

The PCB is a data structure in the operating system kernel that contains essential information about a process. Here’s a breakdown of typical PCB fields:

1. **Process ID (PID):** Unique identifier for the process.
2. **Process State:** Current state of the process.
3. **Program Counter (PC):** Address of the next instruction to execute.
4. **CPU Registers:** Snapshot of CPU registers.
5. **Memory Management Info:** Base and limit registers, page tables, etc.
6. **Scheduling Information:** Priority, scheduling queue pointers.
7. **I/O Status Information:** List of open files, I/O devices allocated.
8. **Accounting Information:** CPU usage, elapsed execution time, user ID.

### Registers in PCB

The PCB includes the current contents of the CPU registers when the process is not executing. This snapshot allows the OS to restore the process state when it resumes execution.

**Common Registers Saved:**
1. **Program Counter (PC):** Next instruction address.
2. **Stack Pointer (SP):** Top of the current stack in memory.
3. **Base Pointer (BP):** Base of the stack frame.
4. **General-Purpose Registers:** Data used during execution (e.g., `eax`, `ebx` in x86 architecture).
5. **Status Register:** Information about the state of the processor.

### Summary

- **Program vs. Process:** A program is a static set of instructions, while a process is an active instance of a program in execution.
- **Process Creation:** Involves loading the program into memory, allocating runtime resources, initializing the PCB, setting up I/O tasks, and transferring control to the program's entry point.
- **Process Architecture:** Consists of text, data, heap, and stack segments.
- **PCB Attributes:** Includes PID, process state, PC, CPU registers, memory management, I/O status, and accounting information.
- **Registers in PCB:** The PCB stores a snapshot of CPU registers to facilitate process switching.

