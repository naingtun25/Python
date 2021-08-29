from itertools import zip_longest as zip
with open("res.txt", 'w') as res, open("atoc.txt") as f1, open("fruits.txt") as f2:
	for line1, line2 in zip(f1, f2):
		res.write("{}{}\n".format(line1.rstrip(), line2.rstrip()))
