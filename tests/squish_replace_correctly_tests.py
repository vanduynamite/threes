from nose.tools import *
import random
import threes

def setup():
    global board
    board = threes.Board()
    board.choose_placement_for_queued_cards = lambda : [0]

def teardown():
    print "TEAR DOWN!"

def test_slide_left():
    board.replacement_stack = [1]
    board.grid = [
            [24,2,6,2],
            [12,2,0,0],
            [1,6,0,0],
            [0,2,0,0]
            ]

    slid_board = [
            [24,2,6,2],
            [12,2,0,0],
            [1,6,0,0],
            [2,0,0,1]
            ]


    board.slide_left()
    assert_equal(board.grid, slid_board)




for i in range(100):
    setup()
    test_slide_left()
    teardown()
