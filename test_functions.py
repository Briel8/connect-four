import unittest
from cf_functions import ConnectFour

class TestConnectFourFunctions(unittest.TestCase):
    """For testing all of the methods of ConnectFour class."""


    def test_switch_turn_to_be_0(self):
        """Is turn switched to '0'?"""
        cf = ConnectFour()
        turn = cf.switch_turn()
        self.assertEqual(turn, '0')

    def test_switch_turn_to_be_X(self):
        """Is turn switched to 'X'?"""
        cf = ConnectFour()
        cf.turn = '0'
        turn = cf.switch_turn()
        self.assertEqual(turn, 'X')

    def test_check_win_1(self):
        """Will winner turned to X?"""
        cf = ConnectFour()
        cf.board = [
             #0   #1   #2   #3   #4   #5   #6
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #0
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #1
            ['_', 'X' ,'_' ,'_' ,'_' ,'_' ,'_'],    #2
            ['_', 'X' ,'_' ,'_' ,'_' ,'_' ,'_'],    #3
            ['_', 'X' ,'_' ,'_' ,'_' ,'_' ,'_'],    #4
            ['_', 'X' ,'_' ,'_' ,'_' ,'_' ,'_'],    #5
            
        ]
        cf.check_win(2, 1)
        self.assertEqual(cf.winner, 'X')
    
    def test_check_win_2(self):
        """Will winner turned to X?"""
        cf = ConnectFour()
        cf.board = [
             #0   #1   #2   #3   #4   #5   #6
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #0
            ['_', 'X' ,'X' ,'X' ,'X' ,'_' ,'_'],    #1
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #2
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #3
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #4
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #5
            
        ]
        cf.check_win(2, 4)
        self.assertEqual(cf.winner, 'X')

    def test_check_win_2(self):
        """Will winner turned to 0?"""
        cf = ConnectFour()
        cf.turn = '0'
        cf.board = [
             #0   #1   #2   #3   #4   #5   #6
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #0
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #1
            ['_', '_' ,'_' ,'0' ,'0' ,'0' ,'0'],    #2
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #3
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #4
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #5
            
        ]
        cf.check_win(2, 3)
        self.assertEqual(cf.winner, '0')

unittest.main()