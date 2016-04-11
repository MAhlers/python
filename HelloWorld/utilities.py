#/usr/bin/python

class Utilities:
	'Utilities Class that Performs Various Duties (ie Print)'
		
def print_comma_exclam(data_list):
	
	try:
		
		out = []
		
		for index in range(len(data_list)):
			
			if index == 0:
			
				out.append(data_list[index].replace('\n','') + ',')
			
			elif index == (len(data_list) - 1):
				
				out.append(' ' + data_list[index].replace('\n','') + '!')
				
			else:
				
				out.append(' ' + data_list[index].replace('\n',''))
		
		print(''.join(out))
		
	except Exception as e:
	
		print('Print_Comma_Exclam Exception: ', e)
		
def print_records(data_list):
	
	try:
	
		for line in data_list:
				
			print(line, end='')
		
	except Exception as e:
	
		print('Print_Records Exception: ', e)