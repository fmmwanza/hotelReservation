
import unittest
import main 

from hotel import Hotel

class MyTeste(unittest.TestCase):
	"""docstring for MyTeste"""
	def setUp(self):
		unittest.TestCase.setUp(self)
		self.inputData = "Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"

	def tearDown(self):
		unittest.TestCase.tearDown(self)

	def testParseFile(self):
		 main.parseFile(self.inputData)

	def testCheapestHotel(self):
		result = main.parseFile(self.inputData)
		main.cheapestHotel(main.hotel, result)

	def testTiecase(self):
		inputTest = [{'value':10, 'name': 'Brigdewood', 'rate': 1}, 
					{'value':10, 'name': 'Lakewood', 'rate': 0}]
		main.tieCase(inputTest)

	def testTiecaseWork(self):
		inputTest = [{'value':10, 'name': 'Brigdewood', 'rate': 1}, 
					{'value':10, 'name': 'Lakewood', 'rate': 0}]
		result = main.tieCase(inputTest)
		self.assertEqual('Brigdewood', result)

	def testCheapestHotelWork(self):
		result = main.parseFile(self.inputData)
		res = main.cheapestHotel(main.hotel, result)
		self.assertEqual(res, 'Brigdewood')

	def testParseFileWork(self):
		result = main.parseFile(self.inputData)
		self.assertEqual(['Regular', 'fri','sat','sun'], result)
		
if __name__== '__main__':
	unittest.main()


