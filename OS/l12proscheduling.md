### Lecture 12: Introduction to Process Scheduling

Process scheduling is a critical function of the operating system that decides the order in which processes are executed by the CPU. Efficient scheduling ensures maximum CPU utilization and overall system performance.

### Point 1: Process Scheduling

**A. Basis of Multiprogramming OS:**
- Process scheduling is fundamental to multiprogramming operating systems.
- It allows multiple processes to share the CPU, increasing system utilization and efficiency.

**B. Makes Computer More Productive:**
- By managing the execution of processes, scheduling improves system responsiveness and throughput.
- It ensures that the CPU is always busy executing a process, minimizing idle time.

**C. Time Quantum Expires:**
- In time-sharing systems, each process is given a fixed time slice or quantum to execute.
- When the time quantum expires, the process is preempted, and the CPU is assigned to the next process in the ready queue.

### Point 2: CPU Scheduler

The CPU scheduler is responsible for selecting which process will run next on the CPU. It makes these decisions based on a specific scheduling algorithm.

### Point 3: Non-Preemptive and Preemptive Scheduling

**Non-Preemptive Scheduling:**
- In non-preemptive scheduling, a process runs to completion once it starts execution, or it voluntarily yields control of the CPU.
- **Cooperation Required:** Processes must cooperate by voluntarily relinquishing the CPU.
- **Drawbacks:**
  - **Starvation:** Low-priority processes may starve if high-priority processes keep arriving.
  - **Low CPU Utilization:** The CPU may be idle if the currently running process is waiting for I/O.

**Preemptive Scheduling:**
- In preemptive scheduling, the OS can forcibly remove a process from the CPU if a higher-priority process arrives or if the current process's time quantum expires.
- **Advantages:**
  - **Higher CPU Utilization:** Ensures the CPU is efficiently used by switching to ready processes.
  - **Improved Responsiveness:** Reduces waiting time for high-priority processes.
- **Drawbacks:**
  - **Context Switching Overhead:** Frequent context switches can add overhead.

### Goals of CPU Scheduling

The goals of CPU scheduling include maximizing CPU utilization, increasing throughput, and reducing response and waiting times.

**Metrics for Evaluating Scheduling Algorithms:**

1. **Throughput:**
   - The number of processes completed per unit of time.
   - Higher throughput indicates better performance.

2. **Arrival Time:**
   - The time at which a process arrives in the ready queue.

3. **Burst Time:**
   - The total time required by a process for execution on the CPU.

4. **Turnaround Time:**
   - The total time taken from process submission to process completion.
   - **Turnaround Time = Completion Time - Arrival Time**

5. **Wait Time:**
   - The total time a process spends in the ready queue waiting for CPU allocation.
   - **Wait Time = Turnaround Time - Burst Time**

6. **Response Time:**
   - The time from process submission until the first response is produced.
   - Important for interactive systems where quick feedback is crucial.

7. **Completion Time:**
   - The time at which a process completes its execution.

### FCFS (First-Come, First-Served) Scheduling

**Description:**
- Processes are executed in the order they arrive in the ready queue.
- **Simple and Easy to Implement:** No complex algorithms are required.

**Drawbacks:**
- **Convoy Effect:** Shorter processes waiting behind longer processes can lead to increased waiting time and reduced throughput.
- **Non-Preemptive:** Once a process starts executing, it runs to completion, which can lead to poor CPU utilization and long wait times for short processes.

**Example:**

Consider three processes with arrival times and burst times:

- **P1:** Arrival Time = 0, Burst Time = 24
- **P2:** Arrival Time = 2, Burst Time = 3
- **P3:** Arrival Time = 4, Burst Time = 3

**Gantt Chart:**

```
P1 |------------------------| P2 |---| P3 |---|
0                         24 27 30
```

**Calculations:**

- **Turnaround Time:**
  - **P1:** 24 - 0 = 24
  - **P2:** 27 - 2 = 25
  - **P3:** 30 - 4 = 26
- **Wait Time:**
  - **P1:** 0 (no waiting)
  - **P2:** 24 - 2 = 22
  - **P3:** 27 - 4 = 23

- **Average Wait Time:** (0 + 22 + 23) / 3 = 15
- **Average Turnaround Time:** (24 + 25 + 26) / 3 = 25

### Summary

- **Process Scheduling:** Fundamental for multiprogramming OS to improve productivity and manage time quantum expiration.
- **CPU Scheduler:** Selects the next process to run based on the scheduling algorithm.
- **Non-Preemptive Scheduling:** Requires cooperation and can lead to starvation and low CPU utilization.
- **Preemptive Scheduling:** Improves utilization and responsiveness but has context switching overhead.
- **Goals of Scheduling:** Include maximizing CPU utilization, throughput, and minimizing wait, turnaround, and response times.
- **FCFS Scheduling:** Simple but prone to the convoy effect, leading to inefficiencies in waiting and turnaround times.

This summary provides a comprehensive understanding of process scheduling, including the goals, types of scheduling, and an in-depth look at the FCFS scheduling algorithm and its drawbacks.