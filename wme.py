#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import getopt
import json
import os
import time
import sys
from datetime import datetime
nick = "P34C3_KHYREIN"
tools_name = "Woocommerce-Mail-Extractor"
now_version = "1.0"
# This Python file uses the following encoding: utf-8

# ============================================= #
# Created | Copyright (c) 2021 by P34C3_KHYREIN
# ============================================= #

# Create Executable Files (.exe) : pyinstaller --onefile wme.py
# pyinstaller --onefile --add-data "C:/Python3/Lib/site-packages/pyfiglet";./pyfiglet --icon=app.ico wme.py

########################################################################

# A notice to all nerds and n00bs...
# If you will copy the developer's work it will not make you a hacker..!
# Respect all developers, we doing this because it's fun...

########################################################################

####################################################################
#                        Check Python Version
if sys.version[0] in "2":
    terminal_clear()
    print("\n[x] ..n00b.. %s Is Not Supported For python 2.x Use Python 3.x \n" % (
        tools_name))
    print(
        "\n\n\t%s \033[1;91mI like to See Ya, Hacking \033[0m\n\n" % (tools_name))
    enter=input("[?] Enter to exit...")
    sys.exit()

####################################################################
#                       Import Python Library
try:
    import pyfiglet

    import requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
except ImportError:
    print("INSTALL REQUIREMENTS LIBRARY...")

    os.system('pip install requests')
    os.system('pip install pyfiglet')

    print("\nOpen again...")
    enter=input("[?] Enter to exit...")
    sys.exit()


def terminal_clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

####################################################################
#                               Color
color_list = {
    # reguler
    "reset": "\033[0m",
    "hitam": "\033[0;30m", "b_hitam": "\033[1;30m", "u_hitam": "\033[4;30m", "bg_hitam": "\033[40m", "hi_hitam": "\033[0;90m", "bhi_hitam": "\033[1;90m", "bghi_hitam": "\033[0;100m",
    "merah": "\033[0;31m", "b_merah": "\033[1;31m", "u_merah": "\033[4;31m", "bg_merah": "\033[41m", "hi_merah": "\033[0;91m", "bhi_merah": "\033[1;91m", "bghi_merah": "\033[0;101m",
    "hijau": "\033[0;32m", "b_hijau": "\033[1;32m", "u_hijau": "\033[4;32m", "bg_hijau": "\033[42m", "hi_hijau": "\033[0;92m", "bhi_hijau": "\033[1;92m", "bghi_hijau": "\033[0;102m",
    "kuning": "\033[0;33m", "b_kuning": "\033[1;33m", "u_kuning": "\033[4;33m", "bg_kuning": "\033[43m", "hi_kuning": "\033[0;93m", "bhi_kuning": "\033[1;93m", "bghi_kuning": "\033[0;103m",
    "biru": "\033[0;34m",  "b_biru": "\033[1;34m",  "u_biru": "\033[4;34m",  "bg_biru": "\033[44m",  "hi_biru": "\033[0;94m",  "bhi_biru": "\033[1;94m",  "bghi_biru": "\033[0;104m",
    "ungu": "\033[0;35m",  "b_ungu": "\033[1;35m",  "u_ungu": "\033[4;35m",  "bg_ungu": "\033[45m",  "hi_ungu": "\033[0;95m",  "bhi_ungu": "\033[1;95m",  "bghi_ungu": "\033[0;105m",
    "cyan": "\033[0;36m",  "b_cyan": "\033[1;36m",  "u_cyan": "\033[4;36m",  "bg_cyan": "\033[46m",  "hi_cyan": "\033[0;96m",  "bhi_cyan": "\033[1;96m",  "bghi_cyan": "\033[0;106m",
    "putih": "\033[0;37m", "b_putih": "\033[1;37m", "u_putih": "\033[4;37m", "bg_putih": "\033[47m", "hi_putih": "\033[0;97m", "bhi_putih": "\033[1;97m", "bghi_putih": "\033[0;107m",
}


