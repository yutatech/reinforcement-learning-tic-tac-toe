from Agent import Agent
from Environment import Environment
import random
import copy

class EpsiloneGreedy:
  def __init__(self):
    pass
  
  def CalculateNextAction(self, optimum_action, available_action_list, optimum_ratio = 0.9):
    if random.random() > 1 - optimum_ratio:
      return optimum_action
    else:
      return available_action_list[random.randint(0, len(available_action_list)-1)]
    
    
    


env = Environment()
agent = Agent(symbol = 'x', alpha = 0.1, gamma = 0.9)
epsilone = EpsiloneGreedy()

for i in range(500000):
  env.ResetState()
  j= 0
  prv_state = None
  while True:
    print(j)
    j+=1
    opposit_player_action = epsilone.CalculateNextAction(agent.CalculateOptimumAction(env.GetState(), env.GetAvailableCellList()), \
                                               env.GetAvailableCellList(), optimum_ratio=0)
    env.UpdateState(opposit_player_action)
    env.PrintState()
    print()
    if env.Judge() == 'o':
      print('AI lose')
      reward = -1
    elif env.Judge() == 'x':
      print('AI won')
      reward = 1
    elif env.Judge() == '_':
      print('draw')
      reward = 0
    else:
      reward = 0
      
    if prv_state != None:
      print('here')
      if env.Judge() == None:
        agent.UpdateQ(prev_state=prv_state, prev_action_cell=prv_action, current_state = env.GetState(), available_cells=env.GetAvailableCellList(), reward=reward)
      else:
        agent.UpdateQ(prev_state=prv_state, prev_action_cell=prv_action, current_state=env.GetState(), available_cells=[], reward=reward)
        
    
    if env.Judge() != None:
      break
    ### ↑ 先手 o
    ### ↓ AI 'x'
    prv_state = env.GetState()
    prv_action = epsilone.CalculateNextAction(agent.CalculateOptimumAction(env.GetState(), env.GetAvailableCellList()), \
                                              env.GetAvailableCellList())

    env.UpdateState(prv_action)
    env.PrintState()
    print()
    if env.Judge() == 'o':
      print('AI lose')
      reward = -1
    elif env.Judge() == 'x':
      print('AI won')
      reward = 1
    elif env.Judge() == '_':
      print('draw')
      reward = 0
    else:
      reward = 0
    
    if env.Judge() != None:
      agent.UpdateQ(prev_state=prv_state, prev_action_cell=prv_action, current_state=env.GetState(), available_cells=[], reward=reward)
      break

agent.Save()
agent.SaveForGo()
      