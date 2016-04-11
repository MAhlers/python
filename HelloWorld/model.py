#/usr/bin/python

class Model:
	'Class to Interact with the "Model" (Text for Simplicity).'

def open_connection(conn_string):
	
	try:
	
		return open(conn_string)
	
	except Exception:
	
		print(Exception)
		
def close_connection(conn):
	
	try:
	
		conn.close()
		
	except Exception:
	
		print(Exception)
		
def get_records(conn):
	
	try:
	
		return conn.readlines()
		
	except Exception:
	
		print(Exception)