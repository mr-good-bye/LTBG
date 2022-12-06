class Cell:
    cell_id = 0

    def __init__(self, parent: 'Cell' = None, data: any = None):
        self.data = data
        self.parent = parent
        self.children = []
        if parent:
            parent.children.append(self)
        self.id = Cell.cell_id
        Cell.cell_id += 1


def main():
    root = Cell()
    for i in range(20):
        Cell(root, f"Cell {i}")
    for idx, val in enumerate(root.children):
        for i in range(idx):
            Cell(val, f"Child {idx}.{i}")

    for i in root.children:
        print(f"{i.data} :")
        print(*[ch.data for ch in i.children])

if __name__ == "__main__":
    main()
