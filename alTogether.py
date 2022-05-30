# alTogether app v1.0
# Variety of Scanning with only given IP address ...
# alTogether can take IP 
   
import os
import sys

# Prints Welcome Screen

print("*"*50 + "\n" + "\n\talTogether PenTest Case Builder App v1.0" + "\n\n" + "*"*50)

ip_address = ""

# Validate the IP addresses  

def validate_ip(s):
    ip_address = s.split('.')
    if len(ip_address) != 4:
        return False
    for x in ip_address:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True
try:
    if (validate_ip(sys.argv[1])):    # Validating the argument IP 
        ip_address = sys.argv[1]
    else:
        print("Enter a valid IP address"+ "\n")
        raise Exception("IP address is not valid")
except:    
    while not validate_ip(ip_address): # Program will keep asking for IP address unless it gets a valid IP address!
        ip_address = input("Which IP address would you like to create a Case: ")

# checking for the directory, if it does not exist will create a new folder with a name format Case_[IP address]
def case():
    case_dir = (f"Case_{ip_address}")
    check_dir = os.path.isdir(case_dir) 
    if not check_dir:
        os.mkdir(f"Case_{ip_address}")
    else:
        pass

# This function does nmap-nikto-sslscan-whois-nmapVuln scans && saves the outputs with respected file name within the case folder:

def main():
    print("\n" + "*"*50 + "\n" + f"initalizing nmap scan for {ip_address}" + "\n" + "Warning this nmap scan needs root privileges; If prompted:type your password and hit enter" + "\n\n" + "*"*50)
    os.system(f"sudo nmap -sV -sC -Pn -A {ip_address} > Case_{ip_address}/nmapscanresults.txt")
    print(f"Detailed nmap scan results for {ip_address} is succesfully saved as nmapscanresults.txt file" + "\n" + "*"*50) 
    
    print("\n" + "\n" + f"initalizing nmap VULN scan for {ip_address}" + "\n" + "Warning this nmap scan needs root privileges; If prompted:type your password and hit enter" + "\n\n" + "*"*50)
    os.system(f"sudo nmap -sV --script vulners {ip_address} > Case_{ip_address}/nmapVulnScanResults.txt")
    print(f"Detailed nmap Vulnerability scan results for {ip_address} is succesfully saved as nmapVulnScanResults.txt file" + "\n" + "*"*50)
    
    print("\n" + "\n" + f"initalizing whois scan for {ip_address}" + "\n")
    os.system(f"whois {ip_address} > Case_{ip_address}/whoisscanresults.txt")
    print(f"whois scan result for {ip_address} succesfully saved as whoisscanresults.txt file" + "\n" + "*"*50) 
    
    print("\n" + "\n" + f"initalizing SSLscan for {ip_address}" + "\n")
    os.system(f"sslscan {ip_address} > Case_{ip_address}/SSLscanresults.txt")
    print(f"Detailed SSLscan result for {ip_address} is succesfully saved as SSLscanresults.txt file" + "\n" + "*"*50) 
    
    print("\n" + "\n" + f"initalizing Nikto scan for {ip_address}" + "\n")
    os.system(f"nikto -h {ip_address} > Case_{ip_address}/niktoscanresults.txt")
    print(f"Detailed nikto scan result for {ip_address} is succesfully saved as niktoscanresults.txt file" + "\n" + "*"*50)
    
    print("\n" + "*"*50 + "\n" + f"initalizing WScan for {ip_address}" + "\n")
    os.system(f"wpscan --url http://{ip_address} --random-user-agent > Case_{ip_address}/wpscanresults.txt")
    print(f"Detailed WPscan result for {ip_address} is succesfully saved as wpscanresults.txt file" + "\n" + "*"*50)    

# running the functions

if __name__ == "__main__":
    case()
    main()

