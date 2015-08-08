from nose.tools import *
import threes

def setup():
    global board
    board = threes.Board()

def teardown():
    print "TEAR DOWN!"

def test_is_board_slideable():
    board.replacement_stack = [2]
    board.grid = [
            [2,2,2,2],
            [2,2,2,2],
            [2,2,2,2],
            [3,2,2,2]
            ]
    original_board = [
            [2,2,2,2],
            [2,2,2,2],
            [2,2,2,2],
            [3,2,2,2]
            ]

    is_board_slideable_output = board.is_board_slideable_at_all()
    assert_equal(is_board_slideable_output, False)
    assert_equal(board.grid, original_board)


setup()
test_is_board_slideable()
teardown()
