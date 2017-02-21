COOPERATE = 0
DEFECT = 1


class Player(object):
    """
    This defines an interface for a player of the 3-player.
    Inherit and modify this class by declaring the following:
    class SecretStrategyPlayer(Player)
        # code goes here
        # make sure you implement the play(...) function
    Attributes:
    While you are not prohibited from adding attributes.  You should not need
    to implement do so.  The parameters to play(...) contain all information
    available about the current state of play.
    """

    def studentID(self):
        """ Returns the creator's numeric studentID """
        raise NotImplementedError("studentID not implemented")

    def agentName(self):
        """ Returns a creative name for the agent """
        return self.__class__.__name__

    def play(self, myHistory, oppHistory1, oppHistory2):
        """
        Given a history of play, computes and returns your next move
        ( 0 = cooperate; 1 = defect )
        myHistory = list of int representing your past plays
        oppHisotry1 = list of int representing opponent 1's past plays
        oppHisotry2 = list of int representing opponent 2's past plays
        NB: use len(myHistory) to find the number of games played
        """
        raise NotImplementedError("play not implemented")
