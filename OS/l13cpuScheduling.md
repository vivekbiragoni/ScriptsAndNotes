### Lecture 13: CPU Scheduling Algorithms

Understanding different CPU scheduling algorithms helps in optimizing CPU utilization, improving process responsiveness, and balancing the load among processes. Here we discuss Shortest Job First (SJF), Priority Scheduling, and Round Robin (RR) Scheduling.

### 1. Shortest Job First (SJF) Scheduling

#### SJF Non-Preemptive

**Description:**
- Selects the process with the shortest burst time next for execution.
- Once a process starts executing, it runs to completion.

**Advantages:**
- Minimizes average waiting time.

**Drawbacks:**
- Cannot handle processes arriving after the start of execution.
- Can lead to starvation for longer processes.

**Example:**

Consider three processes with burst times:
- **P1:** Burst Time = 6
- **P2:** Burst Time = 8
- **P3:** Burst Time = 7
- **P4:** Burst Time = 3

**Gantt Chart:**
```
P4 |---| P1 |------| P3 |------| P2 |--------|
0     3        9         16       24
```

**Flow Chart:**

```
Start -> Check Burst Times
      -> Select Process with Shortest Burst Time
      -> Execute Process to Completion
      -> Repeat Until All Processes are Complete
```

#### SJF Preemptive (Shortest Remaining Time First, SRTF)

**Description:**
- Preempts the currently executing process if a new process arrives with a shorter burst time remaining than the current process's remaining time.

**Advantages:**
- Can handle new processes arriving dynamically.
- More responsive than non-preemptive SJF.

**Drawbacks:**
- Increased complexity due to preemption.
- Still can lead to starvation for longer processes.

**Example:**

Consider three processes with arrival and burst times:
- **P1:** Arrival Time = 0, Burst Time = 8
- **P2:** Arrival Time = 1, Burst Time = 4
- **P3:** Arrival Time = 2, Burst Time = 9
- **P4:** Arrival Time = 3, Burst Time = 5

**Gantt Chart:**
```
P1 |-| P2 |----| P4 |----| P1 |------| P3 |--------|
0   1     5     9          17      26
```

**Flow Chart:**

```
Start -> Check Arrival and Burst Times
      -> Select Process with Shortest Remaining Burst Time
      -> Preempt Current Process if Needed
      -> Execute Until Process Completion or Preemption
      -> Repeat Until All Processes are Complete
```

### 3. Priority Scheduling

#### Priority Scheduling Non-Preemptive

**Description:**
- Selects the process with the highest priority for execution.
- Processes with the same priority are scheduled based on arrival time.

**Advantages:**
- Simple to implement.
- Suitable for systems with predictable workloads.

**Drawbacks:**
- Can lead to starvation for low-priority processes.

**Example:**

Consider four processes with priorities (higher number indicates higher priority):
- **P1:** Priority = 1, Burst Time = 10
- **P2:** Priority = 4, Burst Time = 1
- **P3:** Priority = 3, Burst Time = 2
- **P4:** Priority = 2, Burst Time = 1

**Gantt Chart:**
```
P2 |-| P3 |--| P4 |-| P1 |----------|
0   1    3    4    5       15
```

**Flow Chart:**

```
Start -> Check Priorities
      -> Select Process with Highest Priority
      -> Execute Process to Completion
      -> Repeat Until All Processes are Complete
```

#### Priority Scheduling Preemptive

**Description:**
- Preempts the currently running process if a new process arrives with a higher priority.

**Advantages:**
- Ensures high-priority processes are executed as soon as they arrive.
- More responsive to urgent tasks.

**Drawbacks:**
- Increased complexity due to preemption.
- Can lead to starvation for low-priority processes.

**Example:**

Consider four processes with priorities and arrival times:
- **P1:** Arrival Time = 0, Priority = 1, Burst Time = 10
- **P2:** Arrival Time = 1, Priority = 4, Burst Time = 1
- **P3:** Arrival Time = 2, Priority = 3, Burst Time = 2
- **P4:** Arrival Time = 3, Priority = 2, Burst Time = 1

**Gantt Chart:**
```
P1 |-| P2 |-| P3 |--| P4 |-| P1 |----------|
0   1   2    4    5      6    16
```

**Flow Chart:**

```
Start -> Check Priorities and Arrival Times
      -> Select Process with Highest Priority
      -> Preempt Current Process if Needed
      -> Execute Until Process Completion or Preemption
      -> Repeat Until All Processes are Complete
```

### 5. Round Robin (RR) Scheduling

**Description:**
- Each process is assigned a fixed time slice or quantum.
- Processes are executed in a cyclic order, and preempted after their time quantum expires.

**Advantages:**
- Fair allocation of CPU time.
- Good for time-sharing systems and interactive environments.

**Drawbacks:**
- Performance depends on the length of the time quantum.
- Too short time quantum increases context switching overhead, too long increases response time.

**Example:**

Consider four processes with burst times:
- **P1:** Burst Time = 4
- **P2:** Burst Time = 3
- **P3:** Burst Time = 2
- **P4:** Burst Time = 1

Assume a time quantum of 2.

**Gantt Chart:**
```
P1 |--| P2 |--| P3 |- | P4 |- | P1 |- | P2 |
0    2    4    6    7    8    9   11
```

**Flow Chart:**

```
Start -> Initialize Ready Queue
      -> Select First Process in Queue
      -> Execute for Time Quantum or Until Completion
      -> Move to Next Process in Queue
      -> Repeat Until All Processes are Complete
```

### Summary

1. **SJF Non-Preemptive:**
   - Selects the shortest burst time.
   - Simple but can cause starvation.
   - Gantt Chart: Process with the shortest burst time executes first.
   - Flow Chart: Check Burst Times -> Execute Shortest -> Repeat.

2. **SJF Preemptive:**
   - Preempts if a new process with a shorter remaining time arrives.
   - More dynamic but complex.
   - Gantt Chart: Process with the shortest remaining burst time executes.
   - Flow Chart: Check Arrival and Burst Times -> Preempt if Needed -> Execute.

3. **Priority Scheduling Non-Preemptive:**
   - Selects the highest priority process.
   - Simple but can cause starvation.
   - Gantt Chart: Process with the highest priority executes first.
   - Flow Chart: Check Priorities -> Execute Highest Priority -> Repeat.

4. **Priority Scheduling Preemptive:**
   - Preempts if a new higher priority process arrives.
   - More responsive but complex.
   - Gantt Chart: Highest priority process executes.
   - Flow Chart: Check Priorities -> Preempt if Needed -> Execute.

5. **Round Robin Scheduling:**
   - Fixed time slice for each process in cyclic order.
   - Fair but performance depends on time quantum.
   - Gantt Chart: Processes executed in cyclic order for fixed time quantum.
   - Flow Chart: Initialize Ready Queue -> Execute for Time Quantum -> Move to Next -> Repeat.

This comprehensive summary provides a detailed overview of each scheduling algorithm along with examples, advantages, drawbacks, and flow charts to visualize their operations.