### Definitions

**Program:**
- A program is a static set of instructions written in a programming language that performs a specific task when executed. It is a passive entity stored on disk (e.g., an executable file).

**Process:**
- A process is an active instance of a program. It includes the program code, current activity, data section, heap, stack, and the program counter (PC). A process is an independent entity that the OS manages for resource allocation and scheduling.

**Thread:**
- A thread is the smallest unit of execution within a process. It consists of a thread ID, a program counter, a register set, and a stack. Multiple threads can exist within a single process, sharing the same code and data sections but having their own stack and registers.

### Multitasking vs. Multithreading

**Multitasking:**
- Multitasking refers to the ability of an OS to execute multiple tasks (processes) concurrently. It can be either cooperative or preemptive.
  - **Cooperative Multitasking:** Processes voluntarily yield control to allow other processes to execute.
  - **Preemptive Multitasking:** The OS forcibly preempts processes to allocate CPU time to others.

**Multithreading:**
- Multithreading refers to the ability of a process to have multiple threads executing concurrently. Threads within the same process share resources such as memory and file handles, but they run independently.
  - **Advantages:** Reduced context switching overhead compared to multitasking, better CPU utilization, improved application performance, especially for I/O-bound tasks.

### Thread Scheduling

**Thread Scheduling:**
- Thread scheduling is the method by which the OS decides which thread to run next on the CPU. It is similar to process scheduling but occurs at a finer granularity. Common thread scheduling algorithms include:
  - **Time Slicing:** Each thread is given a fixed time slot to execute.
  - **Priority Scheduling:** Threads with higher priority are scheduled before lower-priority ones.
  - **Round Robin:** Threads are scheduled in a cyclic order, each getting an equal share of CPU time.
  - **Multilevel Queue Scheduling:** Threads are placed in multiple queues based on priority or other criteria, and each queue can have its own scheduling algorithm.

### Context Switching

**Thread Context Switching:**
- Involves saving and restoring the state of the CPU registers, program counter, and stack pointer specific to a thread. Since threads within the same process share the same address space, thread context switching is relatively lightweight and faster compared to process context switching.

**Process Context Switching:**
- Involves saving and restoring the complete state of a process, including CPU registers, program counter, memory mappings, and address space. This is more complex and time-consuming because it involves changing the entire memory context, not just the stack and registers.

### Key Differences:

| Aspect                      | Thread Context Switching      | Process Context Switching         |
|-----------------------------|-------------------------------|-----------------------------------|
| Execution Unit              | Thread                        | Process                           |
| Address Space               | Shared within the process     | Independent address space         |
| Overhead                    | Lower                         | Higher                            |
| Speed                       | Faster                        | Slower                            |
| Complexity                  | Simpler                       | More complex                      |
| Resource Sharing            | Shared within process         | Separate                          |

### Summary:

1. **Program:** Static set of instructions.
2. **Process:** Active instance of a program, including code, data, and execution state.
3. **Thread:** Smallest unit of execution within a process, sharing resources with other threads in the same process.
4. **Multitasking:** OS capability to execute multiple processes concurrently.
5. **Multithreading:** A process's capability to execute multiple threads concurrently.
6. **Thread Scheduling:** Method of deciding which thread to run next, including algorithms like time slicing and priority scheduling.
7. **Thread Context Switching:** Involves switching between threads within the same process, faster and less complex.
8. **Process Context Switching:** Involves switching between processes, slower and more complex due to independent address spaces.

