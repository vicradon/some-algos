def get_file_content(filelocation):
    try:
        with open(filelocation, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("The file was not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")  


def print_ip_and_interfaces(filecontent):
    if not filecontent:
        print("No file content was supplied")
        return
    
    lines = filecontent.split("\n")
    ip_addresses = ["IP-Addresses"]
    assigned_interfaces = ["Interfaces"]

    for line in lines:
        sections = line.split()

        if sections and sections[1][0:3] == "10.":
            ip_addresses.append(sections[1])
            assigned_interfaces.append(sections[0])

    ip_addresses_output = "\n".join(ip_addresses)
    assigned_interfaces_output = "\n".join(assigned_interfaces)

    print(ip_addresses_output)
    print("\n")
    print(assigned_interfaces_output)



if __name__ == "__main__":
    '''
    This script expects a file location inputed as a variable
    It outputs the ip addresses and interfaces that those addresses are assigned to
    '''
    filelocation = "./show_ip_int_brief.txt"
    filecontent = get_file_content(filelocation)
    print_ip_and_interfaces(filecontent) 