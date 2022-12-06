from Trees import Cell


class Folder(Cell):
    all = {}

    def __init__(self, name: str, parent_folder: 'Folder' or str = None):
        if not name:
            raise ValueError("Folder cannot be without name")
        if type(parent_folder) is str:
            parent_folder = Folder.all[parent_folder]
        Cell.__init__(self, parent_folder, name)
        Folder.all[name] = self

    @staticmethod
    def from_dict(dictionary: dict):
        for k, v in dictionary.items():
            for folder in v:
                Folder(folder, k)


class File(Cell):
    def __init__(self, name: str, folder: Folder or str, data=None):
        if type(folder) is str:
            folder = Folder.all[folder]
        Cell.__init__(self, folder, name)
        self.data = name
        self.inner_data = data
        self.protected = data is not None

    def set_data(self, data):
        if not self.protected:
            self.inner_data = data
        else:
            return "Protected"

    def force_set_data(self, data):
        self.inner_data = data

    def get_data(self):
        return self.data


def main():
    root = Folder('root')
    filesys = {
        root: ("bin", "sys", "home", "suck", "some", "dick"),
        "bin": ("desktop", "encrypted", "dll"),
        "home": ("300 bucks",)
    }
    Folder.from_dict(filesys)
    File('LETS SUCK SOME DICKS.exe', '300 bucks')
    File('Piece of shit.dll', 'dll')
    File('testfile', root)

    for folder in Folder.all.values():
        print(f"Folder '{folder.data}':")
        if len([f.data for f in filter(lambda x: type(x) is Folder, folder.children)]) != 0:
            print('#    folders:', *[f.data for f in filter(lambda x: type(x) is Folder, folder.children)])
        if len([f.data for f in filter(lambda x: type(x) is File, folder.children)]) != 0:
            print('#    files:', *[f.data for f in filter(lambda x: type(x) is File, folder.children)])
        print()


if __name__ == "__main__":
    main()

