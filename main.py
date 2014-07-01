from hotel import Hotel
import sys

hotel = []

def parseFile(fileLine):
	result = []
	parseTmp = fileLine.split(':') 	# parse the input file's line
	customerType = parseTmp[0]		# get my customer type, 'Regular' or 'Rewards'
	tmpStr = parseTmp[1]
	result.append(customerType)

	tmp = tmpStr.split('(')
	for par in tmp:
		if ')' in par:
			result.append(par.split(')')[0])
	return result

def tieCase(listTie):
	tmp = listTie[0]['rate']
	highest = listTie[0]
	for i in range(len(listTie)):
		if tmp < listTie[i]['rate']:
			highest = listTie[i]
			tmp = listTie[i]['rate']
	return highest['name']

def cheapestHotel(hotel, inputArg):
	listTie = []
	temp = hotel[0].totalValue(inputArg)
	listTie.append(temp)
	tmp = temp['value']
	hotelResult = temp['name']

	for i in range(len(hotel)):
		res = hotel[i].totalValue(inputArg)
		if tmp >= res['value']:
			if tmp == res['value']:
				listTie.append(res)		# if more than one hotel has the same value, save it into the list
			tmp = res['value']
			hotelResult = res['name']

	if len(listTie) != 1:
		hotelResult = tieCase(listTie)
	else:
		return hotelResult

	return hotelResult

def main(argv):
		if len(argv) != 2:
			sys.exit('run command line: python [name].py [inputTextFIle].txt')

		inputFile = open(str(sys.argv[1]),'r')	#open input file
		fileLine = inputFile.readline()	
		if not fileLine :
			sys.exit('Invalid input file')

		inputArg = parseFile(fileLine)

		"""Create my instances for each hotel"""
		hotel.append(Hotel('Brigdewood'))
		hotel.append(Hotel('Rigdewood'))
		hotel.append(Hotel('Lakewood'))

		inputFile.close()
		print cheapestHotel(hotel, inputArg)

main(sys.argv)	# run 