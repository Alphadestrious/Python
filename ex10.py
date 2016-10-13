tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

print tabby_cat
print persian_cat
print backslash_cat

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i, # this causes an infinite loop
		
		