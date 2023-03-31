#!/usr/bin/python3 

# psutil
# Stanley L. Ferguson III
# 3 Mar 2023
# create a scrip that fetches info in python

import psutil

# Get CPU times
cpu_times = psutil.cpu_times()
# Time spent by normal processes executing in user mode
print("Time spent by normal processes executing in user mode:")
print(cpu_times.user)
# Time spent by processes executing in kernel mode
print("Time spent by processes executing in kernel mode:")
print(cpu_times.system)
# Time when system was idle
print("Time when system was idle:")
print(cpu_times.idle)
# Time spent by priority processes executing in user mode
print("Time spent by priority processes executing in user mode:")
print(cpu_times.nice)
# Time spent waiting for I/O to complete.
print("Time spent waiting for I/O to complete:")
print(cpu_times.iowait)
# Time spent for servicing hardware interrupts
print("Time spent for servicing hardware interrupts:")
print(cpu_times.irq)
# Time spent for servicing software interrupts
print("Time spent for servicing software interrupts:")
print(cpu_times.softirq)
# Time spent by other operating systems running in a virtualized environment
print("Time spent by other operating systems running in a virtualized environment:")
print(cpu_times.steal)
# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:")
print(cpu_times.guest)
