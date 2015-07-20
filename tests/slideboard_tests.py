from nose.tools import *
import threes

def setup():
    global board
    board = threes.Board()
    board.new_random_board()
    return board
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_quit():
    board.quit()
    assert_equal(board.quit(), None)



setup()
test_quit()
teardown()
