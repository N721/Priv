#!/usr/bin/python
# -*- coding: utf-8 -*
#©JametKNTLS
#Youtube : Logic Internet
#####################################
import requests, re, urllib2, os, sys, codecs, random           
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time
import json     
from zlib import compress, decompress
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)

abang = Fore.RED
ijo = Fore.GREEN
putih = Fore.WHITE
biru = Fore.BLUE
kuning = Fore.YELLOW
mbohopo = Fore.MAGENTA


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
              Priv8 Reverse Ip MultiThread  - Jamet31337
                  Ajibarang - 18 January 2K21                   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



cls()
print_logo()
start_raw = raw_input("\n\033[91mIP List \033[97m:~# \033[97m")
apikey = raw_input("\n\033[91mApikey \033[97m:~# \033[97m")
crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
try:
    with open(start_raw, 'r') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
    
try:
    ooo = list(dict.fromkeys((ooo)))
except NameError:
    print '\033[31mOpen Your Eyes!'
    sys.exit()
    
count=0
with open(start_raw,'r')as f:
 for line in f:
    count+=1
print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92mTOTAL IP=',count
def asu(url):
	try:
		res = requests.get("https://www.reverse-ip.uk/reverse/"+apikey+"/"+url, timeout=10,headers={'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}).json()
		for ceks in res["data"]:
			print(ceks+ijo+' > Result From ' +url)
			open('live.txt', 'a').write('http://'+ceks+'\n')
		else:
			print(abang+'You have stopped !!!')
	except:
		pass

def Main():
    try:
        start = timer()
        pp = Pool(int(crownes))
        pr = pp.map(asu, ooo)
        print(abang+'Contact me Shin_Code')
    except:
        pass
        
if __name__ == '__main__':
    Main()
   