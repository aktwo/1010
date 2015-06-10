from pieces import all_pieces
from time import sleep
import random

class TenTen:

  # Initialize empty board of size n.
  def __init__(self, n = 0):
    self.board = [[None for i in range(n)] for j in range(n)]
    self.surface_area = 0
    self.score = 0

  # Simple getter method to return the contents of the board at an arbitrary position.
  def get_contents_at(self, position):
    i, j = position
    return self.board[i][j]

  # Simple setter method to sent the contents of the board at an arbitrary position.
  def set_contents_at(self, position, value):
    i, j = position
    self.board[i][j] = value

  # Checks to see if position is on the board.
  def is_valid_position(self, position):
    i, j = position
    return i >= 0 and i < len(self.board) and j >= 0 and j < len(self.board[i])

  # Checks if the specified piece can be placed at the specified position.
  def is_valid_move(self, piece, position):
    for position in self._get_absolute_positions(piece, position):
      if self.is_valid_position(position):
        if self.get_contents_at(position):
          return False # Another piece is already in this spot
      else:
        return False # Part of the piece is off the board
    return True

  # Place piece into position
  def place(self, piece, position):
    i, j = position
    # Check that move is valid
    if self.is_valid_move(piece, position):

      # Set all piece positions
      absolute_piece_positions = self._get_absolute_positions(piece, position)
      for absolute_piece_position in absolute_piece_positions:
        self.set_contents_at(absolute_piece_position, 1)

      # Update surface area
      self.surface_area += self._marginal_surface_area(piece, position)

      # Update score
      self.score += len(piece)

      self._cleanup()
    else:
      raise ArgumentError("Invalid move: piece cannot be placed at this position")

  def play(self):
    while True:

      # Get three random pieces
      available_pieces = [random.choice(all_pieces) for i in range(3)]

      while len(available_pieces) > 0:

        # print self

        piece, position = self._get_optimal_piece_and_position(available_pieces)

        # Handle the case of no valid moves remaining
        if piece is None and position is None:
          return self.score

        del available_pieces[available_pieces.index(piece)]
        self.place(piece, position)

  ### Generators

  # This function generates all of the positions neighbors on the board.
  def neighbors(self, position):
    x, y = position
    offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dx, dy in offsets:
      if self.is_valid_position((x + dx, y + dy)):
        yield (x + dx, y + dy)

  # This function generates all of the positions on the board.
  def board_positions(self):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        yield (i, j)

  ### Helper methods

  # Gives the change in surface area when inserting piece into position.
  # This function assumes that piece can be placed into position.
  def _marginal_surface_area(self, piece, position):
    marginal_surface_area = 0
    absolute_piece_positions = self._get_absolute_positions(piece, position)
    for absolute_piece_position in absolute_piece_positions:
      for position in self.neighbors(absolute_piece_position):
        if self.get_contents_at(position) is None:
          marginal_surface_area += 1
        elif position not in absolute_piece_positions:
          marginal_surface_area -= 1
    return marginal_surface_area

  # Given a piece and a reference position, this method generates the 
  # absolute coordinates of the piece.
  def _get_absolute_positions(self, piece, position):
    i, j = position
    return map(lambda (x, y): (x + i, y + j), piece)

  # Given a list of pieces, return (optimal piece, optimal position)
  def _get_optimal_piece_and_position(self, pieces):
    current_SA = self.surface_area
    best_SA = None
    best_position = None
    best_piece = None
    for position in self.board_positions():
      for piece in pieces:
        if self.is_valid_move(piece, position):
          marginal_SA = self._marginal_surface_area(piece, position)
          if best_SA is None or current_SA + marginal_SA < best_SA:
            best_piece = piece
            best_SA = current_SA + marginal_SA
            best_position = position
    return (best_piece, best_position)

  def _cleanup(self):
    # Check rows
    rows = []
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if self.board[i][j] is None:
          break
      else:
        rows.append(i)

    # Check columns
    columns = []
    for j in range(len(self.board[0])):
      for i in range(len(self.board)):
        if self.board[i][j] is None:
          break
      else:
        columns.append(j)

    # Update score
    self.score += (len(rows) * len(self.board)) + (len(columns) * len(self.board)) - (len(columns) * len(rows))

    # Cleanup
    marginal_surface_area = 0
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if i in rows or j in columns:
          self.board[i][j] = None

  def __str__(self):
    output = []
    for i in range(len(self.board)):
      for j in range(len(self.board)):
        output.append("{0:5}".format(self.board[i][j]))
      output.append('\n')
    return "".join(output)

trials = 30
hi_score = 0
for i in range(trials):
  print i
  board = TenTen(10)
  hi_score = max(hi_score, board.play())
print hi_score

# board1 = TenTen()
# assert(board1.surface_area == 0)

# board2 = TenTen(7)
# board2.place([(0, 0), (0, 1), (0, 2)], (0, 1))
# assert(board2.surface_area == 5)

# board3 = TenTen()
# board3.board = \
#          [[1, 1, 1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1, 1, 1]]
# board3.cleanup()
# assert(board3.board == [[None for i in range(7)] for j in range(7)])


# board4 = TenTen()
# board4.board = \
#          [[    1,    1,    1,    1,    1,    1,    1],
#           [ None,    1,    1,    1,    1,    1,    1],
#           [    1, None,    1,    1,    1,    1,    1],
#           [    1,    1,    1,    1,    1,    1,    1],
#           [    1,    1,    1, None,    1,    1,    1],
#           [    1,    1,    1,    1, None,    1,    1],
#           [    1,    1,    1,    1,    1, None,    1]]
# desired_board4 = \
#          [[ None, None, None, None, None, None, None],
#           [ None,    1, None,    1,    1,    1, None],
#           [    1, None, None,    1,    1,    1, None],
#           [ None, None, None, None, None, None, None],
#           [    1,    1, None, None,    1,    1, None],
#           [    1,    1, None,    1, None,    1, None],
#           [    1,    1, None,    1,    1, None, None]]
# board4.cleanup()
# assert(board4.board == desired_board4)
