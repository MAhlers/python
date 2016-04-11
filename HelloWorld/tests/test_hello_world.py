import unittest
import os

class UnitTests(unittest.TestCase):
	
	def setUp(self):
		print('SetUp complete')
		#data_file = open('../src/classpkg/data/db.txt','r')
		#for line in data_file:
		#	print(line)
		#list(data_file)
		#data_file.close()
	
	def tearDown(self):
		print('TearDown complete')

import 
	def test_assert_string(self, testString): #testString):
		self.assertEqual('Hello, World!', 'Hello, World!')
		
if __name__ == '__main__':
	unittest.main()