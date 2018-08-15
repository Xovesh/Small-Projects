from chess import Piece


class Bishop(Piece.Piece):

    def __init__(self, identificator, color, x, y):
        super().__init__(identificator, color, x, y)
        self.__name = "Bishop"
        self.__firstmove = True

    def getfirstmove(self):
        return self.__firstmove

    def setfirstmove(self):
        self.__firstmove = False

    def getname(self):
        return self.__name

    def __str__(self):
        return "B"

    def __repr__(self):
        return "B"