
class Board:

	def __init__(self, index, board):
		self.index = index
		self.board = board
		self.winning_number = None

	def place(self, num):
		for y, row in enumerate(self.board):
			for x, val in enumerate(row):
				if val == num:
					self.board[y][x] = -1
					self.winning_number = num
					return True
		return False
	
	def bingo(self):
		for row in self.board:
			if all(x < 0 for x in row):
				return True

		for i in range(5):
			if all(x < 0 for x in [row[i] for row in self.board]):
				return True

		return False
	
	def score(self):
		return sum(sum(filter(lambda x: x > 0, row)) for row in self.board) * self.winning_number
	
	def __str__(self):
		s = ""
		for row in self.board:
			s += str(row) + "\n"
		return s

def read_input(filename):
	with open(filename, "r") as f:
		pool = [int(x) for x in f.readline().strip().split(",")]
		boards = []
		f.readline()
		for i, line in enumerate(f.read().split("\n\n")):
			board = [row.split() for row in line.split("\n")]
			boards.append(Board(i, [[int(x) for x in row] for row in board][:5]))
		return (pool, boards)

def part_1(data):
	pool, boards = data

	for num in pool:
		for board in boards:
			if (board.place(num) and
				board.bingo()):
				return board.score()
	
	return "Error: Board not found"

def part_2(data):
	pool, boards = data

	winners = []
	windex = set()
	for num in pool:
		for board in boards:
			if (board.index not in windex and
				board.place(num) and
				board.bingo()):
				winners.append(board)
				windex.add(board.index)

	return winners[-1].score()

if __name__ == "__main__":
	test = read_input("test")
	data = read_input("input")

	test_out_1 = 4512
	test_out_2 = 1924

	print(f"Test 1: {part_1(test)} | {test_out_1}")
	print(f"Part 1: {part_1(data)}")
	print("-----------------------")
	print(f"Test 2: {part_2(test)} | {test_out_2}")
	print(f"Part 2: {part_2(data)}")