from main import Bishop, Board

board = Board()
bishop = Bishop(0)


def test_add_peice():
    board.add_peice(bishop)
    