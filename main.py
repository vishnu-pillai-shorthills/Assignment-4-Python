import os
from data_extractor.file_loaders.pdf_loader import PDFLoader
from data_extractor.file_loaders.docx_loader import DOCXLoader
from data_extractor.file_loaders.ppt_loader import PPTLoader
from data_extractor.info_extractor.docx_extractor import DOCXExtractor
from data_extractor.info_extractor.pdf_extractor import PDFExtractor
from data_extractor.info_extractor.pptx_extractor import PPTXExtractor
from data_extractor.storage.file_storage import FileStorage
from data_extractor.storage.sql_storage import SQLStorage

def main():
    """
    Main function for extracting data from a file.

    This function takes a file path as an argument, determines the file type (PDF, DOCX, or PPTX),
    uses the appropriate loader to validate and load the file, creates an instance of DataExtractor
    to extract content, and then saves the extracted data to a folder and a SQL database.

    """
    
    file_path=input("Enter file path: ")
    filename = os.path.basename(file_path)
    # print(filename)

    # Determine the file type and use the appropriate loader
    if file_path.endswith(".pdf"):
        # loader = PDFLoader(file_path)
        loader = PDFLoader()
        extractor = PDFExtractor(loader)
    elif file_path.endswith(".docx"):
        loader = DOCXLoader()
        extractor=DOCXExtractor(loader)
    elif file_path.endswith(".pptx"):
        loader = PPTLoader()
        extractor = PPTXExtractor(loader)
    else:
        raise ValueError("Unsupported file format. Use PDF, DOCX, or PPTX.")

    # Validate the file (ensures it's the correct type)
    # loader.validate_file()

    # Load the file using the appropriate loader
    # loader.load_file()

    # Create an instance of DataExtractor for extracting content
    # extractor = DataExtractor(loader)

    extractor.load(file_path)

    # Extract text from the file
    extracted_text = extractor.extract_text()

    # Extract images (if available)
    images = extractor.extract_images()

    # Extract URLs (if it's a PDF or DOCX)
    urls = extractor.extract_urls() 
    # urls = extractor.extract_urls() if file_path.endswith(('.pdf', '.docx')) else None
    print(urls)

    # Extract tables (for PDFs or DOCX only)
    tables = extractor.extract_tables() 

    # Close the file (if applicable)
    # if hasattr(loader, 'close_file'):
    #     loader.close_file()

    # Create a folder for storing the extracted data
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join("extracted_data", base_name)
    file_storage = FileStorage(output_dir)

    # Save the extracted text
    file_storage.store(extracted_text, os.path.basename(file_path), 'text')

    # Save the extracted images
    image_data=None

    if images:
        image_data=file_storage.store(images, os.path.basename(file_path), 'image')

    # Save the extracted URLs (if any)
    if urls:
        file_storage.store(urls, os.path.basename(file_path), 'url')

    # Save the extracted tables (if any)
    if tables:
        file_storage.store(tables, os.path.basename(file_path), 'table')

    print(f"Extracted data saved to: {output_dir}")
    
    # Create an instance of SQLStorage
    sql_storage = SQLStorage("assignment4.db")

    # Store the extracted text in the SQL database
    sql_storage.store("text", extracted_text, filename)

    # Store the extracted images in the SQL database

    if images:
        sql_storage.store("image", image_data, filename)

    # Store the extracted URLs in the SQL database
    if urls:
        sql_storage.store("url", urls, filename)

    # Store the extracted tables in the SQL database
    if tables:
        for table in tables:
            sql_storage.store("info_table", table, filename)

    print("Data stored in SQL database")
    sql_storage.close()
    # loader.close_file()

if __name__ == "__main__":
    main()
