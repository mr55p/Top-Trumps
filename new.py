import os, sys, re, glob, math, time, glob
sys.path.append('./modules')
import core
from core import ca

class FM():
	def __init__(self):
		self.data = []
		self.ccd = ()

		self.pack = []
		self.currentFile = 'None'

	def _update_glob(self):
		cwd = os.getcwd()
		csv = []
		dire = []
		
		# MORE STUFF
		csv = glob.glob('*.csv')
		dire = [i[:-1] for i in glob.glob('*/')]
		
		# Proud of this one ;)
		csv += ['None'] if csv is None else []
		dire += ['None'] if csv is None else []
		
		self.ccd = (cwd,csv,dire)
	
	def _clean(self, raw):
		a = raw.splitlines()
		b = [i.split(',') for i in a]
		return b

	def _readFile(self):
		print('Please enter the name of the file including the extention (case sensetive):')
		fileName = input('>>> ')

		if fileName not in self.ccd[1]:
			core.cls()
			print('Invalid File Name')
			time.sleep(1)
			return None

		with open(fileName, 'r') as f:
			raw = f.read()

		self.currentPack = self._clean(raw)
		self.currentFile = fileName
		print('Success')
		time.sleep(2)
		return 0

	def _newFile(self):
		return 0

	def _newPath(self):
		print('Please enter the subdirectory name')
		path = input('>>> ')
		if path not in self.ccd[2]:
			print('invalid')
			time.sleep(2)
			return 1
		try:
			os.chdir(path)
		except IOError:
			print('Invalid Path/Directory')
			time.sleep(1)
			return 1
		finally:
			return 0
			
	def _newDir(self):
		print('What dir name?')
		name = input('>>> ')
		try:
			os.mkdir(name)
		except IOError:
			print('Unsuccesfull. Please try a different name or check the permissions of the directory.')
			time.sleep(2)
			return 1
		else:
			return 0

	def _viewPack(self):
		pass

	def _exit(self):
		return 2

	def FileManager(self):
		
		opt = {
				0: self._readFile, 
				1: self._newFile,
				2: self._newPath,
				3: self._newDir,
				4: self._viewPack,
				5: self._exit
		}

		optText = ['Read File', 'Create new file','Change the Path', 'Create a new Subdirectiry', 'View your current pack', 'Exit']
		
		while True:
			self._update_glob()
			cwd = self.ccd[0]
			csv = self.ccd[1]
			dire = self.ccd[2]
			core.cls()

				
			a = lambda:  print('{0}\n{1}\n{0}'.format(ca('','#'),ca('| File Manager |','#')))
			b = lambda li : '\n##\t'.join(li) 
			a()
			print('## Current Directory: {0}\n##\n## Current Pack: {3}\n##\n## Sub directories:\n##\t{1}\n##\n## CSV Files:\n##\t{2}'.format(cwd, b(dire), b(csv),self.currentFile))
			print(ca('','#'))
			
			for i in range(len(optText)):
				print('{0}) {1}'.format(i, optText[i]))
			
			arg = input('\n>>> ')
			try:
				arg = int(arg)
			except ValueError:
				print('Bad Opetion')
				return 1
			func = opt.get(arg, None)
			#print('Invalid option')
			#time.sleep(1)
			####s
			status = None
			try:
				status = func()
			except TypeError:
				print('invalid')
				time.sleep(1)
				pass
			
			if status == 2:
				return 0
			
			
			
		return 0



if __name__ == '__main__':
	f = FM()
	f.FileManager()


