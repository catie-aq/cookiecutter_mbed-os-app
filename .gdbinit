# GDB configuration file
# Usage:
# - Launch JLinkGDBServer first:
#   
#     JLinkGDBServer -device YOUR_DEVICE -if (swd|jtag)
#
# - Execute GDB with:
#
#     arm-none-eabi-gdb PATH/TO/ELF_FILE

# Connect to JLinkGdbServer
target remote localhost:2331

# Flash target
monitor reset
load

# Break on main
break main
continue

# Display Test User Interface
tui enable
