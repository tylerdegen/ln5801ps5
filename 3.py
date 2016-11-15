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
		
GCP = model.Model("GCP")
PC = model.Model("PC")
for g in G:
	for p in C:
		for c in C[p]:
			GCP[g, p, c] = G[g] * P[g][p] * C[p][c]
			PC[p, c] += G[g] * P[g][p] * C[p][c]
			
PgivC = model.CondModel("CgivP")

print("PC:")
for p, c in PC:
	print(str(PC[p,c]), p, c)

CgivNone = model.Model("CgivNone")
for p in C:
	for c in C[p]:
		CgivNone[c] += C[p][c] / len(C[c])


#use bayesian!
for p in C:
	for c in C[p]:
		PgivC[c][p] = (C[p][c] * PgivNone[p] / CgivNone[c])


		
print("PgivC:")
for c in PgivC:
	for p in PgivC[c]:
		print(str(PgivC[c][p]), c, p)

