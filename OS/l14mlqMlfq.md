### Lecture 14: Multilevel Queue (MLQ) and Multilevel Feedback Queue (MLFQ) Scheduling

### 1. Multilevel Queue (MLQ) Scheduling

**Point 1: MLQ Overview**

**A. Ready Queue is Divided into Multiple Queues Depending on Priority:**
- The system classifies processes into different priority levels.
- Each priority level has its own queue.

**B. Process is Permanently Assigned to One of the Queues Based on Some Property:**
- Processes are assigned to a queue based on their type or other characteristics, such as system process, interactive process, or batch process.
- Once assigned, processes do not move between queues.

**C. Each Queue has Its Own Scheduling Algorithm:**
- Different queues can use different scheduling algorithms to meet specific needs.
  - **System Processes (Highest Priority):** Can use a scheduling algorithm like SPQ (Shortest Process Queue).
  - **Interactive Processes:** Can use RR (Round Robin) to ensure responsiveness.
  - **Batch Processes (Lowest Priority):** Can use FCFS (First-Come, First-Served) for simplicity.

**D. Example Flowchart:**

```
System Process Queue (SPQ) -> Interactive Process Queue (IPQ) -> Batch Process Queue (BPQ)
    SPQ: Highest Priority Queue using SPQ
    IPQ: Medium Priority Queue using RR
    BPQ: Lowest Priority Queue using FCFS
```

**E. Fixed Priority Pre-emptive Scheduling:**
- Processes in higher priority queues preempt those in lower priority queues.

**F. Interactive Process Comes and Batch Process is Currently Executing:**
- The batch process is preempted, and the interactive process is given CPU time.

**G. Problem: Starvation of Low-Priority Processes:**
- Low-priority processes may starve because higher priority queues are always serviced first.
- **Convoy Effect:** Low-priority processes may experience delays if a large number of high-priority processes are present.

### 2. Multilevel Feedback Queue (MLFQ) Scheduling

**Overview:**
- MLFQ addresses the drawbacks of MLQ by allowing processes to move between queues based on their behavior and waiting time.

**A. Multiple Sub Queues:**
- Each queue represents a different priority level.

**B. Process Movement Between Queues:**
- Processes can move between queues based on their execution history and waiting time.

**C. Aging to Prevent Starvation:**
- If a process waits too long in a low-priority queue, it is moved to a higher priority queue to ensure it eventually gets CPU time.

**D. Configurable Design:**
- MLFQ can be tuned to match specific system design requirements, such as time slices for each queue and criteria for moving processes between queues.

**Example MLFQ Design:**
1. **Top-Level Queue (Q1):** Uses RR with a small time quantum for interactive processes.
2. **Middle-Level Queue (Q2):** Uses RR with a larger time quantum for less interactive processes.
3. **Bottom-Level Queue (Q3):** Uses FCFS for batch processes.

**Flowchart:**

```
Top-Level Queue (Q1, RR) -> Middle-Level Queue (Q2, RR) -> Bottom-Level Queue (Q3, FCFS)
    - Processes can move from Q1 to Q2 if they exceed their time quantum.
    - Processes can move from Q2 to Q3 if they exceed their time quantum.
    - Processes in Q3 may be promoted to Q2 if they wait too long (aging).
```

### Comparison of Scheduling Algorithms

1. **FCFS (First-Come, First-Served):**
   - **Description:** Processes are scheduled in the order they arrive.
   - **Advantages:** Simple and easy to implement.
   - **Disadvantages:** Convoy effect, can lead to poor CPU utilization and long wait times for short processes.

2. **SJF (Shortest Job First):**
   - **Description:** Selects the process with the shortest burst time.
   - **Advantages:** Minimizes average waiting time.
   - **Disadvantages:** Requires knowledge of burst times, can lead to starvation of longer processes.

3. **PSJF (Preemptive Shortest Job First):**
   - **Description:** Preempts the current process if a new process with a shorter burst time arrives.
   - **Advantages:** More responsive than SJF, minimizes average waiting time.
   - **Disadvantages:** Complex to implement, can lead to frequent context switches.

4. **Priority Scheduling:**
   - **Description:** Selects the process with the highest priority.
   - **Advantages:** Ensures critical processes get CPU time.
   - **Disadvantages:** Can lead to starvation of low-priority processes.

5. **Preemptive Priority Scheduling:**
   - **Description:** Preempts the current process if a new higher-priority process arrives.
   - **Advantages:** More responsive to urgent tasks.
   - **Disadvantages:** Increased complexity and potential for frequent context switches.

6. **Round Robin (RR):**
   - **Description:** Each process is assigned a fixed time quantum in a cyclic order.
   - **Advantages:** Fair allocation of CPU time, good for time-sharing systems.
   - **Disadvantages:** Performance depends on the length of the time quantum.

7. **Multilevel Feedback Queue (MLFQ):**
   - **Description:** Multiple queues with different priorities, processes can move between queues.
   - **Advantages:** Reduces starvation, adaptable to different workloads, can be configured for specific requirements.
   - **Disadvantages:** Complex to implement and configure.

### Summary

**MLQ Scheduling:**
- **Structure:** Multiple fixed priority queues with different scheduling algorithms.
- **Advantages:** Simple to implement, allows different types of processes to be handled differently.
- **Drawbacks:** Starvation of low-priority processes, convoy effect.

**MLFQ Scheduling:**
- **Structure:** Multiple queues with dynamic priority adjustment.
- **Advantages:** Reduces starvation, adaptable, prevents long waits for low-priority processes.
- **Drawbacks:** Complex to implement and configure.

**Flowcharts:**

**MLQ Flowchart:**

```
Start -> Process Assigned to Queue (Based on Priority)
      -> Execute Processes in Highest Priority Queue (Using Queue's Scheduling Algorithm)
      -> Move to Next Lower Priority Queue if Higher Priority Queue is Empty
      -> Repeat Until All Processes are Complete
```

**MLFQ Flowchart:**

```
Start -> Process Assigned to Top-Level Queue
      -> Execute Process for Time Quantum
      -> Move Process to Lower Queue if Time Quantum Exceeds
      -> Promote Process if it Waits Too Long (Aging)
      -> Repeat Until All Processes are Complete
```

This summary provides an in-depth comparison and explanation of MLQ and MLFQ scheduling, their advantages, disadvantages, and operational flow.