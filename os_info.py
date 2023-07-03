def system_os_info(ssh):
    # Run a command on the remote system to get OS information
    stdin, stdout, stderr = ssh.exec_command("cat /etc/os-release")
    os_info = stdout.read().decode()

    # Look for the PRETTY_NAME field, which contains the OS name and version
    for line in os_info.split('\n'):
        if "PRETTY_NAME" in line:
            os_name = line.split('=')[1]
            return os_name
    return "Could not determine OS."
