
n = []
i = 0
while (True):
    try:   
		number = raw_input("Enter a number: ")
		if number == 'done':
		    break
		n.append(float(number))
    except:
        print "Invalid input"
print n, len(n), sum(n), sum(n)/len(n), max(n), min(n)