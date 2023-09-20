# subdomain_enum
This Python script enumerates subdomains of a given domain. The script uses a list of subdomains from the file subdomains.txt and tries to connect to each subdomain using the HTTP protocol. If the connection is successful, the script writes the subdomain to a text file called succes.domain.txt.

To use the script, simply save it as a Python file (e.g. subdomain_enum.py) and run it with the domain you want to enumerate subdomains for as a command-line argument. For example, to enumerate subdomains for the domain example.com, you would run the following command:

python subdomain_enum.py example.com

The script will then print a list of all valid subdomains that it found to the console and write the successful connections to the file succesdomains.txt.

Usage:

python subdomain_enum.py <domain>


**Example:**

python subdomain_enum.py example.com


**Output:**

Attempting to connect to http://www.example.com... success!
Attempting to connect to http://mail.example.com... failed.
Attempting to connect to http://blog.example.com... success!

Valid domains:
http://www.example.com
http://blog.example.com

Dependencies:

Python 3
Requests library
Notes:

The script uses a list of subdomains from the file subdomains.txt. This list can be modified to include any subdomains that you want to enumerate.
The script writes the successful connections to a text file called succes.domain.txt. This file will be created in the same directory as the Python script.
The script can be used to enumerate subdomains for any domain, including publicly accessible domains and domains on a private network.
