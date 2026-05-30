# alTogether — Python Security Scanning Case Builder

alTogether is a Python command-line tool that automates authorized security scanning workflows for lab and assessment environments. The tool accepts a target IP address, validates the input, creates a dedicated case folder, runs multiple reconnaissance and vulnerability assessment tools, and saves the results into organized output files.

> **Authorized Use Only:** This tool is intended for educational labs and authorized security testing environments. Do not run scans against systems you do not own or do not have explicit permission to assess.

## Tools Integrated

- Nmap service and script scan
- Nmap vulners vulnerability scan
- WHOIS lookup
- SSLScan
- Nikto web server scan
- WPScan WordPress scan

## Features

- Accepts an IP address as a command-line argument or prompts the user for input
- Validates IPv4 address format before running scans
- Creates a dedicated `Case_[IP_address]` folder
- Runs multiple security scanning tools automatically
- Saves each scan result into a separate output file for review and documentation

## Usage

Run with an IP address:

```bash
python3 alTogether.py <target_ip>
