import os, sys, re, glob, math, time, glob
sys.path.append('./modules')
import core
from core import ca

class FM():
	def __init__(self):
		self.data = []
		self.ccd = ()

		self.pack = []
		self.currentFile = ''

	def _update_glob(self):
		cwd = os.getcwd
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
		a = raw.splitLines()
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
		self.fileName = fileName
		return 0

	def FileManager(self):

		opt = {
				'(R)ead File': self._readFile, 
				'(C)reate new file': self._newFile,
				'Change the (P)ath': self._newPath,
				'Create a new (S)ubdirectiry': self._newDir,
				'(V)iew your current pack': self._viewPack,
				'(E)xit': self._exit()
		}
		while True:
			self._update_glob()
			cwd = self.ccd[0]
			csv = self.ccd[1]
			dire = self.ccd[2]
			core.cls()

				
			a = lambda:  print('{0}\n{1}\n{0}'.format(ca('','#'),ca('| File Manager |','#')))
			b = lambda li : '\n##\t'.join(li) 
			a()
			print('## Current Directory: {0}\n##\n## Sub directories:\n##\t{1}\n##\n## CSV Files:\n##\t{2}'.format(cwd, b(dire), b(csv)))
			print(ca('','#'))
			print(', '.join([i for i,j in opt.items()]))
			arg = input('\n>>> ')
			func = opt.get(arg, None)
			
			if not func:
				print('Invalid option')
				time.sleep(1)
				pass
			
			status = func()
			if status == 2:
				return 0
			
			
			
		return 0



if __name__ == '__main__':
	f = FM()
	f.FileManager()


