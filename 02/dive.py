
def read_input(filename):
	with open(filename, "r") as f:
		return [(x[0], int(x[1])) for x in map(str.split, f.readlines())]

def part_1(data):
	position = 0
	depth = 0

	table = {
		"forward" : lambda p, d, u: (p + u, d),
		"up"      : lambda p, d, u: (p, d - u),
		"down"    : lambda p, d, u: (p, d + u)
	}

	for direction, unit in data:
		position, depth = table[direction](position, depth, unit)

	return position * depth

def part_2(data):
	position = 0
	depth = 0
	aim = 0

	table = {
		"forward" : lambda p, d, a, u: (p + u, d + a * u, a),
		"up"      : lambda p, d, a, u: (p, d, a - u),
		"down"    : lambda p, d, a, u: (p, d, a + u)
	}

	for direction, unit in data:
		position, depth, aim = table[direction](position, depth, aim, unit)

	return position * depth

if __name__ == "__main__":
	test = read_input("test")
	data = read_input("input")

	test_out_1 = 150
	test_out_2 = 900

	print(f"Test 1: {part_1(test)} | {test_out_1}")
	print(f"Part 1: {part_1(data)}")
	print("-----------------------")
	print(f"Test 2: {part_2(test)} | {test_out_2}")
	print(f"Part 2: {part_2(data)}")