### Lecture 5: System Calls

System calls are the primary mechanism through which applications (running in user space) interact with the kernel (running in kernel space). These calls provide the necessary interface for programs to request services from the operating system.

### How Apps Interact with Kernels

**System Call Process:**
1. **Initiation:** An application initiates a system call when it needs to perform an operation that requires higher privileges, such as file manipulation or process creation.
2. **Transition:** The system call causes a transition from user mode to kernel mode. This is often done via a software interrupt or trap.
3. **Execution:** The kernel performs the requested operation.
4. **Return:** Once the operation is complete, control returns to the application, switching back to user mode.

**Example: Creating a Directory with `mkdir`**

1. **User Space Request:** An application calls the `mkdir` function from the standard library (e.g., `glibc` in Linux).
2. **System Call Invocation:** The `mkdir` function invokes the `syscall` instruction, specifying the system call number for `mkdir`.
3. **Kernel Mode Transition:** The `syscall` instruction triggers a software interrupt, causing a transition to kernel mode.
4. **Kernel Execution:** The kernel executes the `sys_mkdir` function to create the directory.
5. **Return to User Space:** The kernel returns the result of the operation to the application, switching back to user mode.

### Transition from User Space to Kernel Space by Software Interrupts

Software interrupts (or traps) are mechanisms to handle the transition from user space to kernel space. They are used to safely switch contexts and provide controlled access to system resources.

**Example:**
1. **System Call Trigger:** An application needs to perform an action requiring kernel intervention.
2. **Trap Instruction:** The application executes a trap instruction (e.g., `int 0x80` in x86 assembly for Linux).
3. **Interrupt Handling:** The CPU switches to kernel mode and jumps to the appropriate interrupt handler.
4. **System Call Handling:** The kernel performs the requested operation.
5. **Return to User Space:** The kernel returns control to the application in user space.

### Types of System Calls

1. **Process Control:**
   - **Examples:** `fork`, `exec`, `exit`, `wait`.
   - **Use Case:** Creating and terminating processes, loading and executing programs.
   - **Example:** In UNIX, `fork()` creates a new process, `exec()` replaces the current process image with a new one.

2. **File Management:**
   - **Examples:** `open`, `read`, `write`, `close`.
   - **Use Case:** Manipulating files and directories.
   - **Example:** `open()` opens a file, `read()` reads data from a file, `write()` writes data to a file.

3. **Device Management:**
   - **Examples:** `ioctl`, `read`, `write`.
   - **Use Case:** Interacting with hardware devices.
   - **Example:** `ioctl()` performs various control operations on devices.

4. **Information Maintenance:**
   - **Examples:** `getpid`, `alarm`, `sleep`, `time`.
   - **Use Case:** Retrieving system and process information.
   - **Example:** `getpid()` returns the process ID, `time()` returns the current time.

5. **Communication Management:**
   - **Examples:** `pipe`, `shmget`, `mmap`, `msgget`, `socket`.
   - **Use Case:** Facilitating communication between processes.
   - **Example:** `socket()` creates a communication endpoint, `pipe()` creates a unidirectional data channel.

### System Calls in Windows and UNIX

**Windows System Calls:**
- **Example:** Creating a process
  - **Function:** `CreateProcess`
  - **Use Case:** Starts a new process and its primary thread.
  - **System Call Flow:**
    1. The application calls `CreateProcess`.
    2. The Windows API forwards the request to the kernel mode using a software interrupt.
    3. The kernel executes the `NtCreateProcess` function.
    4. The process is created, and control is returned to the application.

**UNIX System Calls:**
- **Example:** Creating a process
  - **Function:** `fork`
  - **Use Case:** Creates a new process by duplicating the existing process.
  - **System Call Flow:**
    1. The application calls `fork()`.
    2. A software interrupt triggers the transition to kernel mode.
    3. The kernel executes the `sys_fork` function, duplicating the process.
    4. The new process ID is returned to the parent process.

### Example System Call Flows

**Creating a Process in UNIX:**
```c
pid_t pid;
pid = fork(); // Creates a new process
if (pid == 0) {
    // Child process
    execl("/bin/ls", "ls", (char *)0); // Replaces the process image
} else {
    // Parent process
    wait(NULL); // Waits for the child process to finish
}
```

**Creating a File in Windows:**
```c
HANDLE hFile;
hFile = CreateFile(
    "example.txt",                // Name of the file
    GENERIC_WRITE,                // Open for writing
    0,                            // Do not share
    NULL,                         // Default security
    CREATE_NEW,                   // Create new file only
    FILE_ATTRIBUTE_NORMAL,        // Normal file
    NULL                          // No attribute template
);
if (hFile == INVALID_HANDLE_VALUE) {
    // Handle error
} else {
    // Write to the file
    CloseHandle(hFile);
}
```

### Summary

- **System Calls:** Mechanism for user space applications to request services from the kernel.
- **Transition:** Involves a context switch from user mode to kernel mode using software interrupts or traps.
- **Types:** Include process control, file management, device management, information maintenance, and communication management.
- **Examples:** Differ between Windows and UNIX but serve similar purposes.

