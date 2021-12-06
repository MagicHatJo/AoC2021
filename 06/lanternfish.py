
def read_input(filename):
	with open(filename, "r") as f:
		return [int(x) for x in f.read().split(",")]

def part(data, days):
	fish = [0] * 9

	for i in data:
		fish[i] += 1
	
	for i in range(days):
		active = fish[0]
		fish[0], fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7] = \
		fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7], fish[8]

		fish[6] += active
		fish[8] = active

	return sum(fish)

if __name__ == "__main__":
	test = read_input("test")
	data = read_input("input")

	test_out_1 = 5934
	test_out_2 = 26984457539

	print(f"Test 1: {part(test, 80)} | {test_out_1}")
	print(f"Part 1: {part(data, 80)}")
	print("-----------------------")
	print(f"Test 2: {part(test, 256)} | {test_out_2}")
	print(f"Part 2: {part(data, 256)}")