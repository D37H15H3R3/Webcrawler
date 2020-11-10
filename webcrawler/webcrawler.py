import requests
import re
import sys
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def request(url):
	try:
		return requests.get("https://"+url)
	except KeyboardInterrupt:
		print("You pressed CTRL-C! Abort! Abort!...")
		sys.exit()
	except requests.exceptions.ConnectionError:
		pass
		print(bcolors.FAIL + "No such domain", bcolors.ENDC)
url = input("Please input your url here [->] ")
with open("domains", 'r') as file:
	for line in file:
		word = line.strip()
		test_url = word + "."+ url 
		response = request(test_url)
		if response:
			print(bcolors.OKGREEN + "Subdomain surely does exists {} !".format(test_url), bcolors.ENDC)




