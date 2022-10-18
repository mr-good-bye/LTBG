import pygame as pg
import sys
import helpers


RESOLUTION = (800, 600)
FONT = "engine_res/seguisym.ttf"  # НЕ Моноширинный шрифт (по хорошему найти моноширинный с поддержкой ext ASCII)
FONT_COLOR = (255, 255, 255)
FONT_SIZE = 19
BG_COLOR = (0, 0, 0)


pg.font.init()
pg_font = pg.font.Font(FONT, FONT_SIZE)
# Adapt symbol_size:
test = pg_font.render(helpers.FRAME_X_BOLD, True, FONT_COLOR)
SYMBOL_SIZE = test.get_size()


class Screen:
    elements = []

    def __init__(self, surface: pg.Surface, name: str):
        self.surf = surface
        self.name = name
        self.name_size = len(name)
        self.size = surface.get_size()
        self.size = (self.size[0]//SYMBOL_SIZE[0], self.size[1]//SYMBOL_SIZE[1])
        self.matrix = [u" "*(self.size[0]) for _ in range(self.size[1])]
        Screen.elements.append(self)

    def __del__(self):
        Screen.elements.remove(self)

    def draw(self):
        res = []
        print(len(self.matrix))
        for y in range(self.size[1]):
            if y == 0:
                res.append(helpers.FRAME_UPPERLEFT_BOLD +
                           f"{helpers.FRAME_T_RIGHT_BOLD}{self.name}{helpers.FRAME_T_LEFT_BOLD}".center(
                               self.size[0]-2, helpers.FRAME_UPPER_BOLD) +
                           helpers.FRAME_UPPERRIGHT_BOLD)
            elif y == self.size[1]-1:
                res.append(helpers.FRAME_LOWERLEFT_BOLD + helpers.FRAME_UPPER_BOLD*(self.size[0]-2) +
                           helpers.FRAME_LOWERRIGHT_BOLD)
            else:
                print(y)
                res.append(helpers.FRAME_SIDE_BOLD + self.matrix[y][1:-1] + helpers.FRAME_SIDE_BOLD)
        y = 0
        for row in res:
            x = 0
            for s in row:
                self.surf.blit(pg_font.render(s, True, FONT_COLOR), (x, y))
                x += SYMBOL_SIZE[0]
            y += SYMBOL_SIZE[1]




def main():
    sc = pg.display.set_mode(RESOLUTION)

    screen = Screen(sc, "test run")
    screen.draw()

    pg.display.update()
    while 'LOST exists':
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
