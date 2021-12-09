
import re
from collections import defaultdict

def read_input(filename):
	with open(filename, "r") as f:
		return [[int(x) for x in re.findall('[0-9]+', line)] for line in f.readlines()]

def parse_horizontal(vents, x1, x2, y1, y2):
	for y in range(min(y1, y2), max(y1, y2) + 1):
		vents[(x1, y)] += 1

def parse_vertical(vents, x1, x2, y1, y2):
	for x in range(min(x1, x2), max(x1, x2) + 1):
		vents[(x, y1)] += 1

def part_1(data):
	vents = defaultdict(lambda: 0)

	for x1, y1, x2, y2 in data:
		if x1 == x2:
			parse_horizontal(vents, x1, x2, y1, y2)
		elif y1 == y2:
			parse_vertical(vents, x1, x2, y1, y2)
	
	return len([True for x in vents.values() if x > 1])

def parse_diagonal(vents, x1, x2, y1, y2):
	x_step = 1 if x1 < x2 else -1
	y_step = 1 if y1 < y2 else -1

	for x, y in zip(
		range(x1, x2 + x_step, x_step),
		range(y1, y2 + y_step, y_step)
		):
		vents[(x, y)] += 1

def part_2(data):
	vents = defaultdict(lambda: 0)

	for x1, y1, x2, y2 in data:
		if x1 == x2:
			parse_horizontal(vents, x1, x2, y1, y2)
		elif y1 == y2:
			parse_vertical(vents, x1, x2, y1, y2)
		else:
			parse_diagonal(vents, x1, x2, y1, y2)
	
	return len([True for x in vents.values() if x > 1])

if __name__ == "__main__":
	test = read_input("test")
	data = read_input("input")

	test_out_1 = 5
	test_out_2 = 12

	print(f"Test 1: {part_1(test)} | {test_out_1}")
	print(f"Part 1: {part_1(data)}")
	print("-----------------------")
	print(f"Test 2: {part_2(test)} | {test_out_2}")
	print(f"Part 2: {part_2(data)}")