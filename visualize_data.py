# python version is 3.6

from os import listdir
from os.path import isfile, join
from benfords_law import BenfordsLaw
import pandas as pd


DATA_COLUMN = [
    'Villige_Total', 
    'Villige', 
    'Candidate1_宋楚瑜', 
    'Candidate2_韓國瑜', 
    'Candidate3_蔡英文', 
    'Valid', 
    'Invalid', 
    'Vote'
]
VERIFY_COLUMN = [
    'Candidate1_宋楚瑜', 
    'Candidate2_韓國瑜', 
    'Candidate3_蔡英文',
    'Valid', 
    'Vote'
]
TITLE = "Taiwan 2020 Presidential Election\n" + \
        "Statistics of All Villages Votes In Taiwan by using Benford's Law Analysis"

OUTPUT_FOLDER = "output"
RAW_DATA_FOLDER = "data"

def remove_unused_data(file_path):
    raw_data = pd.read_csv(file_path, encoding = "big5")   
    raw_data = raw_data.drop(range(0, 5))  # remove row 0 ~ 5
    raw_data = raw_data.drop(columns = raw_data.columns[8: 13]) # remove column 8 ~ 13
    raw_data.columns = DATA_COLUMN
    
    raw_data = raw_data[raw_data.Villige_Total.isnull()] # only keep villige data, remove sum
    raw_data = raw_data.drop(columns = raw_data.columns[0])
    
    raw_data.reset_index(drop = True, inplace = True)

    return raw_data


raw_data_files = [f for f in listdir(RAW_DATA_FOLDER) if isfile(join(RAW_DATA_FOLDER, f))]
print("raw_data_files:\n" + '\n'.join(raw_data_files))

file_path = RAW_DATA_FOLDER + "/" + raw_data_files[0]
data_sample = remove_unused_data(file_path)
print("\ndata sample from \"" + raw_data_files[0] + "\" :")
print(data_sample)

data_list = list()
for raw_data_file in raw_data_files:
    file_path = RAW_DATA_FOLDER + "/" + raw_data_file
    data = remove_unused_data(file_path)
    data_list.append(data.Vote.to_list()) ########### change item here

benfords_law_tool = BenfordsLaw()
frequency = benfords_law_tool.count_first_digit_frequency(data_list)
benfords_law_tool.output_data_to_graph(frequency, OUTPUT_FOLDER, "Vote", TITLE)
