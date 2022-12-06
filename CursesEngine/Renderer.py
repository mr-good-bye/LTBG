import curses


class Renderer:
    def __init__(self):
        self.scr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(False)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)     # "Hacker" theme
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)      # "PowerShell" theme
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)    # "Hacker" highlight
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLUE)        # "PowerShell" highlight
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_RED)       # "Error"
        curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_GREEN)     # "Success"
        self.themes = {
            'std': curses.color_pair(0),
            'hacker': curses.color_pair(1),
            'powershell': curses.color_pair(2),
            'hacker_hl': curses.color_pair(3),
            'powershell_hl': curses.color_pair(4),
            'error': curses.color_pair(5),
            'success': curses.color_pair(6)
        }
        self.scr.keypad(True)

    def add_text(self, y: int, x: int, text: str, theme=None):
        self.scr.addstr(y, x, text, self.themes.get(theme, curses.color_pair(0)))

    def del_char(self, y_start: int, x_start: int, y_end: int = None, x_end: int = None):
        pass

    def __del__(self):
        curses.echo()
        curses.nocbreak()
        curses.curs_set(True)
        self.scr.keypad(False)
        del self.scr
        curses.endwin()
