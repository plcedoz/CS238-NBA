import random
import numpy as np


def compute_PR(team, opponent, action, repeatPenaltyScaler=100000):
    
    PR_team = team.PRs[action]-repeatPenaltyScaler*team.repeatPenalty[action]
    action_opponent = list(opponent.PRs.keys())[np.argmax(list(opponent.PRs.values()))]
    PR_opponent = opponent.PRs[action_opponent]-repeatPenaltyScaler*opponent.repeatPenalty[action_opponent]

    #Scale them with (1-win rate) of the opponent vs the style they pick
    PR_team = PR_team * (1 - opponent.WRs[action])
    PR_opponent = PR_opponent * (1 - team.WRs[action_opponent])
    
    return PR_team, PR_opponent

def get_reward(team, opponent, action):

    PR_team, PR_opponent = compute_PR(team, opponent, action)

    #generate the reward by drawing from distribution
    proba = PR_team/(PR_team+PR_opponent)
    reward = int(random.random() < proba)
    
    return reward


