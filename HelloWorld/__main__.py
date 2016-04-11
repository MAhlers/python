#/usr/bin/python

import os
import model
import sys
import utilities

class HelloWorld:
	'The HelloWorld Application'

	project_root = os.path.dirname(os.path.abspath(__file__))
	
	db = (project_root + '\data\db.txt')
	#empty_db = (project_root + '\data\emptydb.txt')
	
	data_size = os.stat(db).st_size

	if data_size > 0:
			
			try:
				
				conn = model.open_connection(db)
				
				data_list = model.get_records(conn)
				
				row_count = len(data_list)
				
				if row_count > 0:
					
					utilities.print_comma_exclam(data_list)
					
				else:
				
					print('Data_File Contains ', row_count, ' Records.')
				
				model.close_connection(conn)
				
				sys.stdin.readline()
				
			except OSError as e:

				print('Main() Exception: ', e)
			
	else:
		
		print("Data_File Data Length is ZERO.")
		