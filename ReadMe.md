# Assignment-4 Python

## Overview
The `data_extractor` directory contains a collection of tools designed for extracting data from various file formats and for storing the resulting data efficiently.

## How to Use
To get started, clone the repository and set the `file_path` variable to the path of the main file. Then, execute the `main.py` script.

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

## Purpose
The main goal of the `data_extractor` directory is to deliver a user-friendly and efficient method for extracting data from a variety of file formats and storing that data for subsequent analysis or processing.