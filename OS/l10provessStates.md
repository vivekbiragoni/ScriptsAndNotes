### Lecture 10: Process States and Process Queues

Understanding process states and process queues is essential for grasping how an operating system manages multiple processes and ensures efficient execution.

### 1. Process States

A process can be in one of several states during its lifecycle. These states help the OS manage and schedule processes efficiently.

**A. New:**
   - The process is being created.
   - The OS has allocated resources for the process, but it has not yet begun execution.

**B. Running:**
   - The process is currently being executed by the CPU.
   - At any given time, only one process per CPU core can be in this state.

**C. Waiting:**
   - The process cannot execute until some external event occurs (e.g., I/O completion, resource availability).
   - It is waiting for a specific condition to be met.

**D. Ready:**
   - The process is ready to run but is not currently executing because another process is running.
   - It is waiting for CPU time.

**E. Terminated:**
   - The process has finished execution.
   - The OS will clean up resources used by the process.

### 2. Process Queues

The OS maintains various queues to manage process states and transitions efficiently. These queues ensure that processes are executed in a fair and orderly manner.

**A. Job Queue:**
   - Contains all processes in the system.
   - Includes processes that are in the new, ready, waiting, running, and terminated states.

**B. Ready Queue:**
   - Contains all processes that are ready to run but are waiting for CPU time.
   - The OS scheduler selects processes from this queue to execute on the CPU.

**C. Waiting Queue (or Device Queue):**
   - Contains all processes that are waiting for a specific I/O device or event.
   - Each I/O device may have its own waiting queue.

### 3. Degree of Multiprogramming

**Degree of Multiprogramming:**
   - Refers to the number of processes in memory at one time.
   - Higher degrees of multiprogramming can improve CPU utilization by ensuring that there is always a process ready to execute when another process is waiting for I/O.

**A. Long-Term Scheduler (LTS):**
   - Also known as the job scheduler.
   - Controls the degree of multiprogramming by deciding which processes are admitted to the system for processing.
   - It selects processes from the job queue and loads them into memory, placing them in the ready queue.
   - The LTS runs less frequently than the short-term scheduler.

### 4. Dispatcher

**Dispatcher:**
   - A component of the OS responsible for moving processes between the ready and running states.
   - It handles the actual switching of processes on the CPU.
   - **Tasks of the Dispatcher:**
     - **Context Switching:** Saving the state of the currently running process and loading the state of the next process to run.
     - **Switching to User Mode:** Ensuring the process runs in user mode rather than kernel mode.
     - **Jumping to the Proper Location:** Setting the program counter to the appropriate location in the process to resume execution.

### Process State Transitions

A process can transition between different states based on events such as scheduling, I/O completion, or process termination. Here are the typical transitions:

1. **New to Ready:** When a new process is created and admitted by the long-term scheduler.
2. **Ready to Running:** When the short-term scheduler selects a process to run.
3. **Running to Waiting:** When a process needs to wait for I/O or an event.
4. **Running to Ready:** When a running process is preempted by the scheduler.
5. **Waiting to Ready:** When the event or I/O completion that a process was waiting for occurs.
6. **Running to Terminated:** When a process completes its execution.

### Summary

- **Process States:** Include new, running, waiting, ready, and terminated.
- **Process Queues:** Include job queue, ready queue, and waiting queue.
- **Degree of Multiprogramming:** Managed by the long-term scheduler (LTS), which controls the number of processes in memory.
- **Dispatcher:** Responsible for context switching and moving processes between ready and running states.

