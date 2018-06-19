
# TLD Scanner
TLD Scanner scans for all existing top level domains for a give domain name.

| Switch | Description |
| --- | --- |
| -d \<domain\>  | Specifiy the domain name, example: "google" |
| -o \<outputfile\> | Write results into \<outputfile\> as json |
| -i \<tldfile\> | Use your own custom TLD list - One TLD per line, no other seperators, case insensitive |
| -f | Use the newest and complete list of TLDs from IANA. This will take quite some time |
| -n | Does a name lookup and prints the ip (fastest) |
| -c | Tries to connect to the host directly |
| -b | Default: Does a namelookup and then tries to connect and prints the ip |
| -s | Check for https too |


## Example 
This will do a name lookup (fastest method) for google using the top TLD list (24 domains in 0.0649 seconds)
```
$ ./tld_scanner.py -n -d google -i topTLDs.txt 
  _______ _      _____     _____  _____          _   _ _   _ ______ _____  
 |__   __| |    |  __ \   / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
    | |  | |    | |  | | | (___ | |       /  \  |  \| |  \| | |__  | |__) |
    | |  | |    | |  | |  \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / 
    | |  | |____| |__| |  ____) | |____ / ____ \| |\  | |\  | |____| | \ \ 
    |_|  |______|_____/  |_____/ \_____/_/    \_|_| \_|_| \_|______|_|  \_\
                                                                   by ozzi-
Using custom TLD List: ['COM', 'CO', 'ORG', 'EDU', 'GOV', 'UK', 'BIZ', 'ME', 'INFO', 'NET', 'CA', 'DE', 'JP', 'FR', 'AU', 'US', 'RU', 'CH', 'IT', 'NL', 'SE', 'NO', 'ES', 'MIL']

Mode: Name lookup only
Using the following protocol(s): ['http://']
google

Using domain: google

100%|████████████████████████████████████████████████████████████████████| 24/24 [00:00<00:00, 376.42domains/s]

{'http://google.co': '172.217.168.46', 'http://google.ch': '172.217.168.3', 'http://google.com': '172.217.168.46', 'http://google.ru': '172.217.168.3', 'http://google.nl': '172.217.168.35', 'http://google.de': '172.217.168.35', 'http://google.ca': '216.58.205.163', 'http://google.net': '172.217.168.4', 'http://google.fr': '172.217.168.35', 'http://google.info': '172.217.168.4', 'http://google.no': '172.217.168.3', 'http://google.es': '172.217.168.35', 'http://google.jp': '172.217.168.35', 'http://google.org': '216.239.32.27', 'http://google.se': '172.217.168.35', 'http://google.me': '172.217.168.4', 'http://google.it': '172.217.168.35', 'http://google.us': '172.217.168.4'}

--- 0.064945936203 seconds ---
```

This will check all ~1500 TLDs for the domain name gnu using http and https
```
./tld_scanner.py -f -d gnu -s
```
