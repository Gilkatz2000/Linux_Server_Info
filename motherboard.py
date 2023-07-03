import paramiko

def get_remote_server_motherboard_info(server_address, username, password):
    # Establish SSH connection to the remote server
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_address, username=username, password=password)

    # Run dmidecode command
    stdin, stdout, stderr = ssh.exec_command('sudo dmidecode -t baseboard')
    output = stdout.read().decode().strip()

    # Parse output for motherboard info
    company_name = None
    model_name = None
    for line in output.split('\n'):
        if 'Manufacturer:' in line:
            company_name = line.strip().split(':')[-1].strip()
        elif 'Product Name:' in line:
            model_name = line.strip().split(':')[-1].strip()

    # Close the SSH connection
    ssh.close()

    # Return motherboard info
    if company_name and model_name:
        return f"Motherboard: {company_name} {model_name}"
    else:
        return "Motherboard info not found."
