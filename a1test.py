#adarsh kumar(2016007)
#deepanshu(2016144)


import unittest
from a1 import *


class testpoint(unittest.TestCase):


	#Testing the currency_response(currency_from,currency_to,amount_from) function

	def testresponse(self):
		self.assertEqual(currency_response('USD','INR','2.5'),'{ "lhs" : "2.5 United States Dollars", "rhs" : "166.773675 Indian Rupees", "valid" : true, "error" : "" }')
		self.assertEqual(currency_response('INR','EUR','50'),'{ "lhs" : "50 Indian Rupees", "rhs" : "0.67179367487105 Euros", "valid" : true, "error" : "" }')
		self.assertEqual(currency_response('ANG','MMK','45'),'{ "lhs" : "45 Netherlands Antillean Guilders", "rhs" : "30665.287336908 Myanma Kyats", "valid" : true, "error" : "" }')
		self.assertEqual(currency_response('AED','AFN','100'),'{ "lhs" : "100 United Arab Emirates Dirhams", "rhs" : "1814.5213492641 Afghan Afghanis", "valid" : true, "error" : "" }')
		self.assertEqual(currency_response('IDR','INR','500'),'{ "lhs" : "500 Indonesian Rupiah", "rhs" : "2.5187166562836 Indian Rupees", "valid" : true, "error" : "" }')
		self.assertEqual(currency_response('IMR','LLR','10'),'{ "lhs" : "", "rhs" : "", "valid" : false, "error" : "Source currency code is invalid." }')

	#Testing the has_error(json) function
	def testquery(self):
		self.assertEqual(has_error('{ "lhs" : "", "rhs" : "", "valid" : false, "error" : "Source currency code is invalid." }'),'TRUE')
		self.assertEqual(has_error('{ "lhs" : "100 United Arab Emirates Dirhams", "rhs" : "1814.5213492641 Afghan Afghanis", "valid" : true, "error" : "" }'),'FALSE')
		self.assertEqual(has_error('{ "lhs" : "", "rhs" : "", "valid" : false, "error" : "Currency amount is invalid." }'),'TRUE')
		self.assertEqual(has_error('{ "lhs" : "", "rhs" : "", "valid" : false, "error" : "Exchange currency code is invalid." }'),'TRUE')
		self.assertEqual(has_error('{ "lhs" : "566 United States Dollars", "rhs" : "2078.948564 United Arab Emirates Dirhams", "valid" : true, "error" : "" }'),'FALSE')

	#Testing the exchange(currency_from, currency_to, amount_from) function	
	def testexchange(self):
		self.assertEqual(exchange('INR','USD','100'),1.4990375429456)
		self.assertEqual(exchange('AED','INR','45'),817.28342409341)
		self.assertEqual(exchange('INR','USD','700'),10.493262800619)
		self.assertEqual(exchange('BAM','USD','0'),0.0)
		self.assertEqual(exchange('EUR','AED','20'),81.960370411693)
			


if __name__=='__main__':
	unittest.main()
