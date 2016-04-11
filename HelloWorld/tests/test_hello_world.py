import os
import unittest

class UnitTests(unittest.TestCase):
	
	def setUp(self):
		
		print('SetUp Complete.')
	
	def test_assert_string(self): #testString):
		
		db_path = '../data/db.txt'
		
		self.assertTrue(os.path.isfile(db_path))

		data_file = open(db_path,'r')
					
		data_list = data_file.readlines()
		
		row_count = len(data_list)
		
		if row_count > 0:
			
			for line in data_list:
				print(line, end='')
		
		data_file.close()
		
		self.assertEqual(data_list[0].replace('\n',''), 'Hello')
		
	@unittest.skip("Only to Test Functionality.")
	def test_print(self):
		print(os.path.dirname(os.path.abspath(__file__)), '\n')
	
	def tearDown(self):
		print('TearDown Complete.')
		
if __name__ == '__main__':
	unittest.main()