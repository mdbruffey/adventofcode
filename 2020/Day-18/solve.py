def part1(data):
	rules, messages = data.split("\n\n")
	rules = rules.split("\n")
	messages = messages.split("\n")
	rdict = {}
	for rule in rules:
		rid, r = rule.split(": ")
		rdict[rid] = r.strip('"')
	
	rstring = rdict["0"]
	for char in loc:
		if char not in "ab |":
				
			rs =
			for rid in rs:
				rstring.append(rdict[rid])
			rstring.remove(loc)
	
	
def part2(data):
	pass

with open("input.txt") as file:
	data = file.read()
	
res1= part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")