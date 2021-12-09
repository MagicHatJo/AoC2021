import statistics
import math

def read_input(filename):
	with open(filename, "r") as f:
		return [int(x) for x in f.read().split(",")]

def part_1(data):
	m = round(statistics.median(data))
	return sum([abs(m - n) for n in data])

def tri(n):
	return n * (n + 1) / 2

def part_2(data):
	m = statistics.mean(data)
	return int(min([sum([tri(abs(n - i)) for n in data]) for i in (math.floor(m), math.ceil(m))]))
	
if __name__ == "__main__":
	test = read_input("test")
	data = read_input("input")

	test_out_1 = 37
	test_out_2 = 168

	print(f"Test 1: {part_1(test)} | {test_out_1}")
	print(f"Part 1: {part_1(data)}")
	print("-----------------------")
	print(f"Test 2: {part_2(test)} | {test_out_2}")
	print(f"Part 2: {part_2(data)}")