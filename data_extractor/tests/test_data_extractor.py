import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from data_extractor.data_extractor import DataExtractor
from data_extractor.file_loaders.pdf_loader import PDFLoader

class TestDataExtractor(unittest.TestCase):

    def test_extract_data(self):
        """
        Tests the DataExtractor's extract_data method with a valid PDF file.

        Asserts that the DataExtractor's extract_data method returns a list of dictionaries
        containing the extracted data for a valid PDF file.

        Parameters
        ----------
        self : TestDataExtractor
            The unit test class.

        Returns
        -------
        None
        """
        loader = PDFLoader()
        extractor = DataExtractor(loader)
        data = extractor.extract_data("/home/shtlp_0068/Documents/Assignment_4_python-main/files/sample.pdf")
        self.assertIsInstance(data, list)

    def test_extract_data_empty_file(self):
        """
        Tests the DataExtractor's extract_data method with an empty PDF file.

        Asserts that the DataExtractor's extract_data method returns an empty list
        for an empty PDF file.

        Parameters
        ----------
        self : TestDataExtractor
            The unit test class.

        Returns
        -------
        None
        """
        loader = PDFLoader()
        extractor = DataExtractor(loader)
        data = extractor.extract_data("/home/shtlp_0068/Documents/Assignment_4_python-main/files/empty.pdf")
        self.assertEqual(data, [])

    def test_extract_data_invalid_file(self):
        """
        Tests the DataExtractor's extract_data method with a non-existent PDF file.

        Asserts that the DataExtractor's extract_data method raises a FileNotFoundError
        for a non-existent PDF file.

        Parameters
        ----------
        self : TestDataExtractor
            The unit test class.

        Returns
        -------
        None
        """
        loader = PDFLoader()
        extractor = DataExtractor(loader)
        with self.assertRaises(FileNotFoundError):
            extractor.extract_data("/home/shtlp_0068/Documents/Assignment_4_python-main/files/non_existent_file.pdf")

if __name__ == '__main__':
    unittest.main()