from levers import *
from levers.renderers import PyQtGraphRenderer


red_line = Style(color="#FF0000FF", width=1, visible=True)

O = Point(static(0.645, 0.402))
C = Point(static(0, 0))
F = Point(static(-1.6552, -0.12578))

A = Point(rotating(O.x, O.y, 0.305, 0.33))
circ_A = Circle(A, 1)
circ_C = Circle(C, 1)
B = Point(on_intersection(circ_A, circ_C, upper_left))
M = Point(on_angle_side(B, A, -114, 1))
circ_M = Circle(M, 0.66)
circ_F = Circle(F, 0.8)
D = Point(on_intersection(circ_M, circ_F, upper_left))
W = Point(on_line(D, F, -1))

Line(A, O)
Line(B, C)
Line(A, B, style=red_line)
Line(B, M, style=red_line)
Line(M, D)
Line(W, F, style=red_line)

PyQtGraphRenderer(-2.75, 1.5, -0.75, 2, 150).run(60)
# PyQtGraphRenderer(-2.75, 1.5, -0.75, 2, 150).capture(fps=60, frames=180, path='capture_folder')
