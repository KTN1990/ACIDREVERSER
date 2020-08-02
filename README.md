# ACIDREVERSER 
Reverse IP Lookup using hackertarget.com API.

# What is a Reverse IP Lookup?
The technique known as Reverse IP Lookup is a way to identify hostnames that have DNS (A) records associated with an IP address.

A web server can be configured to server multiple virtual hosts from a single IP address. This is a common technique in shared hosting environments. It is also common in many organizations and can be an excellent way to expand the attack surface when going after a web server. If for example your primary target web site appears to be secure you may be able to gain access to the underlying operating system by attacking a less secure site on the same server. Bypassing the security controls of the target site.

## Features

1. Multithreading.
2. Single and multiple target scanning.
3. Can check with ip or website and auto-check for port 80 for mass ip scanning.
4. Bypassing free hackertarget.com API limitation using proxies (auto grabbed proxies).

## Installation
For Windows:
	
  1. Download [python3](https://www.python.org/downloads/windows/) 
  2. During the installation add python to your path, [how to ?](https://youtu.be/1jyOHCTgWpg) 
  3. Type this command in your CMD.exe
```
  python -m pip install http-request-randomizer
```
For Linux/Unix:
	
  1. Update your python3 using your package manager, exemple: apt for ubuntu or brew for mac os
  3. Type this command in your terminal
  ```
  python3 -m pip install http-request-randomizer
  ```
  
## Usage
[DEMO](https://youtu.be/lc1r7TMnRh0) 
```
python3 ACIDREVERSER.py [-h] [-s TARGET] [-l LIST] -t THREAD

 1. -s : single target (IP or WEBSITE)
 2. -l : list or targets (IP or WEBSITE)
 3. -t : number of threads
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
