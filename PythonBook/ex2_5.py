celsius = raw_input('Enter the temperature in Celsius:')
try:
	fahrenheit = int(celsius,10)*9/5.0+32
	print 'transfer to '+str(fahrenheit)+' Fahrenheit degree'
except:
	print 'Please enter a number'