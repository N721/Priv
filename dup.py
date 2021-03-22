import sys

get = open(raw_input("Your list : "), "r").read().splitlines()

liste = []
try:
	for sites in get:
		dhon = sites
		sites = sites.replace("https://", "")
		sites = sites.replace("http://", "")
		sites = sites.replace("www.", "")
		sites = sites.split("/")
		sites = sites[0]
		if sites not in liste:
			liste.append(sites)
			open("ip1.txt", "a").write(dhon + "\n")
except:
	pass