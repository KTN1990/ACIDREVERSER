# -*- coding: utf-8 -*
#!/usr/bin/env python3
# Hail Ea,Enki,Satanama, the morning star <3
# https://youtu.be/lc1r7TMnRh0
##[------------------------------[LIBS]--------------------------------]##
try:
    from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
except Exception as e:
    print('[-]: http-request-randomizer required!'+'\n'+'\t'+'[+]: pip install http-request-randomizer')
    exit(0)
from time import time,strftime,gmtime,sleep
from math import ceil
from argparse import ArgumentParser
from urllib.parse import urlparse
import socket, subprocess, platform, concurrent.futures, os, random
if platform.system() == 'Windows':
    cmd = 'cls'
else:
    cmd = 'clear'
##[------------------------------[LIBS]--------------------------------]##
##[-------------------------------[COLORS]--------------------------------]##
R,G,B,C,M,Y = "\033[0;31;40m","\033[0;32;40m","\033[0;34;40m","\033[0;36m",'\033[95m',"\033[0;33;40m"
BOLD,UNDER,END = '\033[1m','\033[4m','\033[0m'
log = strftime("[%H:%M:%S]", gmtime())
##[-------------------------------[COLORS]--------------------------------]##
##[-------------------------------[LOGO]--------------------------------]##
def logo():
    ktns = ['\033[0;36m', '\033[95m', '\033[0;31;40m', '\033[92m', '\033[94m']
    for _ in range(35):
        random.shuffle(ktns)
        color = ktns[1]
        b = END+BOLD +'''            
                               ___  _____   _________  ________  
                              / _ \/ __/ | / / __/ _ \/ __/ __/  
                             / , _/ _/ | |/ / _// , _/\ \/ _/    
                            /_/|_/___/ |___/___/_/|_/___/___/'''+color+BOLD +'''    
                                 H
                                 |
                           H  H  C--H.   
                            `.|,'|
                              C  H  H
                              |     |
                         O    N  H  C
                         // ,' `.|,'|`.
                           C     C  H  H
                           |     |
                        H--C     H ''' + Y +BOLD+ ''' [V]-: 1.0''' + color+BOLD + '''
                         ,' `.__   ''' + Y +BOLD+ ''' [?]-: LYSERGIC AC1D DIETHYLAMIDE''' + END+BOLD + '''
                        /  _/ _ \  ''' + Y +BOLD+ ''' [Author]-: KTN''' + END+BOLD + '''       
                       _/ // ___/                
                      /___/_/'''+color+BOLD +''' 
                  H  H--C  H--C--H
                  |     ||    |
            H     C     C     N  H  H
             `. ,' `. ,' `. ,' `.|,'
               C  _  C  H  C     C
               | (_) |   `.|     |
               C     C     C     H
             ,' `. ,' `. ,' `.
            H     C     C     H
                  |    ||
                  N-----C
                  |     |
                  H     H'''+END+BOLD +''' 
           __   __/___/_/_  __ ____  _____   
          / /  / __ \/ __ \/ //_/ / / / _ \  
         / /__/ /_/ / /_/ / ,< / /_/ / ___/  
        /____/\____/\____/_/|_|\____/_/   '''+'\n'+'\n'+'\x1b[6;30;42m' + 'LOADING...' + '\x1b[0m' 
        os.system(cmd)
        print(b)
        sleep(0.1)
##[-------------------------------[LOGO]--------------------------------]##
##[-----------------------------------------------------------------------------------------------[666]------------------------------------------------------------------------------------------------]##
class reverse:
    def __init__(self, url):
        if not urlparse(url).scheme:
            self.url = f'http://{url}'
            self.url = urlparse(self.url).netloc
        else:
            self.url = urlparse(url).netloc
    def lookup(self):
        try:
            IP   = socket.gethostbyname(self.url)
            SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            SOCK.settimeout(2)
            LIVE = SOCK.connect_ex((IP,80))
            if LIVE==0:
                CMD  = 'python satan0.py ' + IP
                GO   = subprocess.check_output(CMD, shell=True, stderr=subprocess.STDOUT)
                return 1, IP
            else:
                return 0
        except Exception as e:
            print(e)

def w666(site):
    global LEN_SITES, SCANNED
    rev = reverse(site)
    if rev.lookup():
        SCANNED += 1
        try:
            with open(rev.lookup()[1]+'.txt', 'r') as f: COUNT = f.read().splitlines()
            print(f'{BOLD}({str(LEN_SITES)}/{str(SCANNED)})*{G}{BOLD}[{rev.url:50}]~+=======> LIVE\n\t{Y}{BOLD}[+]- SITES FONDED ON THIS IP:{C}{BOLD}{str(len(COUNT))}{END}')
        except:
            print(f'{BOLD}({str(LEN_SITES)}/{str(SCANNED)})*{R}{BOLD}[{rev.url:50}]~+=======> DEAD{END}')

    else:
        SCANNED += 1
        print(f'{BOLD}({str(LEN_SITES)}/{str(SCANNED)})*{R}{BOLD}[{rev.url:50}]~+=======> DEAD{END}')
##[-----------------------------------------------------------------------------------------------[666]------------------------------------------------------------------------------------------------]##
# MAIN ################################################# 
if __name__ == '__main__':
    try:
        print(BOLD+"[PS]-:~~ Stealing the author work won't make you an author just another lame poser :) ~~"+END)
        start = time()
        ktn = ArgumentParser()
        ktn.add_argument('-s', '--target', help="<put your traget website: -l http://site.com>")
        ktn.add_argument('-l', '--list', help="<put your list of website exmple: -l list_site.txt>")
        ktn.add_argument('-t', '--thread', required=True, type=int, help="<threading exmple: -t 100>")
        satan = ktn.parse_args()
        SITE      = satan.target
        SITES     = satan.list
        THREADING = satan.thread
        if SITE:
            W = 0
            print(SITE)
            PP = SITE
            LEN_SITES = 1
        if SITES:
            W = 1
            try:
                with open(SITES, 'r') as f: SITES = f.read().splitlines()
                LEN_SITES = len(SITES)
                PP = str(LEN_SITES)
            except:
                print(f'{R} [-] ERROR:\n\t {Y} CAN`T OPEN SITES_LIST FILE!{END}')
                exit(0)
        logo()
        print ("\033[A                             \033[A")
        print('\n')
        print(f'{BOLD}{log}{G}{BOLD}[✓]~ {BOLD} LOADED: {M} ({PP})  TRAGET {BOLD}\n\t  {BOLD}{BOLD}[✓]~{R}  WORK WITH: {(str(THREADING))} THREADS{END}')
        SCANNED     = 0
        if W:
            with concurrent.futures.ThreadPoolExecutor(max_workers=THREADING) as killz:
                killz.map(w666, SITES)
        if not W:
            w666(SITE)
        print(f'{BOLD}{log}{G}[✓]~ {BOLD} TOTAL SCANNED WEBSITES: {Y} ({str(SCANNED)}) {END}')
        print(f'{BOLD}{log}{G}[✓]~ {BOLD} TIME TOKEN: ({str(ceil(time() - start))}) S {END}')
    except KeyboardInterrupt:
        print(f'{BOLD}{log}{G}[✓]~ {BOLD} Ctrl+c pressed... exiting{END}')
        print(f'{BOLD}{log}{G}[✓]~ {BOLD} TOTAL SCANNED WEBSITES: {Y} ({str(SCANNED)}) {END}')
        print(f'{BOLD}{log}{G}[✓]~ {BOLD} TIME TOKEN: ({str(ceil(time() - start))}) S {END}')
        exit(0)
