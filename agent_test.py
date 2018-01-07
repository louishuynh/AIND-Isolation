"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""
import timeit
import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)
        self.minimax_player = game_agent.MinimaxPlayer()

    def test_game_board_legal_moves(self):
        """ Make sure we can get all legal moves. """
        print('Legal moves: {}'.format(self.game.get_legal_moves()))

    def test_game_board_forecast_moves(self):
        print('Return of forecast moves: {}'.format(self.game.forecast_move((0, 0))))
        self.assertTrue(True)

    def test_minimax(self):
        time_millis = lambda: 1000 * timeit.default_timer()

        move_start = time_millis()
        time_left = lambda : 150 - (time_millis() - move_start)
        resp = self.minimax_player.get_move(self.game, time_left)
        print('Minimax response: {}'.format(resp))
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
