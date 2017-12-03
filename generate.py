import random
import numpy as np

from team import Team


def compute_PR(team1, team2, action1):
    
    #Update the power ratings
    PRs1=team1.PRConstant-repeatPenaltyScaler*team1.repeatPenaltyArr
    PRs2=team2.PRConstant-repeatPenaltyScaler*team2.repeatPenaltyArr

    #UNIMPLEMENTED YET: update with the player injury update
    
    PR1_picked = PRs1[action1];
    action2 = np.argmax(PRs2)
    PR2_picked = PRs2[action2] #assume opponent always plays their most dominant style at the beginning

    #scale them with (1-win rate) of the opponent vs the style they pick
    WRs1=team1.winrateVSStyles
    WRs2=team2.winrateVSStyles

    PR1_picked = PR1_picked * (1 - WRs2[action1])
    PR2_picked = PR2_picked * (1 - WRs1[action2])
    
    return PR1_picked, PR2_picked, action2
    
    
def get_reward_next_state(state, action1, repeatPenaltyScaler=10):

    team1 = state.team1
    team2 = state.team2

    PR1_picked, PR2_picked, action2 = compute_PR(team1, team2, action1)

    #generate the reward by drawing from distribution
    proba = PR1_picked/(PR1_picked+PR2_picked)
    reward = int(random.random() < proba)

    team1.updateTeam(action1)
    team2.updateTeam(action2)
    next_state = State(team1, team2)
    
    return reward, next_state


