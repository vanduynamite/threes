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
        # if you want to define a board from the actual game
        pass



    ### These will transform the board, prepping it for sliding then transforming it back when done.  
    def slide_board(self,direction):
        # TODO
        """ 
        rotate board based on direction with transform_board
        use squish row to squish it
        rotate board back with transform_board_back
        """
        pass

        pass

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

    def transform_board_back():
            pass


def squish_list(num_row):
    # will always squish a list to the left

    first_num = num_row[0]

    if first_num == 0:
        # if the first thing in the list is 0, return everything in the list to the right followed by a 0
        num_row.pop(0)
        num_row.append(None)
        return num_row

    elif len(num_row) > 1:
        # if we're dealing with a list longer than 1 item...
        second_num = num_row[1]

        if first_num + second_num == 3 or (first_num != 1 and first_num != 2 and first_num == second_num):
            # if we can combine the first two in the list, do so and scoot the rest, add a 0 to the right
            num_row[0] = first_num + second_num
            num_row.pop(1)
            num_row.append(None)
            return num_row

        else:
            # if they can't combine then call squish_list on the rest of the list and stick the first item back in the front (phrasing)
            num_row = squish_list(num_row[1:])
            num_row.insert(0,first_num)
            return num_row

    else:
        # if the list is only one item, return it
        return num_row

def main():
    # for i in range(0,1):
    #     my_board = Board(4,4)
    #     my_board.new_random_board()
    #     my_board.display()
    nums = [2,1,0,0]
    print nums
    nums = squish_list(nums)
    print nums


if __name__ == "__main__":
    main()
