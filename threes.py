import numpy
import random

class Board(object):


    def __init__(self):
         self.x_size = 4
         self.y_size = 4
         self.size= self.x_size * self.y_size

         self.grid = [[0 for i in range (0,self.y_size)] for j in range(0,self.x_size)]

    def display(self):
        print "Current Board:"
        for row in self.grid: print row
        print ""

    def get_card(self, x, y):
        return self.grid[x][y]

    def set_card(self, x, y, value):
        self.grid[x][y] = value


    def new_random_board(self):

        def choose_random_position():
            rand_col = random.randint(0,self.x_size - 1)
            rand_row = random.randint(0,self.y_size - 1)
            return rand_col, rand_row

        def is_position_empty(position):
            rand_col, rand_row = position
            if self.grid[rand_col][rand_row] != 0:
                return False
            else:
                return True

        def choose_random_empty_position():
            while True:
                position = choose_random_position()
                if is_position_empty(position) != False:
                    break
            return position
    
        #random.seed(8)

        populate_card_list = lambda num_threes, num_twos, num_ones: num_threes * [3] + num_twos * [2] + num_ones * [1]
        numlist = populate_card_list(3, 3, 3)
        for i in numlist:
            col, row = choose_random_empty_position()
            self.set_card(col, row, i)

    def new_set_board(self):
        # if you want to define a board from the actual game
        pass


    ### These will transform the board, prepping it for sliding then transforming it back when done.  
    def slide_board(self,slide_direction):

        def rotate_board(board, clock):
            # counter goes right to left, top to bottom
            # clock goes left to right, bottom to top

            if clock:
                start_lat = 0
                end_lat = self.x_size

                start_long = self.y_size - 1
                end_long = -1
            else:
                start_lat = self.x_size - 1
                end_lat = -1

                start_long = 0
                end_long = self.y_size

            step_lat = numpy.sign(end_lat - start_lat)
            step_long = numpy.sign(end_long - start_long)

            new_board = []

            for i in range(start_lat, end_lat, step_lat):
                sub_list = []

                for j in range(start_long, end_long, step_long):
                    sub_list.append(self.grid[j][i])

                new_board.append(sub_list)

            return new_board

        def squish_board(board):

            def squish_list(num_row):
                # will always squish a list to the left
                insert_value = 0
                first_num = num_row[0]

                if first_num == 0:
                    # if the first thing in the list is 0, return everything in the list to the right followed by a 0
                    num_row.pop(0)
                    num_row.append(insert_value)
                    return num_row
            
                elif len(num_row) > 1:
                    # if we're dealing with a list longer than 1 item...
                    second_num = num_row[1]
                    if first_num + second_num == 3 or (first_num != 1 and first_num != 2 and first_num == second_num):
                        # if we can combine the first two in the list, do so and scoot the rest, add a 0 to the right
                        num_row[0] = first_num + second_num
                        num_row.pop(1)
                        num_row.append(insert_value)
                        return num_row
            
                    else:
                        # if they can't combine then call squish_list on the rest of the list and stick the first item back in the front (phrasing)
                        num_row = squish_list(num_row[1:])
                        num_row.insert(0,first_num)
                        return num_row
            
                else:
                    # if the list is only one item, return it
                    return num_row

            for i in range(0,len(board)):
                board[i] = squish_list(board[i])

            # Why does this not work?????? Sometimes but not others...
            # for row in board:
            #     row = squish_list(row)

            return board

        print 'Sliding the board %s!' % slide_direction

        if slide_direction == 'left' or slide_direction == 'j':
            # no rotation!
            self.grid = squish_board(self.grid)

        elif slide_direction == 'down' or slide_direction == 'k':
            self.grid = rotate_board(self.grid, True)
            self.grid = squish_board(self.grid)
            self.grid = rotate_board(self.grid, False)

        elif slide_direction == 'up' or slide_direction == 'i':
            self.grid = rotate_board(self.grid, False)
            self.grid = squish_board(self.grid)
            self.grid = rotate_board(self.grid, True)

        elif slide_direction == 'right' or slide_direction == 'l':
            self.grid = rotate_board(self.grid, True)
            self.grid = rotate_board(self.grid, True)
            self.grid = squish_board(self.grid)
            self.grid = rotate_board(self.grid, True)
            self.grid = rotate_board(self.grid, True)
        else:
            print 'Not a valid direction, try again. Use left, up, right, down, i, j, k, or l'

        # Next up add new numbers to the added places. Don't know exactly where to add them though.


def main():
     for i in range(0,1):
         my_board = Board()
         my_board.new_random_board()
         my_board.display()
         while True:
             direction = raw_input(">>>(i,j,k,l)>>>")
             my_board.slide_board(direction)
             my_board.display()




if __name__ == "__main__":
    main()
