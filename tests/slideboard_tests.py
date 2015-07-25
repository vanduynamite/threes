from nose.tools import *
import random
import threes

def setup():
    global board
    board = threes.Board()
    board.choose_placement_for_queued_cards = lambda replacement_cards: [0]

def teardown():
    print "TEAR DOWN!"

def test_slide_right():
    board.replacement_stack = [1]
    board.grid = [
            [1,2,1,2],
            [1,2,1,0],
            [1,1,1,1],
            [1,1,1,0]]

    slid_board_right = [
            [0,1,2,3],
            [0,1,2,1],
            [1,1,1,1],
            [1,1,1,1]]
    print slid_board_right[0]


    board.slide_right()
    assert_equal(board.grid, slid_board_right)

def test_slide_up():
    board.replacement_stack = [1]
    board.grid = [
            [1,1,0,0],
            [2,1,2,1],
            [1,1,1,1],
            [2,1,2,1]]

    slid_board_up = [
            [3,1,2,1],
            [1,1,1,1],
            [2,1,2,1],
            [0,1,0,1]]

    board.slide_up()
    assert_equal(board.grid, slid_board_up)

def test_slide_down():
    board.replacement_stack = [1]
    board.grid = [
            [2,1,2,1],
            [1,1,1,1],
            [2,1,2,1],
            [1,1,0,0]]

    slid_board_down = [
            [1,1,0,0],
            [2,1,2,1],
            [1,1,1,1],
            [3,1,2,1]]

    board.slide_down()
    assert_equal(board.grid, slid_board_down)

def test_slide_left():
    board.replacement_stack = [1]
    board.grid = [
            [2,1,2,1],
            [0,1,2,1],
            [1,1,1,1],
            [0,1,1,1]]

    slid_board_left = [
            [3,2,1,1],
            [1,2,1,0],
            [1,1,1,1],
            [1,1,1,0]]


    board.slide_left()
    assert_equal(board.grid, slid_board_left)


def test_quit():
    board.quit()
    assert_equal(board.quit(), None)



setup()
test_quit()
test_slide_right()
test_slide_up()
test_slide_down()
test_slide_left()
teardown()
