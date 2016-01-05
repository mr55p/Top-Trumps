import sys, os, time, re, platform, math

def cls():
	if platform.system == 'windows': # This does not work, i think
					 # To future me - stop being lazy and
					 # look up the output of platform.sys
		os.system('CLS')
	else:
		os.system('clear')

def _get_terminal_size():
	if platform.system() == "Windows":
		#######################
		## Copied from i-net ##
		#######################
		from ctypes import windll, create_string_buffer
		h = windll.kernel32.GetStdHandle(-12)
		csbi = create_string_buffer(22)
		res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
		
		if res:
		    import struct
		    (bufx, bufy, curx, cury, wattr,
		     left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
		    sizex = right - left + 1
		    sizey = bottom - top + 1
		else:
		    sizex, sizey = 80, 25 
		
		return sizex
	else:
		import shutil
		str = shutil.get_terminal_size()
		intList = re.findall(r'\d+', "{0}".format(str))	
		return int(intList[0])

def ca(s,fillChar=" ",screenWidth=0):
	if screenWidth == 0:
		screenWidth = _get_terminal_size()
		
	if len(s) > screenWidth:
		return "bad"
	
	halfScreen = math.floor(screenWidth / 2)
	x = [fillChar for i in range(screenWidth)] #looking back, im not entirely sure why this works... oh well if it aint broke dont fix it ;)
	for char in s:
		x.pop()
	
	
	halfX = math.floor(len(x)/2)
	frontX = x[:halfX]
	rearX = x[halfX:]
	frontX.extend(s)
	frontX.extend(rearX)
	return "".join(frontX)


def osCheck():
	os = os.name
	if os == 'nt':
		return 1
	elif os == 'poisx':
		return 0
	else:
		return 1



# OLD
