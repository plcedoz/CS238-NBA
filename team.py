import random
import numpy as np

class Team(object):
    
    def __init__(self, teamNumber, PRConstant, winrateVSStyles, repeatPenaltyArr, playerHealthArr, numOfGamesFinished):
        
        self.teamNumber = teamNumber
        self.PRConstant = PRConstant
        self.winrateVSStyles = winrateVSStyless
        self.repeatPenaltyArr = repeatPenaltyArr
        self.playerHealthArr = playerHealthArr
        self.numOfGamesFinished = numOfGamesFinished
    
    def updateRepeatArr(self, action):
        """
        used to update the repeat penalty style array
        """
        self.repeatPenaltyArray[action] += 1
        
    def updatePlayerHealth(self): 
        """
        update the player health array
        players have a certain probability of getting injured the more games into the series, the more likely it is:
        """
        playerInjuryProb = 0.05 * 1.1**(self.numOfGamesFinished)
        for k in range(len(self.playerHealthArr)):
            self.playerHealthArr[k] = int(random.random() <= playerInjuryProb)
        
    def updateFinishedGames(self):
        """
        udpate the games played
        """
        self.numOfGamesFinished=self.numOfGamesFinished+1

    def updateTeam(self, action):
        self.updateRepeatArr(action)
        self.updatePlayerHealth()
        self.updateFinishedGames()
        
