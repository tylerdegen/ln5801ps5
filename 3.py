#here we go writing python

#read in models of language change over generation of speakers
#ultimately want PgivC

import model

input = ["G : who = .1", "G : whom = .9", "P who : who = 1", "P who : whom = 0", 
"P whom : who = .2", "P whom : whom = .8", "C who : who = 1", "C who : whom = 0", 
"C whom : who = .5", "C whom : whom = .5"]

G = model.Model('G')
#PgivG
P = model.CondModel('P')
#CgivP
C = model.CondModel('C')

for line in input:
	G.read(line)
	P.read(line)
	C.read(line)
	print line
	
PgivNone = model.Model("PgivNone")
for g in P:
	for p in P[g]:
		PgivNone[p] += P[g][p] / len(P[p])
		

PgivC = model.CondModel("CgivP")
CgivNone = model.Model("CgivNone")
for p in C:
	for c in C[p]:
		CgivNone[c] += C[p][c] / len(C[c])
		PgivC[c][p] = 0

for p in PgivNone:
	print(str(PgivNone[p]), p)
for c in CgivNone:
	print(str(CgivNone[c]), c)

print("probability, given chhild pronunciation, parent pronunciation")

for g in G:
	for p in P:
		for c in C:
			PgivC[c][p] += C[p][c] * P[g][p]

for c in PgivC:
	for p in PgivC[c]:
		#PgivC[c][p] = C[p][c] * PgivNone[p] / CgivNone[c]
		print(str(PgivC[c][p]), c, p)

#for c in P:
#	for p in P[c]:
#		PgivC[c][p] += P[

#for c, p in P:
#	PgivC[c][p] 