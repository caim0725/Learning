while(True):
	try:
		hours = raw_input("Enter Hours(or type zero to exit): ")
		if float(hours) == 0.0:
			break
		rate = raw_input("Enter Rate: ")
		hours = float(hours)
		rate = float(rate)
		pay = 0.0
		if hours > 40 :
			pay = rate*(40.0+(hours-40.0)*1.5)
			print pay
		elif hours > 0 and hours <= 40 :
			pay = hours * rate
			print pay
	except:
		print "Pls enter number!"