### Lecture 6: What Happens When You Turn on Your Computer?

When you turn on your computer, several steps take place to initialize the hardware and load the operating system. Here’s a detailed breakdown of this process:

### Step 1: Power On

1. **Power Button Pressed:**
   - The power button is pressed, and the computer's power supply unit (PSU) activates, providing power to the motherboard and all connected components.

### Step 2: BIOS/UEFI Initialization

2. **BIOS/UEFI Execution:**
   - The CPU is initialized and begins executing code stored in the Basic Input/Output System (BIOS) or Unified Extensible Firmware Interface (UEFI) firmware. This firmware is located on a chip on the motherboard.

3. **Power-On Self Test (POST):**
   - The BIOS/UEFI performs a Power-On Self Test (POST) to check the basic functionality of the system hardware, including the CPU, RAM, and connected devices.
   - If POST fails, error codes or beeps are generated to indicate the problem.

### Step 3: CPU Runs BIOS/UEFI

4. **Hardware Initialization:**
   - The BIOS/UEFI initializes the system hardware and configures system settings. It checks for the presence of essential hardware components and configures them to a known state.

5. **Boot Device Selection:**
   - The BIOS/UEFI searches for a bootable device (e.g., hard drive, SSD, USB drive) based on the boot order specified in the firmware settings.

### Step 4: Bootloader Initialization

6. **Bootloader Execution:**
   - Once a bootable device is found, the BIOS/UEFI loads and executes the bootloader from the Master Boot Record (MBR) or the GUID Partition Table (GPT).
   - The bootloader is a small program responsible for loading the operating system kernel into memory.

### OS Bootloader Examples:

1. **MBR (Master Boot Record):**
   - Located in the first 512 bytes of the storage device.
   - Contains the bootloader code and partition table.

2. **GRUB (Grand Unified Bootloader):**
   - A popular bootloader used by many Linux distributions.
   - Can load multiple operating systems and offers a menu to select between them.

3. **BOOTMGR (Windows Boot Manager):**
   - Used by Windows to load the operating system.
   - Located in the MBR and can boot different versions of Windows.

4. **boot.efi:**
   - Used by macOS and other UEFI-compatible systems.
   - Located in the EFI System Partition and loads the OS kernel for UEFI-based systems.

### Detailed Boot Process:

1. **MBR Bootloader:**
   - **Location:** The first 512 bytes of the bootable storage device.
   - **Function:** Loads the bootloader code and the partition table.
   - **Transition:** Hands off control to the bootloader (e.g., GRUB, BOOTMGR).

2. **GRUB (Linux):**
   - **Stage 1:** Located in the MBR or EFI System Partition. Loads Stage 2 of GRUB.
   - **Stage 2:** Displays a menu to select the operating system and loads the selected OS kernel into memory.
   - **Kernel Load:** Transfers control to the Linux kernel, which initializes the rest of the system.

3. **BOOTMGR (Windows):**
   - **Location:** Loaded by the MBR.
   - **Function:** Reads the Boot Configuration Data (BCD) and displays a boot menu if multiple OS installations are present.
   - **Kernel Load:** Loads the Windows kernel (ntoskrnl.exe) and transfers control.

4. **boot.efi (macOS/UEFI systems):**
   - **Location:** In the EFI System Partition.
   - **Function:** Loads the OS kernel for macOS or other UEFI-compatible operating systems.
   - **Kernel Load:** Transfers control to the OS kernel.

### Post-Bootloader Steps:

1. **Kernel Initialization:**
   - The OS kernel initializes hardware drivers and system components.
   - Sets up memory management and process scheduling.
   - Loads essential system services and daemons.

2. **User Space Initialization:**
   - The kernel starts the initial system process (e.g., `init` on UNIX/Linux or `wininit` on Windows).
   - This process starts other user-space processes and services, including the graphical user interface (GUI) if applicable.

3. **Login Prompt:**
   - The system displays a login prompt or GUI login screen for the user to authenticate.
   - Upon successful login, user-specific settings and applications are loaded.

### Summary:

- **Step 1: Power On** - The computer receives power and initializes.
- **Step 2: BIOS/UEFI Initialization** - The BIOS/UEFI firmware performs POST and hardware initialization.
- **Step 3: CPU Runs BIOS/UEFI** - The BIOS/UEFI selects the boot device and loads the bootloader.
- **Step 4: Bootloader Initialization** - The bootloader (e.g., GRUB, BOOTMGR, boot.efi) loads the OS kernel into memory.
- **Post-Bootloader Steps** - The kernel initializes system components and starts user-space processes, leading to the login prompt.

