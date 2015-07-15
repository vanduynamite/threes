import pdb
import numpy
import random

class Board(object):


    def __init__(self):
        self.replacement_stack = []
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
            #print "guess", "col: ", rand_col, "row: ", rand_row
            return rand_col, rand_row

        def position_is_empty(position):
            rand_col, rand_row = position
            #print "    is empty?", " |", self.grid[rand_col][rand_row] == 0, "|"
            return self.grid[rand_col][rand_row] == 0

        def choose_random_empty_position():
            while True:
                position = choose_random_position()
                if position_is_empty(position):
                    break
            return position
    
        #random.seed(8)
        #pdb.set_trace()
        populate_card_list = lambda num_threes, num_twos, num_ones: num_threes * [3] + num_twos * [2] + num_ones * [1]
        cardlist = populate_card_list(3,3,3)
        for i in cardlist:
            col, row = choose_random_empty_position()
            #self.display()
            self.set_card(col, row, i)

    ### These will transform the board, prepping it for sliding then transforming it back when done.  
    def slide_board(self,slide_direction):
            
        def replace_empty_cards(board):

            def get_rows_needing_replacement(board):
                
                # for row in board:
                #     print row
                
                open_spots = []

                for i in range(0,len(board)):
                    row = board[i]
                    if row[len(row)-1] == 'placeholder':
                        open_spots.append(i)
       
                return open_spots

            # just a random spot now
            def get_row_to_replace(indices):
                i = random.randint(0, len(indices) - 1)
                return indices[i]


            # just random for now
            def get_value_to_replace():
                return random.randint(1,3)

            rows_needing_replacement = get_rows_needing_replacement(board)
            row_to_replace = get_row_to_replace(rows_needing_replacement)
            value_to_replace = get_value_to_replace()

            # print ''
            # print rows_needing_replacement,
            # print "Replacing row " + str(row_to_replace) + " with " + str(value_to_replace)
            # print ''

            for i in rows_needing_replacement:
                if i == row_to_replace:
                    board[i][3] = value_to_replace
                else:
                    board[i][3] = 0

            return board


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
                
                """something in here is putting 'placeholder' on lines that were not squished. For instance [1,3,1,0] is getting a 'placeholder' at the end. No good!"""

                insert_value = 'placeholder'
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

        if slide_direction == 'left' or slide_direction == 'a':
            # no rotation!
            print 'Sliding the board left!'
            self.grid = squish_board(self.grid)
            self.grid = replace_empty_cards(self.grid)

        elif slide_direction == 'down' or slide_direction == 's':
            print 'Sliding the board down!'
            self.grid = rotate_board(self.grid, True)
            self.grid = squish_board(self.grid)
            self.grid = replace_empty_cards(self.grid)
            self.grid = rotate_board(self.grid, False)

        elif slide_direction == 'up' or slide_direction == 'w':
            print 'Sliding the board up!'
            self.grid = rotate_board(self.grid, False)
            self.grid = squish_board(self.grid)
            self.grid = replace_empty_cards(self.grid)
            self.grid = rotate_board(self.grid, True)

        elif slide_direction == 'right' or slide_direction == 'd':
            print 'Sliding the board right!'
            self.grid = rotate_board(self.grid, True)
            self.grid = rotate_board(self.grid, True)
            self.grid = squish_board(self.grid)
            self.grid = replace_empty_cards(self.grid)
            self.grid = rotate_board(self.grid, True)
            self.grid = rotate_board(self.grid, True)
        elif slide_direction == 'q':
            print 'Thanks for playing!'
        else:
            print 'Not a valid direction, try again. Use a, s, d, w, or q to quit.'

        # Next up add new numbers to the added places. Don't know the exact algorithm for adding them though. If you play the game there's a definite something going on there.


def main():
     my_board = Board()
     my_board.new_random_board()
     my_board.display()
     direction = ''
     while direction <> 'q':
         direction = raw_input(">>>(a,s,d,w,q)>>>")
         my_board.slide_board(direction)
         if direction <> 'q':
            my_board.display()

def test_paul():
    my_board = Board()
    my_board.new_random_board()
    #my_board.display()
    my_board.slide_board('a')
    my_board.display()

    open_spots = []

    for i in range(0,my_board.x_size):
        if my_board.get_card(i,my_board.y_size-1) == 'placeholder':
            open_spots.append(i)


def test_ryan():
    my_board = Board()
    my_board.new_random_board()
    my_board.display()
    my_board.slide_board('a')
    my_board.display()
    print my_board.grid()

if __name__ == "__main__":
    #test_paul() 
    main()








