import time
from urllib import request
import sys, getopt, socket

domain = ''
https  = False
outputfile = ''
tldfile = ''
mode=''

def scan(tlds,domain,protocols):
    if outputfile is not '':
        f = open(outputfile,'w')
    exists = []
    for tld in tlds:
        for protocol in protocols:
            try:
                ip = ""
                if mode == 'b' or mode =='n':
                    ip = socket.gethostbyname(domain+tld)
                if ip != "127.0.53.53":
                    target=(protocol+domain+tld.lower())
                    if mode != 'n':
                        response = request.urlopen(target)
                    exists.append(target)
                    if outputfile is not '':
                        f.write(target+" "+ip+'\n')
                    print (target+" "+ip)
            except Exception as e:
                c=1 #eat up
    if outputfile is not '':
        f.close()
    return exists

def print_header():
    print ('')
    print ('  _______ _      _____     _____  _____          _   _ _   _ ______ _____  ')
    print (' |__   __| |    |  __ \   / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ ')
    print ('    | |  | |    | |  | | | (___ | |       /  \  |  \| |  \| | |__  | |__) |')
    print ('    | |  | |    | |  | |  \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / ')
    print ('    | |  | |____| |__| |  ____) | |____ / ____ \| |\  | |\  | |____| | \ \ ')
    print ('    |_|  |______|_____/  |_____/ \_____/_/    \_|_| \_|_| \_|______|_|  \_\\') 
    print ('')

def main(argv):
    global domain,https,outputfile,tldfile,mode
    c=False
    n=False
    b=False
    try:
        opts, args = getopt.getopt(argv,"bncsd:o:i:")
    except getopt.GetoptError:
        print ('tld_scanner.py  [-d <domain>] [-o <outputfile>] [-i <tldfile>] [-n] [-c] [-b] [-s]')
        print ('')
        print ('This tool scans for all possible TLDs of a given domain name')
        print ('')
        print ('-d <domain>     | Specifiy the domain name, example: "google"')
        print ('-o <outputfile> | Write results into <outputfile>')
        print ('-i <tldfile>    | Use your own custom TLD list')
        print ('                  One TLD per line, no other seperators, case insensitive')
        print ('-n              | Does a namelookup and prints the ip (fastest)')
        print ('-c              | Tries to connect to the host directly')
        print ('-b              | Default: Does a namelookup and then tries to connect')
        print ('                  prints the ip')
        print ('-s              | Check for https:// too')

        sys.exit(2)
    for opt, arg in opts:
        if opt == '-s':
            https = True
        elif opt in ("-o"):
            outputfile = arg
        elif opt in ("-d"):
            domain = arg
        elif opt in ("-i"):
            tldfile = arg     
        elif opt in ("-b"):
            b=True
        elif opt in ("-c"):
            c=True
        elif opt in ("-n"):
            n=True
    mode = 'b' # DEFAULT
    if b or (n and c):
	    mode = 'b'
    elif n:
	    mode = 'n'
    elif c:
        mode = 'c'

if __name__ == '__main__':
    main(sys.argv[1:])
    print_header()
    try:
        print("Getting the newest TLD's from iana.org . . .")
        request.urlretrieve ("https://data.iana.org/TLD/tlds-alpha-by-domain.txt", "tld_scanner_list.txt")
    except Exception as e:
        print(e)
        print("Please check your network connectivity (or https://data.iana.org is down)!")
        sys.exit(2)
    try:
        if tldfile is not '':
            try:
                tlds = [line.rstrip('\n') for line in open(tldfile)]
            except Exception as e:
                print ("Inputfile doesn't exist / not readable")
                sys.exit(2)
            print("Using custom TLD List: "+str(tlds))
        else:
            tlds = [line.rstrip('\n') for line in open("tld_scanner_list.txt")]
            print(tlds.pop(0))
        print("")
        if mode =='c': print("Mode: Connecting to host")
        if mode =='b': print("Mode: Name lookup + connecting to host")
        if mode =='n': print("Mode: Name lookup only")
        print('')
        protocols = ["http://","https://"] if https else ["http://"]
        print("Using the following protocol(s): "+str(protocols))
        if domain is '':
            print("")
            domain = input("Enter Domain name (example 'google'): ")
        else:
            print('\nUsing domain: '+domain)
        domain = domain+"."
        print("")
        start_time = time.time()
        exists= scan(tlds,domain,protocols)
        print("\n--- %s seconds ---" % (time.time() - start_time))
    except:
        print ('CTRL-C or exception')
