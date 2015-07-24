import random
from nose.tools import *
import threes

def setup():
    global board
    board = threes.Board()
    board.default_replacement_stack = [1]

def teardown():
    print "TEAR DOWN!"


def test_slide_left():
    """random.seed(0) results in an index of '3' for randint"""
    random.seed(0)
    board.grid = [
            [2,1,2,1],
            [0,1,2,1],
            [1,1,1,1],
            [0,1,1,1]]

    slid_board_left = [
            [3,2,1,0],
            [1,2,1,0],
            [1,1,1,1],
            [1,1,1,1]]


    board.slide_left()
    assert_equal(board.grid, slid_board_left)


setup()
test_slide_left()
teardown()
