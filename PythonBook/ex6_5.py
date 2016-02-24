str = 'X-DSPAM-Confidence:0.8475'
colpos = str.find(':')
print type(colpos), colpos#check type
number = float(str[colpos+1:])
print type(number), number#check type