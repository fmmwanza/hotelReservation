class Hotel(object):

	hotelName = None
	def __init__(self, hotelName):
		super(Hotel, self).__init__()
		self.hotelName = hotelName

	def getInfo(self):
		if self.hotelName == "Lakewood":
			return  {"name": self.hotelName, "rate": 3,"Regular": {"WeekDay": 110, "WeekEnd": 90}, 
										  	 "Rewards": {"WeekDay": 80, "WeekEnd": 80}}
		if self.hotelName == "Brigdewood":
			return  {"name": self.hotelName, "rate": 4,"Regular": {"WeekDay": 160, "WeekEnd": 60}, 
										 	 "Rewards": {"WeekDay": 110, "WeekEnd": 50}}
		if self.hotelName == "Rigdewood":
			return  {"name": self.hotelName, "rate": 5,"Regular": {"WeekDay": 220, "WeekEnd": 150}, 
										  	 "Rewards": {"WeekDay": 100, "WeekEnd": 40}}
	
	def dayType(self, day):
		if day == 'sat' or day == 'sun' :
			return 'WeekEnd'
		else:
			return 'WeekDay'

	def totalValue(self, inputValue):
		result = 0
		info = self.getInfo()								#get the hotel informations
		customerType = info[inputValue[0]]					#get the customer type
		for i in range(1,4):
			result +=  customerType[self.dayType(inputValue[i])] # For each day, return and add the value into result --It seems confuse, but it's the best way to do, I think !!!!
		return {'value':result, 'name': info['name'], 'rate':info['rate']} 