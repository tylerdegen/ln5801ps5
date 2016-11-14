import model

input = ["R : ohio = .5", "R : phil = .5", "W : /nek/ = .6", "W : /naek/ = .4",
"O ohio /nek/ : [nek] = 1", "O phil /nek/ : [nek] = .667", "O phil /nek/ : [naek] = .333",
"O ohio /naek/ : [naek] = 1", "O phil /naek/ : [naek] = 1"]

R = model.Model("R")
W = model.CondModel('W')
O = model.CondModel("O")

for line in input:
	R.read(line)
	W.read(line)
	O.read(line)

Idata = "I [naek] [nek] [naek]"

RivenIdata = model.Model("RgivI")
