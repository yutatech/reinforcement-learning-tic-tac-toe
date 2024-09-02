import pickle
import copy

class Agent:
  def __init__(self, symbol: str, alpha, gamma):
    self.q_afterstate = [0] * (3**9)
    self.symbol = symbol
    self.alpha = alpha
    self.gamma = gamma
    pass
  
  def Save(self, file_name = 'q_table'):
    with open(file_name, 'wb') as file:
      pickle.dump(self.q_afterstate, file)
      
  def Load(self, file_name = 'q_table'):
    with open(file_name, 'rb') as file:
      self.q_afterstate = pickle.load(file)
  
  def CalculateOptimumAction(self, current_state, available_action_cells: list[list[int]]):
    if len(available_action_cells) == 1:
      return available_action_cells[0].copy()

    max_action = available_action_cells[0].copy()
    for i in range(1, len(available_action_cells)):
      if self.q(current_state, available_action_cells[i]) > self.q(current_state, max_action):
        max_action = available_action_cells[i].copy()
    return max_action.copy()
      
  def PrintQValue(self, current_state, available_action_cells: list[list[int]]):
    for cells in available_action_cells:
      print(cells, self.q(current_state, cells))
    
  def q(self, state, action_cell:list[int]):
    return self.q_afterstate[self.CalculateAfterStateIndex(state, action_cell)]
    
  def CalculateAfterStateIndex(self, state, action_cell:list[int]):
    after_state = copy.deepcopy(state)
    after_state[action_cell[0]][action_cell[1]] = self.symbol
    return self.State2Index(after_state)
    
  def State2Index(self, state):
    index = 0
    for i in range(9):
      if state[int(i/3)][i%3] == '_':
        value = 0
      elif state[int(i/3)][i%3] == 'o':
        value = 1
      elif state[int(i/3)][i%3] == 'x':
        value = 2
      else:
        print('Agent.State2Index() state[', int(i/3), '][' + i%3 + '] is invalid \'', state[int(i/3)[i%3]], '\'')
      index += value * (3**i)
    return index
  
  def Index2State(self, index):
    state = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    for i in range(9):
      if index % 3 == 0:
        state[int(i/3)][i%3] = '_'
      elif index % 3 == 1:
        state[int(i/3)][i%3] = 'o'
      elif index % 3 == 2:
        state[int(i/3)][i%3] = 'x'
      index = int(index/3)
    return state
    
  
  def UpdateQ(self, prev_state, prev_action_cell, current_state, available_cells, reward):
    max_q = 0
    for cell in available_cells:
      print(cell, self.q(current_state, cell))
      max_q = max(max_q, self.q(current_state, cell))
      
    print('---')
    print('max_q', max_q)
    
    self.q_afterstate[self.CalculateAfterStateIndex(prev_state, prev_action_cell)] = \
      (1 - self.alpha) * self.q_afterstate[self.CalculateAfterStateIndex(prev_state, prev_action_cell)] + \
      self.alpha * (reward + self.gamma * max_q)
    print('q', self.q_afterstate[self.CalculateAfterStateIndex(prev_state, prev_action_cell)])
    state = self.Index2State(self.CalculateAfterStateIndex(prev_state, prev_action_cell))
    for line in state:
      print(line)
    print('---')