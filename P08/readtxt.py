def bacafile(nama, filter):
	f = open(nama)
	alldata = f.read().splitlines()
	N = len(alldata)
	allval = []
	for i in range(N):
		val = int(alldata[i])
		if (val > filter):
			print(val)
			allval.append(val)
	return allval