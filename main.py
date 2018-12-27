from __future__ import unicode_literals

models, rules, PDA = 'SPOK', [
	'SPO',
	'SPOK',
	'SPK',
	'SP'
], []

# adding models
for file in list(models):
	with open("models/{}.dat".format(file)) as u:
		exec("{} = {}".format(file, u.read().splitlines()))

def iS(txt):
	txt = list(txt)

	# init
	if not PDA: PDA.append('#')
	for i in txt: PDA.append(i)

	# final state adding lambda
	PDA.append(None)

	# check
	candidate = []
	for dataset in map(lambda x:x.lower(), S):
		if len(dataset) == len(txt):
			candidate.append(dataset)

	start = len(txt)-1
	while PDA.pop() != "#":
		tmp = PDA[len(PDA)-1] # get last char (LIFO)
		if tmp == "#": continue # pop initial symbol

		for i, c in enumerate(candidate):
			if tmp != c[start]:
				del candidate[i]
				break

		start -= 1
		
	return 0 if not candidate else 1

def iP(txt):
	txt = list(txt)

	# init
	if not PDA: PDA.append('#')
	for i in txt: PDA.append(i)

	# final state adding lambda
	PDA.append(None)

	# check
	candidate = []
	for dataset in map(lambda x:x.lower(), P):
		if len(dataset) == len(txt):
			candidate.append(dataset)

	start = len(txt)-1
	while PDA.pop() != "#":
		tmp = PDA[len(PDA)-1] # get last char (LIFO)
		if tmp == "#": continue # abaikan

		for i, c in enumerate(candidate):
			if tmp != c[start]:
				del candidate[i]
				break

		start -= 1
		
	return 0 if not candidate else 1

def iO(txt):
	txt = list(txt)

	# init
	if not PDA: PDA.append('#')
	for i in txt: PDA.append(i)

	# final state adding lambda
	PDA.append(None)

	# check
	candidate = []
	for dataset in map(lambda x:x.lower(), O):
		if len(dataset) == len(txt):
			candidate.append(dataset)

	start = len(txt)-1
	while PDA.pop() != "#":
		tmp = PDA[len(PDA)-1] # get last char (LIFO)
		if tmp == "#": continue # abaikan

		for i, c in enumerate(candidate):
			if tmp != c[start]:
				del candidate[i]
				break

		start -= 1
		
	return 0 if not candidate else 1

def iK(txt):
	txt = list(txt)

	# init
	if not PDA: PDA.append('#')
	for i in txt: PDA.append(i)

	# final state adding lambda
	PDA.append(None)

	# check
	candidate = []
	for dataset in map(lambda x:x.lower(), K):
		if len(dataset) == len(txt):
			candidate.append(dataset)

	start = len(txt)-1
	while PDA.pop() != "#":
		tmp = PDA[len(PDA)-1] # get last char (LIFO)
		if tmp == "#": continue # abaikan

		for i, c in enumerate(candidate):
			if tmp != c[start]:
				del candidate[i]
				break

		start -= 1
		
	return 0 if not candidate else 1

state, _ = [], map(str, raw_input('>> ').split())
for st in _: state.append(st)

result = ""
for kata in state:
	if iS(kata): result += "S"
	if iP(kata): result += "P"
	if iO(kata): result += "O"
	if iK(kata): result += "K"

print ">> {} | {} [{}]".format(' '.join(state), '-'.join(result.split()), 'OK' if result in rules else '!OK')
