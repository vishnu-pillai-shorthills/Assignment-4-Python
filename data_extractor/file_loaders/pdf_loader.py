import os
from PyPDF2 import PdfReader
from data_extractor.file_loaders.file_loader import FileLoader
from data_extractor.file_loaders.helper import Helper

class PDFLoader(FileLoader):
    def load_file(self, file_path: str) -> PdfReader:
        return Helper(file_path, PdfReader).load()

    