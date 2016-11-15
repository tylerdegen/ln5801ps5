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

Idata = "I [naek] [nek] [naek]"
IdataSplit = Idata.split()

for o in IdataSplit:
	print(o)
	
for r, w in O:
	for o in O[r,w]:
		OgivR[r][o] += O[r,w][o] / 2
		
for r in OgivR:
	for o in OgivR[r]:
		print(o, r, str(OgivR[r][o]))

RgivenIdata = model.Model("RgivI")
for r in OgivR:
	for o in OgivR:
		RgivenIdata[r] 
		
RgivenIdata = R
for o in IdataSplit:
	for r in RgivenIdata:
		if OgivR[r][o] != 0:
			RgivenIdata[r] *= OgivR[r][o]
		
for r in RgivenIdata:
	print (r, RgivenIdata[r])