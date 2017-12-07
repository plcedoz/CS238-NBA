import pandas as pd
import numpy as np
import random

from generate import get_reward

class MDP(object):
    
    """Object that encapsulate the MDP and its methods
    
    Attributes:
        -states (list): List of states in the samples (subset of the full state space).
        -actions (list): List of actions in the samples (subset of the full action space).
        -discount (float): Discount factor.
        -Q (dataframe): Pandas dataframe that contains the Q(s,a) values for s in states and a in actions.
    
    """
    def __init__(self, teams, team_index, discount):
        
        self.teams = teams
        self.discount = discount
        self.team_index = team_index
        self.states = ["(%d, %d, %d)"%(a,b,c) for a in range(len(teams)) for b in range(len(teams)) for c in range(len(teams))]
        self.actions = ["A", "B", "C"]
        self.Q = pd.DataFrame(data=np.zeros((len(self.states),len(self.actions))), index=self.states, columns=self.actions,
                              dtype=float, copy=False)


    def q_learning(self, learning_rate, epsilon, nb_seasons):
        """Method that implements Q learning
    
        Args:
            -teams_data (dataframe): Dataset of the sampled transitions.
            -learning_rate (float): Learning rate for Qlearning.
            -n_iter (int): Number of iterations.

        """
        team = self.teams[self.team_index]
        opponents_Ids = [Id for Id in self.teams.keys() if Id != self.team_index]

        for season in range(nb_seasons):
            for opponent_Id in opponents_Ids:
                opponent = self.teams[opponent_Id]
                current_state = str(tuple(team.repeatPenalty.values()))
                action = self.choose_action(current_state, epsilon)
                reward = get_reward(team, opponent, action)
                team.update(action)
                next_state = str(tuple(team.repeatPenalty.values()))
                self.Q.loc[current_state, action] += learning_rate*(reward + self.discount*
                                                                    np.max([self.Q.loc[next_state,next_action] for next_action in
                                                                            self.actions]) - self.Q.loc[current_state, action])
            team.reset()
    
    
    
    def choose_action(self, current_state, epsilon):
        
        if random.random() < epsilon:
            action = np.random.choice(["A","B","C"])
        else:
            action = np.argmax(self.Q.loc[current_state, :])
        
        return action
        
        
        
        
        
        
        
        
        

