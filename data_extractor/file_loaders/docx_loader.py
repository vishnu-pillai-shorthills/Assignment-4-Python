import docx
from data_extractor.file_loaders.file_loader import FileLoader
from data_extractor.file_loaders.helper import Helper

class DOCXLoader(FileLoader):
    def load_file(self, file_path: str) -> docx.Document:
        return Helper(file_path, docx.Document).load()