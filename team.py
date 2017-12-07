import numpy as np
import pandas as pd


class Team(object):
    
    def __init__(self, PRs, WRs):
        
        self.PRs = PRs
        self.WRs = WRs
        self.repeatPenalty = {'A':0, 'B':0, 'C':0}
        #self.playerHealthArr = playerHealthArr
        #self.numOfGamesFinished = numOfGamesFinished
    
    def update(self, action):
        """
        used to update the repeat penalty style array
        """
        self.repeatPenalty[action] += 1
    
    def reset(self):
        self.repeatPenalty = {'A':0, 'B':0, 'C':0}
    
    
def get_teams(filename="Data/teams_data.csv"):
    
    data = pd.read_csv(filename, header = None).iloc[:,1:7]
    data.columns = ["PRA", "PRB", "PRC", "WRA", "WRB", "WRC"]
    teams = {}
    for i in range(len(data)):
        stats = data.iloc[i,:]
        PRs = {"A": stats["PRA"], "B": stats["PRB"], "C": stats["PRC"]}
        WRs = {"A": stats["WRA"], "B": stats["WRB"], "C": stats["WRC"]}
        teams[i] = Team(PRs, WRs)
    return teams    
    
    
    
    
    
    
    #def updatePlayerHealth(self): 
    #    """
    #    update the player health array
    #    players have a certain probability of getting injured the more games into the series, the more likely it is:
    #    """
    #    playerInjuryProb = 0.05 * 1.1**(self.numOfGamesFinished)
    #    for k in range(len(self.playerHealthArr)):
    #        self.playerHealthArr[k] = int(random.random() <= playerInjuryProb)
    #    
    #def updateFinishedGames(self):
    #    """
    #   udpate the games played
    #    """
    #    self.numOfGamesFinished=self.numOfGamesFinished+1

    #def updateTeam(self, action):
    #    self.updateRepeatArr(action)
        #self.updatePlayerHealth()
        #self.updateFinishedGames()
        
