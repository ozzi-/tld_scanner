     _______ _      _____     _____  _____          _   _ _   _ ______ _____  
    |__   __| |    |  __ \   / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
       | |  | |    | |  | | | (___ | |       /  \  |  \| |  \| | |__  | |__) |
       | |  | |    | |  | |  \___ \| |      / /\ \ | . ` | . ` |  __| |  _  /
       | |  | |____| |__| |  ____) | |____ / ____ \| |\  | |\  | |____| | \ \
       |_|  |______|_____/  |_____/ \_____/_/    \_|_| \_|_| \_|______|_|  \_\
       
       
       
This tool scanns for all possible (ICANN) TLDs of a given domain name.


| Switch | Description |
| --- | --- |
| -d \<domain\>  | Specifiy the domain name, example: "google" |
| -o \<outputfile\> | Write results into \<outputfile\> |
| -i \<tldfile\> | Use your own custom TLD list - One TLD per line, no other seperators, case insensitive |
| -n | Does a namelookup and prints the ip (fastest) |
| -c | Tries to connect to the host directly |
| -b | Default: Does a namelookup and then tries to connect and prints the ip |
| -s | Check for https:// too |
