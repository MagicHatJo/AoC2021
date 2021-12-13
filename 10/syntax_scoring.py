from collections import defaultdict
import statistics

def read_input(filename):
	with open(filename, "r") as f:
		return f.readlines()

def check_valid(line):
	matching = {
		'(' : ')',
		'[' : ']',
		'{' : '}',
		'<' : '>'
	}
	stack = []

	for bracket in line:
		if bracket in "([{<":
			stack.append(bracket)
		elif bracket in ")]}>":
			if matching[stack[-1]] == bracket:
				stack.pop()
			else:
				return None, bracket
	return stack, None
	
def part_1(data):
	illegal = defaultdict(lambda: 0)
	for line in data:
		_, error = check_valid(line)
		if error is not None:
			illegal[error] += 1

	return (illegal[')'] * 3 +
			illegal[']'] * 57 +
			illegal['}'] * 1197 +
			illegal['>'] * 25137)

def complete(stack):
	score = 0
	matching = {
		'(' : 1,
		'[' : 2,
		'{' : 3,
		'<' : 4
	}
	for bracket in reversed(stack):
		score *= 5
		score += matching[bracket]
	return score


def part_2(data):
	illegal = defaultdict(lambda: 0)
	scores = []
	for line in data:
		stack, _ = check_valid(line)
		if stack is not None:
			scores.append(complete(stack))
	return statistics.median(scores)

if __name__ == "__main__":
	test = read_input("test")
	data = read_input("input")

	test_out_1 = 26397
	test_out_2 = 288957

	print(f"Test 1: {part_1(test)} | {test_out_1}")
	print(f"Part 1: {part_1(data)}")
	print("-----------------------")
	print(f"Test 2: {part_2(test)} | {test_out_2}")
	print(f"Part 2: {part_2(data)}")