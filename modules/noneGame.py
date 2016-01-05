# Some stuff
import os, sys,  math, re
sys.path.append('./modules')
from core import *
from glob import glob
from time import sleep

# Move up from the modules dir, mabey?
# os.chdir('..')

# Classes
class _fileManager():
	def __init__(self):
		self.fileName = ''
		self.data = None

	def updateDirContents(self, paths = True):
		if paths:
			return glob('*/')
		else:
			return glob('*.csv')

	def changePath(self, newPath):
		try:
			os.chdir(newPath)
		except IOError as e:
			print('Directory not found or Premission is Denied')
			print('{0}: {1}'.format(e.errno, e.strerror))
			return False
		else:
			return True

	def loadFile(fileName, self):
		with open(fileName, 'r') as contents:
			data = contents.read()
		return data

	def cleanData(self,data):
		ucList = data.splitlines()
		finalList = [i.split(',') for i in ucList]
		return finalList
	

	def fileBrowser(self, dataToGo = None):
		while True:
			cls()
			allCSV = self.updateDirContents(False)
			allSubDir = [i[:-1] for i in glob('*/')]
		
			if len(allCSV) == 0:
				allCSV.append('None')
			if len(allSubDir) == 0:
				allSubDir.append('None')

			print('{0}\n{1}\n{0}'.format(centerAlign('', '#'),centerAlign('| FileBrowser {0} |'.format('4.0.3'), '#')))
			print('## The current sub directories are:')
			print('##\t'+'\n##\t'.join(allSubDir))
			print('##\n## The current CSV Files are:')
			print('##\t'+'\n##\t'.join(allCSV))
			print('{0}\n{0}'.format(centerAlign('', '#')))

			
			options = ["(O)pen a file","(C)reate a new subdirectory","(M)ake a new file","Change the (P)ath","(R)efresh the file list","(E)xit"]

			print('## Do you want to:\n##\t{0}'.format('\n##\t'.join(options)))
			newPath = input('>>> ').lower()
			if newPath == 'o':
				print('## What File?')
				fileName =  input('>>> ')
				if fileName in allCSV:
					with open(fileName, 'r') as File:
						data = File.read()
					print("Success!")
					sleep(2)
					return data
				else:
					print('That file does not exist')
					sleep(2)
					continue
			
			elif newPath == 'c':
				print('## What name?')
				dirName = input('>>> ')
				if dirName not in allSubDir:
					try:
						os.mkdir(dirName)
					except OSError:
						opt = ["Change the name of the folder","Change the directory you are using", "Change the permissions of the folder"]
						print("There was an error. You can try:\n{0}".format('\n\t'.join(opt)))	
						sleep(3)
						continue
					else:
						print("Sucess")
						sleep(1)
						continue

			elif newPath == 'm':				
				print("## What file name?")
				fileName = input('>>> ')
				if fileName in allCSV or fileName+'.csv' in allCSV:
					print("That file already exists, would you like to overwrite it? (y/n)")
					ask = input('>>> ')
					if ask == 'y':
						pass
					else:
						print("No changes have been made, restarting...")
						sleep(1)
						continue
				if fileName[-4:].lower() != '.csv':
					fileName += '.csv'					
				
				dataByteCount = sys.getsizeof(dataToGo)
				if not dataToGo:
					print('No data to write, writing empty file')
					dataToGo = ''
				else: 
					dataToGo = str(dataToGo)
					
				print("## Do you want to write {0} bytes to '{1}'? (y/n)".format(dataByteCount, fileName))
				write = input('>>> ').lower()
				if write == 'y':
					try:
						with open(fileName,'w') as File:
							File.write(str(dataToGo))
					except IOError as e:
						print('Something went wrong, check the permissions.\nError {0}: {1} with file {2}.'.format(e.errno, e.strerror, e.filename )) 
					else:
						cls()
						print('Sucess')
						sleep(2)
						return True


			elif newPath == 'p':
				print('## What directory?')
				path = input('>>> ')
				if path in allSubDir:
					status = self.changePath(path)
					if status:
						cls()
						print(centerAlign('| Completed |','=' ))
						sleep(1)
						continue
					else:
						cls()
						print('There was an error in changing the path')
						sleep(1)
						continue
				elif path == '..':
					os.chdir('..')
					print(centerAlign('| Completed |','=' ))
					sleep(1)
					continue
				else:
					print('The path name specified was invalid')
					sleep(1)
					continue
			
			elif newPath == 'r':
				continue

			elif newPath == 'e':
				break
		return None		
			
	

class _cardViewer():
	def __init__(self, cardPack):
		cardPackCopy = [i for i in cardPack]
		self.headers = cardPackCopy.pop(0)
		self.data = cardPackCopy
	
	def getHeaders(self):
		return self.headers
	
	def sortCards(self, field, reverse = False):
		#get index of field given
		fieldNameIndex = 0
		for i in range(len(self.headers)):
			if self.headers[i] == field:
				fieldNameIndex = i
				break
		else:
			return None
			
		self.data = sorted(self.data, key = lambda data:data[fieldNameIndex], reverse=reverse)
		return self.data
		
	
	def viewCards(self):
		cls()
		for i in range(len(self.data)):
			
			print('{0}\n{1}\n{0}'.format(centerAlign('','#'), centerAlign('| Card {0} of {1} |'.format(i+1, len(self.data)), '#')))
			for j in range(len(self.data[i])):
				sleep(0.0625)
				print('## {0}: {1}'.format(self.headers[j], self.data[i][j]))
				sleep(0.0625)
			print(centerAlign('','#'))
			input('>>> ')
			cls()
		
		
		

