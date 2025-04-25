# DNS Lookup Utility - Documentation

## Overview
This Python script provides a command-line utility to perform DNS lookups (`nslookup`) in three different ways:
1. For a single domain or IP address
2. For a list of domains/IPs from a text file
3. For a range of IP addresses

The results are saved to a specified output file with detailed DNS information.

## Requirements
- Python 3.x
- Standard Python libraries:
  - `subprocess`
  - `ipaddress`

## Installation
No installation required. Simply download the script and run it with Python:
```bash
python dns_lookup.py
```

## Usage

### Running the Script
Execute the script from the command line:
```bash
python dns_lookup.py
```

You will be prompted to:
1. Enter an output filename (where results will be saved)
2. Choose an operation mode:
   - `1`: Lookup domains/IPs from a file
   - `2`: Lookup a range of IP addresses

### Functionality

#### 1. NSLookup from File
- Provide a text file with one domain or IP address per line
- The script will perform a detailed DNS lookup for each entry
- Results are appended to the output file

#### 2. NSLookup for IP Range
- Provide a starting and ending IP address
- The script will perform DNS lookups for all IPs in this range (inclusive)
- Results are appended to the output file

### Output Format
For each lookup, the output file contains:
- The queried address
- Detailed DNS records (ANY type)
- Or error messages if the lookup fails

## Functions

### `nslookup(address, output_file)`
Performs a detailed DNS lookup for a single address.

**Parameters:**
- `address`: Domain name or IP address to lookup
- `output_file`: File to append results to

### `nslookup_from_file(filename, output_file)`
Performs DNS lookups for each address in a file.

**Parameters:**
- `filename`: Text file containing addresses (one per line)
- `output_file`: File to append results to

### `nslookup_ip_range(start_ip, end_ip, output_file)`
Performs DNS lookups for all IPs in a specified range.

**Parameters:**
- `start_ip`: Starting IP address of the range
- `end_ip`: Ending IP address of the range
- `output_file`: File to append results to

## Example Usage

1. **From a file:**
   ```
   Enter the output filename: results.txt
   Choose an option:
   1. Perform nslookup from a file
   2. Perform nslookup for a range of IP addresses
   Enter your choice (1/2): 1
   Enter the filename with addresses: domains.txt
   ```

2. **IP range:**
   ```
   Enter the output filename: ip_results.txt
   Choose an option:
   1. Perform nslookup from a file
   2. Perform nslookup for a range of IP addresses
   Enter your choice (1/2): 2
   Enter the start IP address: 192.168.1.1
   Enter the end IP address: 192.168.1.10
   ```

## Notes
- The script uses `nslookup -type=ANY` to get all available DNS records
- Errors are captured and written to the output file
- IP range must be valid IPv4 addresses