def color(param):
    if param == True:
        terminal_clear()
        for x in color_list:
            print(color_list["putih"]+"kode warna: " +
                  color_list[x]+x+color_list["putih"])
        
        enter=input("[?] Enter to exit...")
        sys.exit()
    else:
        try:
            return color_list[param]
        except:
            print('color "'+param+'" tidak tersedia...')
            
            enter=input("[?] Enter to exit...")
            sys.exit()


####################################################################
#                               Symbol
symbol_list = {
    "check": "✔", "check_green_box": "✅",
    "cross": "✖", "cross_red": "❌", "cross_green_box": "❎",

    "muka_nangis": "😭", "muka_sedih": "😥", "muka_setan": "😈",
    "muka_kacamata": "😎", "muka_love": "😍", "muka_ketawa": "😂",
    "muka_senyum1": "😀", "muka_senyum2": "😁",
    "muka_jengkel": "😒", "muka_datar": "😕",

    "seratus": "💯", "rantai": "🔗",
    "palu": "🔨", "kunci_motor": "🔧", "palu_kunci": "🛠",
    "gear": "⚙", "pisau": "🔪",
    "kapak": "🪓", "tulang": "🦴",
    "hati": "🧡", "otak": "🧠", "patah_hati": "💔",
    "mercon": "🧨", "magnet": "🧲",
    "kompas": "🧭", "resep": "🧾",
    "disket": "💾", "jangkar": "⚓", "map": "🗺",
    "roket": "🚀", "sepeda": "🚴", "vespa": "🛵", "satelit": "🛰",
    "tidak_boleh": "🚫", "tidak_boleh_masuk": "⛔", "dilarang_masuk_proyek": "🚧",
    "lampu": "💡", "lampu_traffic": "🚥",
    "jam_beker": "⏰", "jam_tangan": "⌚", "stopwatch": "⏱",
    "timbangan": "⚖️", "kaca_pembesar": "🔍",
    "tepat_sasaran": "🎯", "dua_topeng": "🎭",
    "hp": "📱", "telepon": "📞",
    "antena": "📡", "pc": "💻",
    "karung_uang": "💰", "uang": "💵",
    "kunci_rumah": "🔑", "kunci_gembok": "🔐",
    "bell": "🔔", "speaker": "🔊",
    "gembok_lock": "🔒", "gembok_unlock": "🔓",
    "warning": "⚠",
    "bomb": "💣", "ganja": "🍁",
    "injection": "💉", "skull": "💀",
    "ghost_1": "👹", "ghost_2": "👺", "ghost_3": "👻",
    "kacamata": "👓",

    "tepuk_tangan": "👏", "oke": "👌", "dadah": "👋",
    "jempol_atas": "👍", "jempol_bawah": "👎",

    "text_up": "🆙", "text_new": "🆕", "text_ok": "🆗",
    "text_sos": "🆘", "text_free": "🆓",
    "square_back": "🔙", "square_soon": "🔜",
}


def symbol(param):
    if param == True:
        terminal_clear()
        for x in symbol_list:
            print(x+": "+symbol_list[x])
        
        enter=input("[?] Enter to exit...")
        sys.exit()
    else:
        try:
            return symbol_list[param]
        except:
            print('symbol "'+param+'" tidak tersedia...')
            
            enter=input("[?] Enter to exit...")
            sys.exit()
####################################################################
#                                Function


def execute(cmd):
    os.system(cmd)


def wget(link):
    print(color("kuning") + "DOWNLOAD FILE...\n" + color("merah") +
          'execute: ' + color("kuning") + 'wget ' + link + '\n' + color("hijau"))
    execute('wget '+link)


def rename(awal, akhir):
    execute('mv '+awal+' '+akhir)


def rm(link):
    execute('rm '+link)


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def logger(data, filename):
    if len(data) != 0:
        file = open(filename, "a")
        file.write(str(data))
        file.write("\n")
        file.close()
####################################################################
#                         get info from database


