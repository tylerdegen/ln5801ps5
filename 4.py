import model

input = ["R : ohio = .5", "R : phil = .5", "W : /nek/ = .6", "W : /naek/ = .4",
"O ohio /nek/ : [nek] = 1", "O phil /nek/ : [nek] = .667", "O phil /nek/ : [naek] = .333",
"O ohio /naek/ : [naek] = 1", "O phil /naek/ : [naek] = 1"]

R = model.Model("R")
W = model.CondModel('W')
O = model.CondModel("O")

OgivR = model.CondModel('OR')

for line in input:
	R.read(line)
	W.read(line)
	O.read(line)
	
OgivNone = model.Model("Onone")

Idata = "I [naek] [nek] [naek]"
IdataSplit = Idata.split()
	
#w values aren't given for each time step, so condition out
for r, w in O:
	for o in O[r,w]:
		OgivR[r][o] += O[r,w][o] / 2
		OgivNone[o] += O[r,w][o] / 4

#for o in OgivNone:
	#print(o, OgivNone[o])


RgivenIdata = model.Model("RgivI")

for r in OgivR:
	for o in OgivR:
		RgivenIdata[r] 
	'''	
RgivenIdata = R
for o in IdataSplit:
	for r in RgivenIdata:
		if OgivR[r][o] != 0:
			RgivenIdata[r] *= OgivR[r][o]
'''
denominator = 0			
for r in RgivenIdata:
	for o in IdataSplit:
		denominator += OgivR[r][o] * OgivNone[o]
		
	numerator = OgivR[r][o] * R[r]
	RgivenIdata[r] = numerator / denominator
	denominator = 0
		
for r in RgivenIdata:
	print (r, RgivenIdata[r])