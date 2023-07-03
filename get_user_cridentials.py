import getpass

def get_user_credentials():
    """Prompts the user to enter their credentials and returns them as a tuple."""
    system_name_host = ""
    port = 22
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    return (system_name_host, port, username, password)