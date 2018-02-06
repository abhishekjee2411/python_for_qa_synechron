#ping a list of machines

import os
ips=["localhost","google.com","cognizant.com","infosys.com","rediff.com","yahoo.com","barclays.com","trumpputinmodi.com","www.redbus.in"]

while True:
	for ip in ips:
		result = os.system("ping {} > NUL".format(ip))
		if result == 0:
			status = "Up"
		else:
			status = "Down"
		print("{} is {}".format(ip,status))
