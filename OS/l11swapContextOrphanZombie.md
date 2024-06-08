### Lecture 11: Swapping, Context Switching, Orphan Process, and Zombie Process

### Swapping

Swapping is a memory management technique used to manage the processes in the system by temporarily moving inactive processes from main memory to secondary storage (swap space) and bringing them back when needed. This process helps manage the limited amount of main memory and ensures that active processes have the necessary resources.

**Key Points:**

1. **Medium Term Scheduler:**
   - The medium-term scheduler (MTS) is responsible for swapping processes in and out of the main memory.
   - It balances the load on the system by managing the degree of multiprogramming.

2. **Reduced Degree of Multiprogramming:**
   - Swapping out processes reduces the number of active processes in memory, which can help manage system load and improve performance.
   - The degree of multiprogramming refers to the number of processes in memory at one time. Swapping helps control this number.

3. **Swap-Out and Swap-In by MTS:**
   - **Swap-Out:** Moving an inactive or low-priority process from main memory to swap space.
   - **Swap-In:** Bringing a swapped-out process back into main memory when it becomes active again.

4. **Process Selection for Swapping:**
   - The MTS selects processes for swapping based on their state (e.g., waiting for I/O), priority, and resource requirements.

5. **Flow Chart:**
   - **Start:** Process enters the system.
   - **Check Memory:** Is there enough memory?
     - **Yes:** Process stays in memory.
     - **No:** MTS selects a process to swap out.
   - **Swap-Out:** Process moved to swap space.
   - **New Process:** Load the new process into memory.
   - **Swap-In:** When the swapped-out process is needed again, it is brought back into memory.

**Flow Chart:**
```
Start -> Check Memory
        -> If No -> MTS selects process to swap out -> Swap-Out -> Load new process
        -> If Yes -> Process stays in memory
        -> Swap-In (when needed)
```

### Context Switching

Context switching is the process of saving the state of a currently running process and loading the state of another process. This allows the OS to manage multiple processes by switching the CPU's focus between them.

**Key Points:**

1. **State Save:**
   - The OS saves the current state of the running process, including the values of CPU registers, program counter, and other critical data.
   - This information is stored in the Process Control Block (PCB) of the process.

2. **State Restore:**
   - The OS loads the saved state of the next process to be executed from its PCB.
   - This includes restoring CPU registers, program counter, and other critical data.

3. **PCB (Process Control Block):**
   - The PCB is a data structure used by the OS to store all the information about a process.
   - It contains the process state, program counter, CPU registers, memory management information, and I/O status.

4. **Pure Overhead:**
   - Context switching is considered pure overhead because it does not perform any useful work itself.
   - The time spent saving and restoring process states can impact system performance, especially if context switches are frequent.

### Orphan Process

An orphan process is a process whose parent process has terminated, but it is still running.

**Key Points:**

1. **Parent Process Terminated:**
   - The parent process has terminated, leaving the child process as an orphan.

2. **Adopted by Init Process:**
   - In UNIX-like systems, orphan processes are adopted by the `init` process (process ID 1), which is the first process started by the OS.
   - `init` takes over the responsibility of cleaning up orphan processes.

3. **Function of Init:**
   - `init` ensures that orphan processes are properly managed and eventually terminated.

### Zombie Process

A zombie process, or defunct process, is a process that has completed its execution but still remains in the process table.

**Key Points:**

1. **Execution Completed:**
   - The process has finished executing but has not been fully cleaned up by the OS.

2. **Still Present in Process Table:**
   - The process entry remains in the process table to hold the exit status for the parent process to read.

3. **Reaping:**
   - The process remains a zombie until the parent process retrieves its exit status using the `wait` function.
   - The parent process must call `wait` to remove the zombie process entry from the process table.

4. **Wait Function:**
   - The `wait` system call allows the parent process to collect the exit status of the terminated child process.
   - Once the status is collected, the zombie process is removed from the process table.

### Summary

**Swapping:**
- **Medium Term Scheduler:** Manages swapping to control the degree of multiprogramming.
- **Swap-Out:** Moving inactive processes to swap space.
- **Swap-In:** Bringing processes back into memory when needed.

**Context Switching:**
- **State Save:** Saving the state of the current process in its PCB.
- **State Restore:** Loading the state of the next process from its PCB.
- **Pure Overhead:** Context switching time does not contribute to useful work.

**Orphan Process:**
- **Parent Process Terminated:** Leaves the child process as an orphan.
- **Adopted by Init:** `init` process adopts orphan processes to manage them.

**Zombie Process:**
- **Execution Completed:** Process remains in the process table.
- **Reaping:** Parent process must call `wait` to remove the zombie process.

**Flow Chart for Swapping:**

1. **Start:** Process enters the system.
2. **Check Memory:** Is there enough memory?
   - **Yes:** Process stays in memory.
   - **No:** MTS selects a process to swap out.
3. **Swap-Out:** Process moved to swap space.
4. **Load New Process:** Load the new process into memory.
5. **Swap-In:** When the swapped-out process is needed again, it is brought back into memory.

Would you like to explore any specific part of this lecture in more detail or move on to another topic?