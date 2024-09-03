from Agent import Agent
from Environment import Environment

env = Environment()
agent = Agent(symbol = 'x', alpha = 0.1, gamma = 0.9)

if __name__ == '__main__':
  env = Environment()
  agent.Load()
  
  while True:
    print('player', env.GetNextPlayer(), '\'s turn')
    coordinate = input()
    coordinate = coordinate.split(' ')
    coordinate = [int(coordinate[0]), int(coordinate[1])]
    env.UpdateState(cell = coordinate)
    env.PrintState()
    print(agent.State2Index(env.GetState()))
    if env.Judge() != None:
      if env.Judge() == '_':
        print('draw')
      else:
        print(env.Judge() , 'winner.')
      env.ResetState()
      continue

    agent.PrintQValue(env.GetState(), env.GetAvailableCellList())
    ai_action = agent.CalculateOptimumAction(env.GetState(), env.GetAvailableCellList())
    print('ai action:', ai_action)
    env.UpdateState(cell = ai_action)
    env.PrintState()
    if env.Judge() != None:
      if env.Judge() == '_':
        print('draw')
      else:
        print(env.Judge() , 'winner.')
      env.ResetState()