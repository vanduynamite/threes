from nose.tools import *
#import main
import threes

def setup():
    threes.new_game()
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_quit():
    slide_board("q")



setup()
#test_quit()
teardown()
