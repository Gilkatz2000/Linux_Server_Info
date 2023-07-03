import paramiko

global ssh
def connect_to_server(host, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    sftp = ssh.open_sftp()
    return ssh, sftp