class _packCreator():
	def __init__(self):
		self.packName = None
		self.fields = None
		self.data = None
		self.allData = None
		self.allDataString = None
	
	def getData(self):		
		cls()
		print("What fields do you want (enter nothing to stop)")
		self.fields = []
		while True:
			toApp = input('>>> ')
			if toApp == '':
				break
			else:
				self.fields.append(toApp)
		
		cls()
		
		currentRecord = 1
		print("Record Time!...")
		sleep(1)
		cls()
		self.data = []
		lev1 = []
		
# 		if len(self.fields) < 1:
# 			print('There are no fields, returning to menu.')
# 			sleep(1)
# 			return False

		
		while True:
			exit = False
			for field in self.fields:
				print(centerAlign('| Data for field \'{0}\' record {1} |'.format(field,currentRecord), '#'))
				toGo = input('>>> ')
				cls()
				if toGo == '':
					exit = True
				else:
					lev1.append(toGo)
			
			if exit:
				break
			else:
				self.data.append(lev1)
			lev1 = []
			currentRecord += 1
			
	def printData(self):
		print(self.data)
		print(self.fields)	
				
	def condenseData(self):
		self.allData = []
		data = self.data
		tempList = []
		for i in data:
			temp = ','.join(i)
			tempList.append(temp)
			
		final = '\n'.join(tempList)
		headers = ','.join(self.fields)		
		headers += '\n'
		headers += final
		
		return headers
		
			



# Functions for menu
def openPack():
	print('## Please select a file to load')
	sleep(1)
	fm = _fileManager()
	data = str(fm.fileBrowser())
	data = fm.cleanData(data)
	return data
def createPack():
	pc = _packCreator()
	pc.getData()

	data = pc.condenseData()
	cls()
	print('## please choose a file to write to')
	sleep(1.5)
	fm = _fileManager()
	finished = fm.fileBrowser(data)
	if finished:
		return True
	
	elif not finished:
		return False
		
	else:
		return "Muchos crapas"
def viewPack(pack):
	cv = _cardViewer(pack)
	print("## Do you want to sort the cards first? (y/n)")
	a = input('>>> ').lower()
	
	if a == 'y':
		headers = cv.getHeaders()
		cls()
		print('{0}\n## Please choose a field by name (case sensitive)\n{0}\n##\t{1}'.format(centerAlign('','#'),'\n##\t'.join(headers)))
		field = input('>>> ')
		while True:
			if field not in headers:
				print("Invalid field, please try again")
				sleep(2)
				cls()
			else:
				break
			print('\n- '.join(headers))
			field = input('>>> ')
		print('## Do you want to reverse the sort order (Z -> A / 100 -> 1) (y/n)')
		reverse = input('>>> ')
		if reverse == 'y':
			reverse = True
		else:
			reverse = False
		cv.sortCards(field, reverse)
		
		
		###### LIMITATION #######################
		##									 ####
		## The sorter breaks when there are  ####
		## two or more identical card		 ####
		## in the pack.						 ####
		## 									 ####
		###### SORRY ############################
	cv.viewCards()
		

				
			


# Main Menu (I know, the name is a bit of a give away')
def mainMenu():
	options = ["(O)pen a new pack","(V)iew your current pack","(C)reate a new pack","(P)lay the game","(E)xit"]
	pack = []
		
	while True:
		
		if not pack:
			options[1] = "(V)iew your current pack - no pack is loaded"
		else:
			options[1] = "(V)iew your current pack"
		
		cls()
		
		print('{0}\n{1}\n{0}\n{2}'.format(centerAlign('','#'),centerAlign("| Welcome |",'#'),'##\t{0}'.format('\n##\t'.join(options))))
		a = input('>>> ').lower()
		
		if a == 'o':
			pack = openPack()
		
		elif a == 'v' and pack:
			viewPack(pack)
					
		elif a == 'v' and not pack:
			print('I told you once Rodney i\'m not going to tell you again son; I do the one..two..three..four\'s\nSrsly though, you need to load a pack')
			sleep(2)
			continue
			
		elif a == 'c':
			createPack()
			continue
		
		elif a == 'p' and pack:
			return pack
			
		elif a == 'p' and not pack:
			print('You must load a pack first.')
			continue
		
		elif a == 'e':
			raise SystemExit
		
			
		else:
			continue
				
		
			
def dev():
	with open('hobbit.csv','r') as f:
		data = f.read()
	fm = _fileManager()
	data = fm.cleanData(data)
	pack = data
	return data


x = sys.argv			
if len(x) > 1:
	if x[1] == 'FMTest':
		test_fileManager()
	elif x[1] == 'CV':
		_cardViewerTest()
	elif x[1] == 'help':
		helpList = ['FMTest']
		print('\n'.join(helpList))
		raise SystemExit
	elif a[1] == 'dev':
		pack = dev()
		
