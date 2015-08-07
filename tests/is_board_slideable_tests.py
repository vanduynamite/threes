from nose.tools import *
import threes

def setup():
    global board
    board = threes.Board()

def teardown():
    print "TEAR DOWN!"

def test_slide_left():
    board.replacement_stack = [2]
    board.grid = [
            [0,2,2,2],
            [2,2,2,2],
            [2,2,2,2],
            [2,2,2,2]
            ]

    slid_board = [
            [2,2,2,2],
            [2,2,2,2],
            [2,2,2,2],
            [2,2,2,2]
            ]
    
    lose_output = "You Lose"

    board.slide_left()
    #assert_equal(board.grid, slid_board)

    board.slide_left()
    assert_equal(buffer, lose_output)


for i in range(100):
    setup()
    test_slide_left()
    teardown()
