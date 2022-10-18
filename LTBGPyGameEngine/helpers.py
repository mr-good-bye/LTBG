# Graphics for frames
FRAME_UPPER = u"─"
FRAME_UPPER_BOLD = u"━"
FRAME_SIDE = u"│"
FRAME_SIDE_BOLD = u"┃"
FRAME_UPPERLEFT = u"┌"
FRAME_UPPERRIGHT = u"┐"
FRAME_LOWERLEFT = u"└"
FRAME_LOWERRIGHT = u"┘"
FRAME_UPPERLEFT_BOLD = u"┏"
FRAME_UPPERRIGHT_BOLD = u"┓"
FRAME_LOWERLEFT_BOLD = u"┗"
FRAME_LOWERRIGHT_BOLD = u"┛"
FRAME_T_UPPER = u"┬"
FRAME_T_LEFT = u"├"
FRAME_T_RIGHT = u"┤"
FRAME_T_LOWER = u"┴"
FRAME_T_UPPER_BOLD = u"┳"
FRAME_T_LEFT_BOLD = u"┣"
FRAME_T_RIGHT_BOLD = u"┫"
FRAME_T_LOWER_BOLD = u"┻"
FRAME_X = u"┼"
FRAME_X_BOLD = u"╋"


def get_frame(left=None, right=None, up=None, down=None):
    """
    :param left: light/bold/None
    :param right: light/bold/None
    :param up: light/bold/None
    :param down: light/bold/None
    :return: symbol
    Choose which sides are which frames and get a symbol you need
    """
    # TODO create get_frame (maybe unicode maths?)
    raise NotImplementedError()
