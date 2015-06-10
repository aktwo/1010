single = [(0, 0)]
double_vert = [(0, 0), (1, 0)]
double_horiz = [(0, 0), (0, 1)]
triple_vert = [(0, 0), (1, 0), (2, 0)]
triple_horiz = [(0, 0), (0, 1), (0, 2)]
quad_vert = [(0, 0), (1, 0), (2, 0), (3, 0)]
quad_horiz = [(0, 0), (0, 1), (0, 2), (0, 3)]
quint_vert = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
quint_horiz = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
small_square = [(0, 0), (1, 0), (0, 1), (1, 1)]
large_square = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
corner_top_left = [(0, 0), (1, 0), (0, 1)]
corner_bottom_left = [(0, 0), (-1, 0), (0, 1)]
corner_top_right = [(0, 0), (1, 0), (0, -1)]
corner_bottom_right = [(0, 0), (-1, 0), (0, -1)]

all_pieces = \
[single, double_vert, double_horiz, triple_vert, triple_horiz, \
quad_vert, quad_horiz, quint_vert, quint_horiz, small_square, \
large_square, corner_bottom_right, corner_top_right, \
corner_bottom_left, corner_top_left]
