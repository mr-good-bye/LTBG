import bext
from random import randint
try:
    import LTBGTextEngine.constants as constants
except Exception:
    import constants

bext.bg(constants.BG_COLOR)
bext.fg(constants.FG_COLOR)


class Renderer:
    # TODO: add percent_position(p) => p(10%, 10%) => p(0.1width, 0.1height)
    def __init__(self, title=constants.APP_TITLE):
        bext.title(title)
        self.size = bext.size()

    def go_to(self, p: (int, int)):
        if not self._check_outside_(p):
            raise ValueError("point is outside of box")
        bext.goto(*p)

    def input(self):
        bext.show()
        r = input()
        bext.hide()
        return r

    def _check_outside_(self, p: (int, int), p_max: (int, int) = None):
        """
            Checks if point is inside terminal
        :param p: point to check
        :param p_max: max point (size of renderer if None)
        :return: bool point is inside
        """
        p_max = p_max if p_max else (self.size[0]-1, self.size[1])
        return p[0] < p_max[0] and p[1] < p_max[1]

    def resize(self):
        self.size = bext.size()

    def line(self, p1: (int, int), p2: (int, int), c: str = '#'):
        """
        :param p1: point (x, y) start
        :param p2: point (x, y) end
        :param c: = '#' param to fill
        :return: None, but draws a line
        """
        _t = self._check_outside_(p1)
        _t = _t and self._check_outside_(p2)
        if not _t:
            raise ValueError("point is outside of box")

        if p1[0] > p2[0]:
            p1, p2 = p2, p1

        delta_x = abs(p2[0] - p1[0])
        delta_y = abs(p2[1] - p1[1])
        crutch = delta_y > delta_x
        if crutch:
            p1, p2 = (p1[1], p1[0]), (p2[1], p2[0])
            if p1[0] > p2[0]:
                p1, p2 = p2, p1
            delta_x, delta_y = delta_y, delta_x
        error = 0.0
        delta_err = (delta_y+1)/(delta_x+1)
        y = p1[1]
        dir_y = -1 if p2[1] < p1[1] else 1
        for x in range(p1[0], p2[0]+1):
            if crutch:
                bext.goto(y, x)
            else:
                bext.goto(x, y)
            print('#', end='')
            error += delta_err
            if error >= 1.0:
                y += dir_y
                error -= 1.0

    def curve(self, *args):
        if len(args) < 2:
            raise ValueError("Not enough points")
        for p in args:
            self._check_outside_(p)
        for i in range(len(args)-1):
            self.line(args[i], args[i+1])

    def draw_text(self, top_left_point: (int, int), text: str):
        if not self._check_outside_(top_left_point):
            raise ValueError("point is outside of box")

        delta = (self.size[0]-2 - top_left_point[0], self.size[1]-top_left_point[1])
        if delta[0]*delta[1] < len(text):
            raise ValueError("No space for text")

        pos = (0, top_left_point[1])
        while pos[0] < len(text):
            bext.goto(top_left_point[0], pos[1])
            print(text[pos[0]:pos[0]+delta[0]])
            pos = (pos[0]+delta[0], pos[1]+1)


    def _test_draw_(self):
        p1 = (randint(0, self.size[0]-2), randint(0, self.size[1]-1))
        p2 = (randint(0, self.size[0]-2), randint(0, self.size[1]-1))
        self.line(p1, p2)
        self.draw_text((0, self.size[1]-1), f"{p1}:{p2}")


if __name__ == "__main__":
    r = Renderer("try to graphics")
    while key := bext.getKey():
        if key == 'r':
            r.resize()
        bext.hide()
        bext.clear()
        r._test_draw_()

    input()