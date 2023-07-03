from connect_to_server import connect_to_server

def get_cpu_info(ssh):
    # Run lscpu command and search for 'Model name'
    stdin, stdout, stderr = ssh.exec_command('lscpu')
    output = stdout.read().decode().strip()

    # Search for 'Model name' in the output
    model_name = [line.split(':')[1].strip() for line in output.split('\n') if 'Model name' in line]

    # Return model name as a string
    return ", ".join(model_name)
