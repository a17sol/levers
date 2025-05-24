from levers.geometry import *
from levers.motions import *
from levers.renderers import PyQtGraphRenderer


p1 = Point(rotating(x=0, y=0, r=2, f=0.25))
p2 = Point(static(x=4, y=0))
c1 = Circle(center=p1, radius=5)
c2 = Circle(center=p2, radius=5)
p3 = Point(intersect(c1, c2, lambda x, y: max(x, y, key=lambda a: (a[1], a[0]))))
p4 = Point(oncont(p1, p3, 5))
p5 = Point(static(x=0, y=0))
Line(p1, p4)
Line(p2, p3)
Line(p1, p5)
Trail(p4, 240)

PyQtGraphRenderer(-4, 11, -3, 12, 30).run(60)
