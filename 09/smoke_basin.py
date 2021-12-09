import math

def read_input(filename):
	with open(filename, "r") as f:
		return {(x, y): int(n) for y, row in enumerate(f.read().split()) for x, n in enumerate(row)}

def find_lows(data):

	def is_low(x, y, v, data):
		for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
			if data.get((x + dx, y + dy), 9) <= v:
				return False
		return True

	for c, v in data.items():
		if is_low(*c, v, data):
			yield c

def part_1(data):
	return sum([data[c] + 1 for c in find_lows(data)])

def reverse_flood(x, y, v, data, basin):
	if (x, y) in basin:
		return 0

	basin[(x, y)] = 0
	
	if data[(x, y)] == 9:
		return 0
	
	for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
		if data.get((x + dx, y + dy), -1) > v:
			basin[(x, y)] += reverse_flood(x + dx, y + dy, v + 1, data, basin)

	basin[(x, y)] += 1
	return basin[(x, y)]

def part_2(data):
	basin = {}
	out = []

	for c in find_lows(data):
		v = data[c]
		basin[c] = reverse_flood(*c, v, data, basin)
		out.append(basin[c])

	return math.prod(sorted(out)[-3:])

if __name__ == "__main__":
	test = read_input("test")
	data = read_input("input")

	test_out_1 = 15
	test_out_2 = 1134

	print(f"Test 1: {part_1(test)} | {test_out_1}")
	print(f"Part 1: {part_1(data)}")
	print("-----------------------")
	print(f"Test 2: {part_2(test)} | {test_out_2}")
	print(f"Part 2: {part_2(data)}")