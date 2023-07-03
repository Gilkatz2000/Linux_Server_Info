import socket
from connect_to_server import connect_to_server
from get_user_cridentials import get_user_credentials
from system_names_list import firmware_lab_servers

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

def online_status():
    # Technician Lab systems
    online_servers = 0
    offline_servers = 0

    # Get user credentials once
    system_name_host, port, username, password = get_user_credentials()

    firmware_lab_input = input("\nWould you like to view th Firmware Lab Servers? Y or N: ")
    online_servers = 0
    offline_servers = 0
    if firmware_lab_input == "y":
        for system_name in firmware_lab_servers:
            if is_server_online(system_name + '.jer.intel.com', 22):
                ssh, sftp = connect_to_server(system_name + '.jer.intel.com', port, username, password)
                print(system_name + " successfully connected")
                online_servers += 1
            else:
                print(system_name + " failed to connect")
                offline_servers += 1
    else:
        print("script is completed! ")

    print("Here are the results for testing Firmware Lab Servers: ")
    print("\nThere are online {} servers".format(online_servers))
    print("\nThere are offline {} servers".format(offline_servers))
online_status()
