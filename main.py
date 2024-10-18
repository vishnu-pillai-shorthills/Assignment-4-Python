from data_extractor.info_extractor.helper import ExtractData
from data_extractor.storage.save_data import SaveData

def main():

    file_path = input("Enter the file path: ")

    # validate if the file path is given
    if not file_path:
        raise ValueError("FILE_PATH is not given.")
    
    # a dictionary object is returned
    helper = ExtractData(file_path)
    extracted_data = helper.extractData()

    # this function will save data to local and database
    saveData = SaveData(extracted_data, file_path)
    saveData.saveToLocal()
    saveData.saveToSQLDatabase()

if __name__ == "__main__":
    main()
