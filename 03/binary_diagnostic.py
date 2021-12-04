
import numpy as np
from collections import Counter

def read_input(filename):
	with open(filename, "r") as f:
		return np.array([list(x) for x in f.read().split()])

def mode(li):
	counter = Counter(li)
	max_count = max(counter.values())
	return [k for k, v in counter.items() if v == max_count]

def part_1(data):
	gamma = 0
	epsilon = 0
	
	for i, _ in enumerate(data[0]):
		m = int(max(mode(data[:, i])))
		gamma = gamma << 1 | m
		epsilon = epsilon << 1 | (1, 0)[m]

	return gamma * epsilon

def get_oxygen(data):
	i = 0
	while len(data) > 1:
		m = max(np.array(mode(data[:, i])))
		data = data[np.in1d(data[:,i], m)]
		i += 1
	return int(''.join(data[0]), 2)

def least_frequent(li):
	counter = Counter(li)
	min_count = min(counter.values())
	return [k for k, v in counter.items() if v == min_count]

def get_co2(data):
	i = 0
	while len(data) > 1:
		m = min(np.array(least_frequent(data[:, i])))
		data = data[np.in1d(data[:,i], m)]
		i += 1
	return int(''.join(data[0]), 2)

def part_2(data):
	return get_oxygen(data) * get_co2(data)

if __name__ == "__main__":
	test = read_input("test")
	data = read_input("input")

	test_out_1 = 198
	test_out_2 = 230

	print(f"Test 1: {part_1(test)} | {test_out_1}")
	print(f"Part 1: {part_1(data)}")
	print("-----------------------")
	print(f"Test 2: {part_2(test)} | {test_out_2}")
	print(f"Part 2: {part_2(data)}")