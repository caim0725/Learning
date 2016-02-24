def countnum(string,letter):
    count = 0
    for i in string:
	    if i == letter:
		    count += 1
    print count
word = raw_input("Enter the article: ")
letter = raw_input("which word you want to calc? ")
countnum(word,letter)