def computegrade(grade):
    if grade >1.0:
		print "Bad score"
    elif grade <=1.0 and grade >=0.9:
		print "A"
    elif grade >=0.8 and grade <0.9:
		print "B"
    elif grade >=0.7 and grade <0.8:
		print "C"
    elif grade >=0.6 and grade <0.7: 
		print "D"
    elif grade >0.0 and grade <0.6:
		print "F"
while(True):
	try:
		grade = float(raw_input("Enter score(0 for exit): "))
		if grade == 0 :
		    break
		computegrade(grade)
	except:
		print "Bad score"