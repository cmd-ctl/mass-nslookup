import subprocess
import ipaddress

def nslookup(address, output_file):
    # nslookup for the given address with detailed information
    try:
        result = subprocess.run(["nslookup", "-type=ANY", address], capture_output=True, text=True, check=True)
        with open(output_file, "a") as file:
            file.write(f"\n Results for {address} (detailed):\n")
            file.write(result.stdout)
    except subprocess.CalledProcessError as e:
        with open(output_file, "a") as file:
            file.write(f"\n Error performing nslookup for {address}: {e}\n")


def nslookup_from_file(filename, output_file):
    # nslookup for each address in a file
    try:
        with open(filename, "r") as file:
            for line in file:
                address = line.strip()
                if address:
                    print(f"\n Performing nslookup for: {address}")
                    nslookup(address, output_file)
    except FileNotFoundError:
        print(f"File {filename} not found.")


def nslookup_ip_range(start_ip, end_ip, output_file):
    # nslookup for a range of IP addresses
    try:
        start = ipaddress.IPv4Address(start_ip)
        end = ipaddress.IPv4Address(end_ip)

        for ip in range(int(start), int(end) + 1):
            ip_str = str(ipaddress.IPv4Address(ip))
            print(f"\n Performing nslookup for: {ip_str}")
            nslookup(ip_str, output_file)

    except ipaddress.AddressValueError as e:
        print(f"Invalid IP address: {e}")


def main():
    output_file = input("Enter the output filename: ")
    print("Choose an option:")
    print("1. Perform nslookup from a file")
    print("2. Perform nslookup for a range of IP addresses")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        filename = input("Enter the filename with addresses: ")
        nslookup_from_file(filename, output_file)
    elif choice == "2":
        start_ip = input("Enter the start IP address: ")
        end_ip = input("Enter the end IP address: ")
        nslookup_ip_range(start_ip, end_ip, output_file)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
