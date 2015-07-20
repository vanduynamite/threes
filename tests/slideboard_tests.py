from nose.tools import *
import threes

def setup():
    global board
    board = threes.Board()


    print "SETUP!"


def teardown():
    print "TEAR DOWN!"

def test_slide_right():
    board.grid = [
            [1,2,1,2],
            [1,2,1,0],
            [1,1,1,1],
            [1,1,1,0]]

    slid_board_right = [
            ["placeholder",1,2,3],
            ["placeholder",1,2,1],
            [1,1,1,1],
            ["placeholder",1,1,1]]


    board.slide_right()
    assert_equal(board.grid, slid_board_right)

def test_slide_up():
    board.grid = [
            [1,1,0,0],
            [2,1,2,1],
            [1,1,1,1],
            [2,1,2,1]]

    slid_board_up = [
            [3,1,2,1],
            [1,1,1,1],
            [2,1,2,1],
            ["placeholder",1,"placeholder","placeholder"]]

    board.slide_up()
    assert_equal(board.grid, slid_board_up)

def test_slide_down():
    board.grid = [
            [2,1,2,1],
            [1,1,1,1],
            [2,1,2,1],
            [1,1,0,0]]

    slid_board_down = [
            ["placeholder",1,"placeholder","placeholder"],
            [2,1,2,1],
            [1,1,1,1],
            [3,1,2,1]]

    board.slide_down()
    assert_equal(board.grid, slid_board_down)

def test_slide_left():
    board.grid = [
            [2,1,2,1],
            [0,1,2,1],
            [1,1,1,1],
            [0,1,1,1]]

    slid_board_left = [
            [3,2,1,"placeholder"],
            [1,2,1,"placeholder"],
            [1,1,1,1],
            [1,1,1,"placeholder"]]


    board.slide_left()
    assert_equal(board.grid, slid_board_left)


def test_quit():
    board.quit()
    assert_equal(board.quit(), None)

#def test_all_slide_directions():
    #board.slide_left()
    #board.slide_right()
    #board.slide_down()
    #board.slide_up()


setup()
test_quit()
test_slide_right()
test_slide_up()
test_slide_down()
test_slide_left()
teardown()
