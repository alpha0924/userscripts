import time
import copy

start_time = time.time()

steps = 1
start_floors = [["EG", "EM", "DG", "DM", "SG", "SM", "PG", "PM"], ["TG", "RG", "RM", "CG", "CM"], ["TM"], []]
start_elevator = 0
moves = []
seen = []
checked = []
found = False

def check_valid(dest, pt1, pt2, validfloors, validelevator):
	testdest = list(validfloors[dest])
	testdest.append(pt1)
	if pt2 != "":
		testdest.append(pt2)

	for i in testdest:
		if i[1] == "M":
			for j in testdest:
				if j[1] == "G" and i[0] + "G" not in testdest:
					return False

	if pt1 not in validfloors[validelevator]:
		return False
	if pt2 != "" and pt2 not in validfloors[validelevator]:
		return False

	testfloor = list(validfloors[validelevator])
	testfloor.remove(pt1)
	if pt2 != "":
		testfloor.remove(pt2)
	for i in testfloor:
		if i[1] == "M" and i[0] + "G" not in testfloor:
			for j in testfloor:
				if j != i and j[1] == "G":
					return False
	return True



def do_move(destination, part1, part2, infloors, inelevator):
	global steps
	movefloors = copy.deepcopy(infloors)
	moveelevator = int(inelevator)
	valid = check_valid(destination, part1, part2, movefloors, moveelevator)
	state = [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0], destination]
	if not valid:
		return False
	else:
		movefloors[destination].append(part1)
		if part2 != "":
			movefloors[destination].append(part2)
		movefloors[moveelevator].remove(part1)
		if part2 != "":
			movefloors[moveelevator].remove(part2)
		movefloors[destination] = sorted(movefloors[destination])
		moveelevator = destination
	for i in range(4):
		for j in movefloors[i]:
			if j[1] == "M":
				if j[0] + "G" not in movefloors[i]:
					state[i][0] += 1
				else:
					state[i][2] += 1
			else:
				if j[0] + "M" not in movefloors[i]:
					state[i][1] += 1

	return [movefloors, moveelevator, state, steps]



for i in start_floors[start_elevator]:
	test = do_move(1, i, "", start_floors, start_elevator)
	if test != False and test[2] not in seen:
		moves.append(test)
		seen.append(test[2])
	for j in start_floors[start_elevator]:
		if i != j:
			test = do_move(1, i, j, start_floors, start_elevator)
			if test != False and test[2] not in seen:
				moves.append(test)
				seen.append(test[2])

while not found:
	steps += 1
	print(len(moves))
	for i in copy.deepcopy(moves):
		moves.remove(i)
		if len(i[0][3]) == 14:
			print(i)
			found = True
			break
		floors = i[0]
		elevator = i[1]
		testfloors = copy.deepcopy(floors)
		testelevator = int(elevator)
		for p1 in testfloors[testelevator]:
			for p2 in testfloors[testelevator]:
				if p1 != p2:
					if testelevator < 3:
						test = do_move(testelevator + 1, p1, p2, testfloors, testelevator)
						if test != False and test[2] not in seen:
							moves.append(test)
							seen.append(test[2])
			if testelevator < 3:
				test = do_move(testelevator + 1, p1, "", testfloors, testelevator)
				if test != False and test[2] not in seen:
					moves.append(test)
					seen.append(test[2])
			testfloors = copy.deepcopy(floors)
			if elevator > 1 and all(testfloors[x] == [] for x in range(1, elevator)):
				continue
			if testelevator > 0:
				test = do_move(testelevator - 1, p1, "", testfloors, testelevator)
				if test != False and test[2] not in seen:
					moves.append(test)
					seen.append(test[2])
			for p2 in testfloors[testelevator]:
				if p1[0] != p2[0]:
					if testelevator > 0:
						test = do_move(testelevator - 1, p1, p2, testfloors, testelevator)
						if test != False and test[2] not in seen:
							moves.append(test)
							seen.append(test[2])

print("Run time: %s" % (time.time() - start_time))