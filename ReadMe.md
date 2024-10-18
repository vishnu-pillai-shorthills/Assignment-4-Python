# Assignment-4 Python

## Python Version
The python version **3.12.3**, and rest packages versions are mentioned in **requirements.txt** file.

## Overview
The `data_extractor` directory contains a collection of tools designed for extracting data from various file formats and for storing the resulting data efficiently.

## Installation
To begin, clone the repository with command file to install the packages used in the project.
```bash
https://github.com/vishnu-pillai-shorthills/Assignment-4-Python.git
```

## How to Use
After cloning the project, run the main.py file.
```bash
python main.py
```

## Loaders
The `data_extractor` directory includes the following loaders to facilitate data extraction from different file types:

- **PDFLoader**: Extracts data from PDF files.
- **DOCXLoader**: Extracts data from DOCX files.
- **PPTLoader**: Extracts data from PPTX files.

## Data Extraction
The `data_extractor` uses the specified loaders to gather data from the supported file formats, offering a consistent interface for accessing the extracted information.

## Storage Options
The `data_extractor` directory provides the following storage solutions for the extracted data:

- **FileStorage**: Saves the extracted data in a file.
- **SQLStorage**: Saves the extracted data in a SQL database.

## Functionality
The `data_extractor` offers the following features:

- Extracts data from PDF, DOCX, and PPTX files using the appropriate loaders.
- Saves the extracted data either in a file or in a SQL database using the provided storage options.
- Provides a unified interface for easy access to the extracted data.

## How to see the database
Run the command
```bash
sqlite3 <DATABASE_NAME>.db 
``` 
in the terminal and see the tables made using .tables and retrieve the content from the table using 
```bash
SELECT * FROM <TABLE_NAME>
```

## Purpose
The main goal of the `data_extractor` directory is to deliver a user-friendly and efficient method for extracting data from a variety of file formats and storing that data for subsequent analysis or processing.