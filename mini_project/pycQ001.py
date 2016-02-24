import string
s = raw_input("Translate machine: ")
table = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print s.translate(table)#Q1