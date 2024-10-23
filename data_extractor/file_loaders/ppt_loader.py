import pptx
from data_extractor.file_loaders.file_loader import FileLoader
from data_extractor.file_loaders.helper import Helper

class PPTLoader(FileLoader):
    def load_file(self, file_path: str) -> pptx.Presentation:
         return Helper(file_path, pptx.Presentation).load()

