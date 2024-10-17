import docx
from data_extractor.file_loaders.file_loader import FileLoader

class DOCXLoader(FileLoader):
    # def __init__(self, file_path):
    #     super().__init__(file_path)
    #     self.file = None
        
    # def validate_file(self):
    #     if not self.file_path.endswith('.docx'):
    #         raise ValueError("Invalid file type. Expected a DOCX file.")

    # def load_file(self):
    #     return docx.Document(self.file_path)
    def validate_file(self, file_path: str) -> bool:
        return file_path.lower().endswith('.docx')
    
    def load_file(self, file_path: str) -> docx.Document:
        if not self.validate_file(file_path):
            raise ValueError("Invalid DOCX file.")
        try:
            # Attempt to open the DOCX file
            return docx.Document(file_path)
        except Exception:
            # Catch any exception that occurs and raise a ValueError
            raise ValueError("Invalid DOCX file.")
    
    # def is_docx_valid(self, file_path: str) -> bool:
    #     try:
    #         docx.Document(file_path)
    #         return True
    #     except Exception:
    #         return False

    # def load_file(self, file_path: str) -> docx.Document:
    #     if not self.validate_file(file_path):
    #         raise ValueError("Invalid DOCX file.")
    #     if not self.is_docx_valid(file_path):
    #         raise ValueError("Corrupted DOCX file.")
    #     return docx.Document(file_path)
    
    
    # def close_file(self):
    #     if self.file:
    #         self.file.close()
