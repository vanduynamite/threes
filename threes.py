
class Board(object):


	def __init__(self, x_size, y_size):
		 self.x_size = 4
		 self.y_size = 4

		 self.rows = [0 for x in range (0,x_size)]
		 self.cols = [self.rows for x in range(0,y_size)]

	def display(self):
		print self.cols,


def main():
	my_board = Board(4,4)
	my_board.display()


if __name__ == "__main__":
	main()


#git add --all
#git commit
#(in vim) - i, esc, comment, :wq
#git push
