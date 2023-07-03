import subprocess

def get_network_card_name():
    # Run ip command and search for network card name
    command_output = subprocess.run(['ip', 'link'], capture_output=True, text=True)
    
    # Parse the output to find the network card name
    card_name = [line.split(':')[1].strip() for line in command_output.stdout.split('\n') if 'state UP' in line]

    # Check if we found a network card name
    if card_name:
        return card_name[0]
    else:
        return None

def main():
    card_name = get_network_card_name()

    if card_name is not None:
        print("Network card name: ", card_name)
    else:
        print("No network card found")

if __name__ == "__main__":
    main()
