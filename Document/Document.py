import datetime as dt
import os


class Document:
    Path: str
    Name: str
    Extension: str
    FullContent: str
    ContentLines: list[str]
    is_loaded: bool
    loaded_at: dt.datetime

    def __init__(self, document_fullpath: str):
        self.Path = document_fullpath
        self.Name = os.path.basename(self.Path)
        self.Extension = os.path.splitext(self.Path)[1]

    def load_document(self) -> None:
        if self.Path is not None:
            with open(self.Path, 'r') as f:
                self.FullContent = f.readline()
                self.ContentLines = f.readlines()

        if self.FullContent is not None:
            self.is_loaded = True
            self.loaded_at = dt.datetime.now()


