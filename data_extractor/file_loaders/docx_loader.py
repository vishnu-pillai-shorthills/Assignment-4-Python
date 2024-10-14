import docx
from data_extractor.file_loaders.file_loader import FileLoader

class DOCXLoader(FileLoader):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.file = None
        
    def validate_file(self):
        if not self.file_path.endswith('.docx'):
            raise ValueError("Invalid file type. Expected a DOCX file.")

    def load_file(self):
        return docx.Document(self.file_path)
    
    def close_file(self):
        if self.file:
            self.file.close()
