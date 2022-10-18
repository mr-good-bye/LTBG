from LTBGTextEngine import engine

renderer = engine.Renderer()

# TODO [IMPORTANT] Look at dearpygui !

if __name__ == "__main__":
    size = renderer.size
    renderer.curve((0, 0), (0, size[1]-1), (size[0]-2, size[1]-1), (size[0]-2, 0), (0, 0))
    x = int(size[0]*0.3)
    y = int(size[1]*0.3)
    renderer.draw_text((x, y), "[Nickname]:")
    renderer.draw_text((x, y+1), "[Password]:")
    renderer.go_to((x+len("[Nickname]:"), y))
    nick = renderer.input()
    renderer.go_to((x+len("[Password]:"), y+1))
    pwd = renderer.input()
    renderer.draw_text((5, size[1]-3), nick)
    renderer.draw_text((5, size[1]-2), pwd)
    input()
