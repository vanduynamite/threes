import random

class Board(object):


    def __init__(self, x_size, y_size):
         self.x_size = 4
         self.y_size = 4
         self.size= x_size * y_size

         self.grid = [[0 for i in range (0,y_size)] for j in range(0,x_size)]

    def display(self):
        #print self.grid
        print "Current Board:"
        for row in self.grid: print row

    def get_card(self, x, y):
        return self.grid[x][y]

    def set_card(self, x, y, value):
        self.grid[x][y] = value

    def new_random_board(self):
        num_threes = 4
        num_twos = 3
        num_ones = 2

        nums_to_place = []

        for i in range(0,num_threes):
            nums_to_place.append(3)
        for i in range(0,num_twos):
            nums_to_place.append(2)
        for i in range(0,num_ones):
            nums_to_place.append(1)

        nums_placed = 0
        
        for i in nums_to_place:
            
            location = random.randint(0,self.size - nums_placed-1)
            x_loc = location % self.y_size
            y_loc = (location - x_loc) / self.y_size

            while self.get_card(x_loc,y_loc) != 0:
                location += 1
                if location > self.size:
                    location = 0 
                x_loc = location % self.y_size
                y_loc = (location - x_loc) / self.y_size

            #print "Rand int between 0 and %d is %d: (%d, %d)" %(self.size-nums_placed,location, x_loc, y_loc)

            self.set_card(x_loc, y_loc, i)

            nums_placed += 1


    def new_set_board(self):
        pass



    ### These will transform the board, prepping it for sliding then transforming it back when done.  
    def slide_board(self,direction):
        # TODO
        """ 
        rotate board based on direction
        combine cards if they're in [3*2^^i for i in range(0,n)] n can be generated with bisection to save time
        
        """
        pass
    def is_stationary(self):
        """
        is there a zero or a wall adjacent to the sliding direction?
        """

        pass

    def combine_cards(self, stationary_card, moving_card):
        if stationary_card == moving_card:
            stationary_card += moving_card
    def transform_board(self,direction):
        pass

        def arrays_to_matrix():
            pass

        def rotate_left_90():
            pass

        def rotate_right_90():
            pass

        def rotate_180():
            pass

    def transform_board_back(():
            pass


def main():
    for i in range(0,1):
        my_board = Board(4,4)
        my_board.new_random_board()
        my_board.display()


if __name__ == "__main__":
    main()
