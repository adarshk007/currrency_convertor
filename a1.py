#a1.py
#adarsh kumar(2016007)
#deepanshu badshah(2016144)


	#now we have to make full url for make it operational
	#so we concatenate all the strings 

import urllib.request
	#now we have to make full url for make it operational
	#so we concatenate all the strings

#Part A:
def currency_response(currency_from,currency_to,amount_from):       
	
	
	source1="http://cs1110.cs.cornell.edu/2015fa/a1server.php?"
	a1="from="
	a2="&to="
	a3="&amt="
	
	#url formation
	url=source1+a1+currency_from+a2+currency_to+a3+str(amount_from)
	
	#now we have to open this given url
	#so what we do now use function urlopen()
	#make the object of its as j
	#Returns decoded string to utf-8 format
	with urllib.request.urlopen(url) as j:

	#Decoding of jstring string to utf-8 format.
		jstring=j.read().decode('utf-8')
	
	return jstring

#Part B:
def has_error(jstring):
	#Check if the jstring string is invalid or valid.
	if jstring.find("false")>=0:
		return "TRUE"
	else:
		return "FALSE"

#Part C:
#slicing part for removing float and string part
def before_space(s):
	d=int(s.index(' '))
	k=s[:d]
	return k

def after_space(s):
	
	d=int(s.index(' '))
	l=s[d+1:]
	return l


def exchange(currency_from,currency_to,amount_from):


	 
	jstring=currency_response(currency_from,currency_to,amount_from)
	
	
	
	if has_error(jstring)=='TRUE':
		return -1

	  
	
	
	q=jstring.find('"',11)
	k=jstring.find('"',q+10)
	e=jstring.find('"',k+1)
	
	 	
	s=jstring[k+1:e]

	
	#USING before_space and after_space function.
	value=before_space(s)
	currency=after_space(s)

	
	return float(value)


if __name__=='__main__':

	print (currency_response("USD","INR",.2))
	print (has_error('{ "lhs" : "0.2 United States Dollars", "rhs" : "13.341894 Indian Rupees", "valid" : false, "error" : "" }'))
	print (exchange("INR","USD",2.3))
