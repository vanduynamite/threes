import pdb
import numpy
import random
import copy # I know I'm sorry....

class Board(object):
    def __init__(self):
        self.default_replacement_stack = [1,1,1,1,2,2,2,2,3,3,3,3]
        self.replacement_stack = []
        self.replacement_stage_size = 1
        self.replacement_stage = []
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

    def find_rows_needing_replacement(self):
        place_holder_locations = []
        for i in range(0,len(self.grid)):
            row = self.grid[i]
            if row[-1] == 'placeholder':
                place_holder_locations.append(i)
        return place_holder_locations

    def queue_cards_from_stage(self, stage_size=1):
        replacement_cards = []
        for i in range(stage_size):
            replacement_cards.append(self.replacement_stage.pop(0))
        return replacement_cards
    
    def choose_placement_for_queued_cards(self):
        placeholder_locations = self.find_rows_needing_replacement()
        card_insert_locations = []
        for i in range(self.replacement_stage_size):
            card_insert_locations.append(random.randrange(0,len(placeholder_locations)))
        return card_insert_locations

    def place_queued_cards(self):
        cards_to_be_placed = self.queue_cards_from_stage()
        card_insert_locations = self.choose_placement_for_queued_cards()
        for i in card_insert_locations:
            self.grid[i][-1] = cards_to_be_placed.pop(0)

    def replace_remaining_placeholders_with_zeros(self):
        for i in range(len(self.grid)):
            if self.grid[i][-1] == "placeholder":
                self.grid[i][-1] = 0

    def update_stage(self):
        if len(self.replacement_stage) < self.replacement_stage_size:
            for i in range(self.replacement_stage_size):
                replacement_stack_length = len(self.replacement_stack)
                random_selection_from_stack = random.randrange(0, replacement_stack_length)
                card_from_stack = self.replacement_stack.pop(random_selection_from_stack)
                self.replacement_stage.append(card_from_stack)

    def update_replacement_stack(self):
        if len(self.replacement_stack) < 1:
            self.replacement_stack.extend(self.default_replacement_stack)

    def replace_cards(self):
        """did board slide?, if not do nothing"""
        self.update_stage()
        self.place_queued_cards()
        self.replace_remaining_placeholders_with_zeros()

    def squish_board(self):

        def squish_list(num_row):
            # will always squish a list to the left
            #pdb.set_trace()
            insert_value = 'placeholder'
            first_num = num_row[0]
            #print num_row

            if first_num == 0 and sum(x for x in num_row) != 0:
                # if the first thing in the list is 0, return everything in the list to the right followed by a 0
                num_row.pop(0)
                num_row.append(insert_value)
                return num_row
        
            elif len(num_row) > 1:
                # if we're dealing with a list longer than 1 item...
                second_num = num_row[1]

                #print num_row, first_num, second_num
                if is_addable(first_num, second_num):
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

        def is_addable(first_num, second_num):
            if first_num != 0 and second_num != 0 and first_num + second_num == 3:
                # in this case the numbers are 1 and 2 (or 2 and 1)
                return True
            elif first_num != 0 and first_num != 1 and second_num != 2 and first_num == second_num:
                # in this case the numbers are not 0, 1, or 2, but are the same, so can be added
                return True
            else:
                return False

        for i in range(0,len(self.grid)):
            self.grid[i] = squish_list(self.grid[i])

    def rotate_clockwise(self):
        self.rotate_board(0, self.y_size - 1, self.x_size, -1)

    def rotate_counter_clockwise(self):
        self.rotate_board(self.x_size - 1, 0, -1, self.y_size)

    def rotate_board(self, start_lat, start_long, end_lat, end_long):
        step_lat = numpy.sign(end_lat - start_lat)
        step_long = numpy.sign(end_long - start_long)

        new_board = []

        for i in range(start_lat, end_lat, step_lat):
            sub_list = []

            for j in range(start_long, end_long, step_long):
                sub_list.append(self.grid[j][i])

            new_board.append(sub_list)

        self.grid = new_board

    def update_board(self):
        self.update_replacement_stack()
        if self.is_board_squishable():
            self.squish_board()
            self.replace_cards()
        else:
            print "Sorry Fool, you can't slide that way"

    def slide_left(self):
        print 'Sliding the board left!'
        self.update_board()

    def slide_down(self):
        print 'Sliding the board down!'
        self.rotate_clockwise()
        self.update_board()
        self.rotate_counter_clockwise()

    def slide_up(self):
        print 'Sliding the board up!'
        self.rotate_counter_clockwise()
        self.update_board()
        self.rotate_clockwise()

    def slide_right(self):
        print 'Sliding the board right!'
        self.rotate_clockwise()
        self.rotate_clockwise()
        self.update_board()
        self.rotate_clockwise()
        self.rotate_clockwise()

    def quit(self):
        print 'Thanks for playing!'

    def not_a_valid_choice(self):
        print 'Not a valid direction, try again. Use a, s, d, w, or q to quit.'




    def new_random_board(self):

        def choose_random_position():
            rand_col = random.randint(0,self.x_size - 1)
            rand_row = random.randint(0,self.y_size - 1)
            return rand_col, rand_row

        def position_is_empty(position):
            rand_col, rand_row = position
            return self.grid[rand_col][rand_row] == 0

        def choose_random_empty_position():
            position = choose_random_position()
            while not position_is_empty(position):
                position = choose_random_position()
            return position
    
        populate_card_list = lambda num_threes, num_twos, num_ones: num_threes * [3] + num_twos * [2] + num_ones * [1]
        cardlist = populate_card_list(3,3,3)
        for i in cardlist:
            col, row = choose_random_empty_position()
            #self.display()
            self.set_card(col, row, i)

    def new_set_board(self):
        self.grid = [[2,12,3,0],[3,0,0,0]]

    def slide_board(self,slide_direction):
        slide_actions = {
                'q':self.quit,
                'a':self.slide_left,
                'left':self.slide_left,
                'd':self.slide_right,
                'right':self.slide_right,
                's':self.slide_down,
                'down':self.slide_down,
                'w':self.slide_up,
                'up':self.slide_up}
        if slide_direction in slide_actions:
            slide_actions[slide_direction]()
        else:
            self.not_a_valid_choice()

    def is_board_squishable(self):
        pre_slide_grid = copy.deepcopy(self.grid)
        self.squish_board()

        placeholder_locations = self.find_rows_needing_replacement()
        self.grid = copy.deepcopy(pre_slide_grid)
        return len(placeholder_locations) != 0


    def is_board_slideable_at_all(self):
        """slides the board in all directions"""
        """returns which directions the board can be slid in"""
        pass
        


def main():
    my_board = Board()
    my_board.new_random_board()
    my_board.display()
    direction = ''
    while direction != 'q':
        """can_you_even_slide_bro?"""
        direction = raw_input(">>>(a,s,d,w,q)>>>")
        my_board.slide_board(direction)
        if direction != 'q':
            my_board.display()

#def test_paul():
    #my_board = Board()
    #my_board.new_random_board()
    ##my_board.display()
    #my_board.slide_board('a')
    #my_board.display()

    #open_spots = []

    #for i in range(0,my_board.x_size):
        #if my_board.get_card(i,my_board.y_size-1) == 'placeholder':
            #open_spots.append(i)


#def test_ryan():
    #my_board = Board()
    #my_board.new_random_board()
    #my_board.display()
    #my_board.slide_board('a')
    #my_board.display()
    #print my_board.grid()

if __name__ == "__main__":
    #test_paul() 
    main()








