#! /usr/bin/env python

import os
import sys
import shutil
import argparse
from config import bootstrap_app
from config import folders
from config import files

app_name='sample'

def create_folders(folders):
	try:
	
		print '---------------------------------'
		print 'Creating necessary folders'
		print '---------------------------------'
		
		for folder in folders:
			try:
				path=os.path.join(os.getcwd(),app_name+'/'+folder)

				print 'Creating folder '+app_name+'/'+folder
				
				os.makedirs(path)
			except OSError,e:
				print 'Error creating folder '+app_name+'/'+folder
				
				raise Exception
		
	except Exception,e:
		print e
		sys.exit(1)
		
def create_files(files):
	try:
	
		print ''
		print '---------------------------------'
		print 'Creating necessary files'
		print '---------------------------------'

		for filename in files:
			try:
				source_file=os.path.join(os.path.dirname(__file__),bootstrap_app+'/'+filename)
				dest_file=os.path.join(os.getcwd(),app_name+'/'+filename)
			
				print 'Creating file {0} in folder {1} '.format(os.path.split(dest_file)[1],os.path.split(dest_file)[0])
			
				shutil.copy(source_file,dest_file)
			except Exception,e:
				print 'Error creating file {0} in folder {1} '.format(os.path.split(dest_file)[1],os.path.split(dest_file)[0])
			
				raise Exception
	except Exception,e:
		print e
		sys.exit(1)
		
def handle_cmd_args(parser):
	global app_name
	
	parser.add_argument('app_name',help='Name of the app to create')
	
	args=parser.parse_args()
	
	if args.app_name:
		app_name=args.app_name

if __name__=='__main__':

	parser=argparse.ArgumentParser()
	
	handle_cmd_args(parser)

	create_folders(folders)
	create_files(files)

	print ''
	print 'Successfully created application\n'
	print 'To run the application:'
	print '\tpython manage.py runserver\n'
	print 'To launch the shell:'	
	print '\t python manage.py shell'