def get_version():
    terminal_clear()
    t0 = time.time()
    try:
        print("Get info from database...")
        response = requests_retry_session().get("https://raw.githubusercontent.com/p34c3-khyrein/version/main/%s.json" %
                                                (tools_name), timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
        return json.loads(response.text)
    except Exception as x:
        try:
            print('It failed :( ' + x.__class__.__name__ + ', status:' +
                  str(response.status_code) + '\ncontent:\n' + response.text)
        except AttributeError:
            print('It failed :( ' + x.__class__.__name__ +
                  ', status: No Internet Connection')
        except UnboundLocalError:
            print('It failed :( ' + x.__class__.__name__ +
                  ', status: No Internet Connection')
            
        enter=input("[?] Enter to exit...")
        sys.exit()
    else:
        print('It eventually worked ' + response.status_code)
        
        enter=input("[?] Enter to exit...")
        sys.exit()
    finally:
        t1 = time.time()
        print('Time Took: ' + str(round(t1 - t0, 2)) + ' seconds')
        time.sleep(2)


database = get_version()


def whats_new():
    print(symbol("timbangan") + color("b_ungu") + "  what's new? : \n")
    info_wn = database['whats_new']
    # info_wn.sort(key=lambda x: x.count, reverse=True)
    for p in info_wn:
        info_update = p['update']
        update = "\n"
        for a in info_update:
            update += "      " + \
                symbol(a["icon"]) + color("b_ungu") + " : " + \
                color("hijau") + a["info"] + "\n"
        ok_print = "   " + symbol("check_green_box") + color("b_biru") + " [" + color(
            "b_hijau") + p['version'] + color("b_biru") + "] " + color("cyan") + update
        print(ok_print)

########################################################################
#                               Banner
# Font Available
# slant , banner3-D , isometric1 , alligator , alligator2 , banner
# big , binary (:V) , block (bg, color) , chunky , colossal , computer
# contessa , contrast ,


# ok: slant , banner3-D , contessa , contrast , cosmic , drpepper
namatool = tools_name.split("-")
ascii_banner = ""
for anu in namatool:
    ascii_banner = ascii_banner + pyfiglet.figlet_format(anu, font="slant")
row_pembatas = 79
####################################################################
#                               Header


def pembatas():
    print(color("b_kuning")+"-" * row_pembatas + color("hijau"))


def banner():
    terminal_clear()
    print("")
    pembatas()
    print(color("bhi_merah") + ascii_banner)
    print(color("b_biru") + "Version: " + now_version + ( " " * (row_pembatas-28) ) + color("b_kuning") + "by " + color("b_hijau") + nick)
    pembatas()

####################################################################
#                             Define Variable
# check update sources
if float(database["version"]) > float(now_version):
    banner()
    print("please update new sources!")
    print("now version: " + color("b_hijau") + database["version"])
    whats_new()

    ready = input(color("b_cyan") +
                  "Ready to Update? (Y/y ~ N/n/*): " + color("b_hijau"))
    if ready == "Y" or ready == "y":
        print("")
        rm(sys.argv[0])
        wget("https://raw.githubusercontent.com/p34c3-khyrein/%s/main/%s.exe" %
             (tools_name, tools_name))
        print(symbol("check_green_box")+" Updated!")
        print(color("b_cyan") + "please open again!")
    else:
        print(color("b_merah") + "you should update this file!")
    pembatas()
    
    enter=input("[?] Enter to exit...")
    sys.exit()

####################################################################
#                                MAIN
banner()
try:
    input_file = input("\n[+] file dump [.sql] : ")

    list = open(input_file, 'r', encoding='utf-8').read().splitlines()

    input_pointer = 0
    while True:
        input_pointer = int(input("\n[+] pointer [angka] : "))
        for a in list:
            try:
                list_sql = a.split("'")
                print("\n[=] Select ~> %s" % (list_sql[input_pointer]))
                break
            except:
                continue
        input_ok = input("\n[?] Selected is email? [enter > input ulang pointer // ketik asal > next step] : ")
        if len(input_ok) != 0:
            break
        else:
            banner()
            

    input_namesave = input("\n[+] save [.txt] : ")

    list = open(input_file, 'r', encoding='utf-8').read().splitlines()
    for b in list:
        try:
            list_sql = b.split("'")
            logger(list_sql[input_pointer], input_namesave)
            print("Save ~> %s" % (list_sql[input_pointer]))
        except:
            continue

    print("\nSelesai...")
    enter=input("[?] Enter to exit...")
except KeyboardInterrupt:
    print("\n\nLho koq keluar?\n")