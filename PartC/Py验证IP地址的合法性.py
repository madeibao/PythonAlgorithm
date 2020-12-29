# -*- coding: utf-8 -*-



while True:
	try:
	    def isLegal(ip):
	        	
	        ipTest = list(map(int,ip.split('.')))
	        if len(ipTest)!=4:
	        	return False
	        	
	        for i in range(4):
	            if ipTest[i] < 0 or ipTest[i] >255:
	            	return False
	        return True	

	    ip1 = input()
	    print(isLegal(ip1))
	except:
		break

#================================
#----------------------------------------------------------------

# 脚本语言来判断最终的效果。


def isLegal(ip):
	        	
	ipTest = list(map(int,ip.split('.')))
	if len(ipTest)!=4:
		return False

	        	
	for i in range(4):
		if ipTest[i] < 0 or ipTest[i] >255:
			return False
	return True	


while True:
	try:
	    ip1 = input()
	    print(isLegal(ip1))
	except:
		break