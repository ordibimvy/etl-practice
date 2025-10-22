import glob # automatically find files by pattern
import pandas as pd # data handler libaray
import xml.etree.ElementTree as ET # to parse xml
from datetime import datetime

log_file = 'log_file.txt' # where we would log data
target_file = 'transformed_data.csv' # our target file for the transformed data

# DATA EXTRACTION PROCESS 

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe 

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe 

def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns = ['car_model', 'year_of_manufacture', 'price', 'fuel'])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for car in root:
        car_model = car.find('car_model').text
        year_of_manufacture = int(car.find('year_of_manufacture').text)
        price = float(car.find('price').text)
        fuel = car.find('fuel').text
        dataframe = pd.concat([dataframe, pd.DataFrame([{'car_model': car_model, 'year_of_manufacture':year_of_manufacture, 'price': price, 'fuel':fuel}])], ignore_index=True)
    return dataframe

# test my extraction
#if __name__ == "__main__":
#   print(extract_from_xml("used_car_prices1.xml").head())

# MASTER EXTRACT : CREATING ONE HUGE DF
def extract():
    # empty df to hold the extracted data
    extracted_data = pd.DataFrame(columns = ['car_model', 'year_of_manufacture', 'price',  'fuel'])

    #process all csv files , except the target fiiel 
    for csvfile in glob.glob('*.csv'):
        if csvfile != target_file: # check if the file is not a target file 
            extracted_data = pd.concat([extracted_data, extract_from_csv(csvfile)], ignore_index=True)

    #process all json files 
    for jsonfile in glob.glob('*.json'):
        extracted_data = pd.concat([extracted_data, extract_from_json(jsonfile)], ignore_index=True)

    #process all xml files 
    for xmlfile in glob.glob('*.xml'):
        extracted_data = pd.concat([extracted_data, extract_from_xml(xmlfile)], ignore_index=True)

    return extracted_data
    
# test my extract 
#if __name__ == "__main__":
   # extracted_data = extract()
    # print(extracted_data.head())

# TRANSFORMATION OF DATA (ROUND PRICE TO TWO DECIMAL PLACE)

def transform(data):
    data['price'] = pd.to_numeric(data['price'], errors='coerce') # converts non numeric values and passes a NaN value
    data['price'] = data['price'].round(2) # round of price to two decimal place
 
    return data

# Test my Transformation
#if __name__ == "__main__":
    #extracted_data = extract()
    #transformed_data = transform(extracted_data)
    #print(transformed_data.head())

# LOAD DATA PROCESSING
def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file, index=False)

# Logging File
def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 










