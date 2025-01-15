# System Information Collector

This Python script is designed to gather and output information about the system, such as hardware, installed software, network configuration, environment variables, running services, and configuration files. 

## Features

- **System Information**: Displays details like OS, version, machine architecture, and processor information.
- **Users**: Lists the system users.
- **Network Information**: Gathers network configuration and ARP table data.
- **Environment Variables**: Displays all the environment variables set in the system.
- **Installed Software**: Lists all the installed software with their versions using Windows Management Instrumentation (WMI).
- **Services**: Lists the currently running services in the system.
- **Search Configuration Files**: Searches predefined directories for common configuration files (e.g., `.ini`, `.json`, `.xml`).
- **Output to File**: Saves the gathered information to a text file for future reference or analysis.

## How to Use

- **Run the Script**: Execute the script in a Python environment. You can specify the output file name using the `-o` or `--output` flag, otherwise it defaults to `output.txt`.

   Example:
   ```bash
   python system_info_collector.py -o system_report.txt

## Terminal 
![image](https://github.com/user-attachments/assets/d5bcf410-7e05-450d-a78a-584a43c87c6d)
