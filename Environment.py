import copy

class Environment:
  def __init__(self):
    self.state = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    self.judge_lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ]
    self.next_player = 'o'
    
  def PrintState(self):
    print(self.state[0][0], self.state[1][0], self.state[2][0])
    print(self.state[0][1], self.state[1][1], self.state[2][1])
    print(self.state[0][2], self.state[1][2], self.state[2][2])
    
  def UpdateState(self, cell: list[int]):
    if cell[0] < 0 or cell[0] > 2 or cell[1] < 0 or cell[1] > 2 or len(cell) != 2:
      print('[Environment.UpdateState] get invalid cell', cell, '.')
    self.state[cell[0]][cell[1]] = self.next_player
    if self.next_player == 'o':
      self.next_player = 'x'
    elif self.next_player == 'x':
      self.next_player = 'o'
    else:
      print('[Environment.UpdateState] invalid player', self.next_player, 'is set to next_player.')
      
  def GetAvailableCellList(self):
    available_cells = []
    for x in [0, 1, 2]:
      for y in [0, 1, 2]:
        if self.state[x][y] == '_':
          available_cells.append([x, y])
    return available_cells.copy()
  
  def Cell2Index(self, cell: list[int]):
    if cell[0] < 0 or cell[0] > 2 or cell[1] < 0 or cell[1] > 2 or len(cell) != 2:
      print('[Environment.Cell2Index] get invalid cell', cell, '.')
    return cell[0] * 3 + cell[1]
  
  def Index2Cell(self, index):
    if index < 0 or index > 8:
      print('[Environment.Index2Cell] get invalid index', index, '.')
    return [int(index / 3), index % 3]
    
  def GetState(self):
    return copy.deepcopy(self.state)
  
  def GetVectorState(self):
    state_temp = []
    for line in self.state:
      state_temp += line
    return state_temp.copy()
      
  def GetNextPlayer(self):
    return self.next_player
  
  def Judge(self):
    for line in self.judge_lines:
      if self.GetVectorState()[line[0]] == self.GetVectorState()[line[1]] and \
          self.GetVectorState()[line[1]] == self.GetVectorState()[line[2]] and \
          self.GetVectorState()[line[0]] != '_':
        return self.GetVectorState()[line[0]]
    for cells in self.state:
      for cell in cells:
        if cell == '_':
          return None # on going
    return '_' # draw
  
  def ResetState(self):
    self.state = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    self.next_player = 'o'

if __name__ == '__main__':
  env = Environment()

  while True:
    print('player', env.GetNextPlayer(), '\'s turn')
    coordinate = input()
    coordinate = coordinate.split(' ')
    coordinate = [int(coordinate[0]), int(coordinate[1])]
    env.UpdateState(cell = coordinate)
    env.PrintState()
    if env.Judge() != '_':
      print(env.Judge() , 'winner.')
      env.ResetState()