from functools import reduce
with open("day20data.txt", "r") as f:
    DATA = f.read().splitlines()
accel = 1000
particle = 0
simul = []
for i in range(len(DATA)):
    DATA[i] = DATA[i].split(" ")
    partacc = DATA[i][2].split(",")
    partacc = list(map(lambda x: int(x), [partacc[0][3:], partacc[1], partacc[2][:-1]]))
    tempacc = reduce((lambda x, y: abs(x) + abs(y)), partacc)
    partvel = DATA[i][1].split(",")
    partvel = list(map(lambda x: int(x), [partvel[0][3:], partvel[1], partvel[2][:-1]]))
    tempvel = reduce((lambda x, y: abs(x) + abs(y)), partvel)
    partpos = DATA[i][0].split(",")
    partpos = list(map(lambda x: int(x), [partpos[0][3:], partpos[1], partpos[2][:-1]]))
    temppos = reduce((lambda x, y: abs(x) + abs(y)), partpos)
    simul.append([partpos, partvel, partacc])
    DATA[i][2] = tempacc
    DATA[i][1] = tempvel
    DATA[i][0] = temppos
    DATA[i].append(i)

steps = 0
while steps < 100000:
    
DATA = sorted(DATA, key=lambda x: (x[2], x[1], x[0]))
print(DATA[0])
