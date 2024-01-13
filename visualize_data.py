# minumum python version is 3.6

from os import listdir
from os.path import isfile, join
from benfords_law import BenfordsLaw
import pandas as pd


RAW_DATA_FOLDER = "data"
OUTPUT_FOLDER = "output"

DATA_COLUMN = [
    'Villige_Total',
    'Villige',
    'Candidate1',
    'Candidate2',
    'Candidate3',
    'Valid',
    'Invalid',
    'Vote'
]
VERIFY_COLUMN = [
    'Candidate1',
    'Candidate2',
    'Candidate3',
    'Valid',
    'Vote'
]

GRAPH_TITLE = "Taiwan 2020 Presidential Election\n" + \
    "Statistics of All Villages Votes In Taiwan by using Benford's Law Analysis"


def remove_unused_data(file_path):
    raw_data = pd.read_csv(file_path, encoding="big5")
    raw_data = raw_data.drop(range(0, 5))  # remove row 0 ~ 5
    # remove column 8 ~ 13
    raw_data = raw_data.drop(columns=raw_data.columns[8: 13])
    raw_data.columns = DATA_COLUMN

    # only keep villige data, remove sum column 'Villige_Total'
    raw_data = raw_data[raw_data.Villige_Total.isnull()]
    raw_data = raw_data.drop(columns=raw_data.columns[0])

    raw_data.reset_index(drop=True, inplace=True)

    return raw_data


def show_data_sample_on_console(raw_data_file):
    file_path = RAW_DATA_FOLDER + "/" + raw_data_file
    data_sample = remove_unused_data(file_path)
    print("\ndata sample from \"" + raw_data_file + "\" :")
    print(data_sample)


def output_to_benfords_law_graph_for_specific_data(raw_data_files):
    benfords_law_tool = BenfordsLaw()

    for column in VERIFY_COLUMN:
        data = get_specific_data_from_all_files(column, raw_data_files)
        digit_frequency = benfords_law_tool.count_first_digit_frequency(data)
        benfords_law_tool.output_data_to_graph(
            digit_frequency, OUTPUT_FOLDER, column, GRAPH_TITLE)


def get_specific_data_from_all_files(column_name, raw_data_files):
    data_list = list()
    for raw_data_file in raw_data_files:
        file_path = RAW_DATA_FOLDER + "/" + raw_data_file
        data = remove_unused_data(file_path)
        data_list.append(data[column_name].to_list())

    return data_list


raw_data_files = [f for f in listdir(
    RAW_DATA_FOLDER) if isfile(join(RAW_DATA_FOLDER, f))]
print("raw_data_files:\n" + '\n'.join(raw_data_files))

show_data_sample_on_console(raw_data_files[0])
output_to_benfords_law_graph_for_specific_data(raw_data_files)
