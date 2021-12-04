
def read_input(filename):
	with open(filename, "r") as f:
		return f.readlines()

def part_1(data):
	pass

def part_2(data):
	pass

if __name__ == "__main__":
	test = read_input("test")
	data = read_input("input")

	test_out_1 = 0
	test_out_2 = 0

	print(f"Test 1: {part_1(test)} | {test_out_1}")
	# print(f"Part 1: {part_1(data)}")
	# print("-----------------------")
	# print(f"Test 2: {part_2(test)} | {test_out_2}")
	# print(f"Part 2: {part_2(data)}")