import socket
import pandas as pd
from os_info import system_os_info
from cpu_info import get_cpu_info
from motherboard import get_remote_server_motherboard_info
from connect_to_server import connect_to_server
from get_user_cridentials import get_user_credentials
from system_names_list import technician_lab_servers

def is_server_online(server_address, port):
    # Checks if a server is online or offline by attempting to connect to it.
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # set a timeout of 5 seconds for the connection
        result = sock.connect_ex((server_address, port))
        if result == 0:
            return True
        else:
            return False
    except:
        return False

def get_server_information():
    # Technician Lab systems
    online_servers = []
    offline_servers = []

    # Get user credentials once
    system_name_host, port, username, password = get_user_credentials()

    for system_name in technician_lab_servers:
        if is_server_online(system_name + '.jer.intel.com', 22):
            ssh, sftp = connect_to_server(system_name + '.jer.intel.com', port, username, password)
            os_info = system_os_info(ssh)
            cpu_info = get_cpu_info(ssh)
            motherboard_info = get_remote_server_motherboard_info(system_name + '.jer.intel.com', username, password)
            server_info = {
                'Server Name': system_name,
                'Status': 'Online',
                'OS': os_info if os_info else "",
                'CPU': cpu_info if cpu_info else "",
                'Motherboard': motherboard_info
            }
            online_servers.append(server_info)
        else:
            server_info = {
                'Server Name': system_name,
                'Status': 'Offline',
                'OS': '',
                'CPU': '',
                'Motherboard': ''
            }
            offline_servers.append(server_info)

    # Create DataFrame
    columns = ['Server Name', 'Status', 'OS', 'CPU', 'Motherboard']
    data = online_servers + offline_servers
    df = pd.DataFrame(data, columns=columns)

    return df

# Call the function to get server information
server_info_df = get_server_information()

# Save to Excel file
file_path = '/home/laduser/Desktop/server_info.xlsx'  # Replace with the desired file path on your local system
server_info_df.to_excel(file_path, index=False)

print(f"Server information exported to {file_path}")
server_info_dfa = get_server_information()
server_info_dfa