# README.md file

## Project Overview

This project provides a suite of Python scripts that connect to a list of servers, check their online status and collect information about their operating system, CPU, and motherboard. The information is then exported to an Excel file.

The project includes the following Python scripts:
connect_to_server.py

This script provides a function connect_to_server(host, port, username, password) to establish an SSH connection to a remote server. It utilizes the paramiko library for SSH connectivity.
cpu_info.py

This script includes a function get_cpu_info(ssh) that executes the 'lscpu' command on the remote server and returns the CPU model.
get_user_credentials.py

This script provides a function get_user_credentials() that prompts the user to enter their credentials. The credentials are used to establish SSH connections to remote servers.
motherboard.py

This script includes a function get_remote_server_motherboard_info(server_address, username, password) that connects to a remote server and fetches information about the motherboard by executing the 'sudo dmidecode -t baseboard' command.
os_info.py

This script provides a function system_os_info(ssh) that executes the 'cat /etc/os-release' command on the remote server to get operating system information.
system_names_list.py

This script includes a list technician_lab_servers that holds the names of the servers the scripts connect to.
system_online_status.py

This script checks whether each server in the technician_lab_servers list is online or offline. If the server is online, it fetches its operating system, CPU, and motherboard information. This information is compiled into a pandas DataFrame and exported to an Excel file.
Usage

    Run python3 system_online_status.py
    Enter your username and password when prompted.
    Wait for the script to connect to each server, check its status and gather information.
    Find the output Excel file with the server information at the specified path.

## Dependencies

    Python 3.6 or above
    paramiko library for SSH connectivity
    getpass for secure password input
    pandas for data manipulation and analysis
    openpyxl for writing to Excel files

## Notes

    You need to have SSH access to the servers listed in technician_lab_servers.
    The script currently uses 'laduser' and the path '/home/laduser/Desktop/server_info.xlsx' to save the Excel file. You may want to change these to match your environment.
    The scripts are designed to run on Unix-like systems, including Linux and MacOS. If you're using a different system, you may need to modify the scripts.
    For the scripts to work, all the Python files should be in the same directory.