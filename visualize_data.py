# minumum python version is 3.6

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import re

from os import listdir
from os.path import isfile, join
from pandas import DataFrame

from benfords_law import BenfordsLaw

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


def print_raw_data(file: str):
    data_sample = get_filtered_data(file)
    print("\ndata from \"" + file + "\" :")
    print(data_sample)


def validate_by_benfords_law(files: list):
    for column in VERIFY_COLUMN:
        print("processing '" + column + "'")

        data_list = extract_column_data_from_files(column, files)

        first_digit_count = [0] * 9

        for data in data_list:
            freq = BenfordsLaw.count_first_digit(data)
            first_digit_count = [x + y for x,
                                 y in zip(first_digit_count, freq)]

        print("first_digit_count: " + ', '.join(map(str, first_digit_count)))
        print("number of data: " + str(sum(first_digit_count)))

        output_data_to_graph(
            first_digit_count=first_digit_count,
            output_folder=OUTPUT_FOLDER,
            data_name=column,
            title=GRAPH_TITLE
        )


def extract_column_data_from_files(column: str, files) -> list:
    data_list = list()
    for file in files:
        data = get_filtered_data(file)
        data_list.append(data[column].to_list())

    return data_list


def get_filtered_data(file: str) -> DataFrame:
    raw_data = pd.read_csv(file, encoding="big5")

    # remove row 0 ~ 5
    raw_data = raw_data.drop(range(0, 5))

    # remove column 8 ~ 13
    raw_data = raw_data.drop(columns=raw_data.columns[8: 13])

    raw_data.columns = DATA_COLUMN

    # only keep villige data, remove sum column 'Villige_Total'
    raw_data = raw_data[raw_data.Villige_Total.isnull()]
    raw_data = raw_data.drop(columns=raw_data.columns[0])

    raw_data.reset_index(drop=True, inplace=True)

    return raw_data


def output_data_to_graph(
    first_digit_count: list,
    output_folder: str,
    data_name: str,
    title: str
):
    if (len(first_digit_count) != len(BenfordsLaw.DIGITS)):
        raise Exception("invalid first_digit_count")

    total = sum(first_digit_count)
    probability = [
        count / total for count in first_digit_count]

    plt.clf()
    plt.title(title)
    plt.xlabel("First Digit")
    plt.ylabel("Probability")

    data_x = np.array(BenfordsLaw.DIGITS)
    data_y = np.array(probability)
    plt.bar(data_x, data_y)

    plt.plot(
        BenfordsLaw.DIGITS,
        BenfordsLaw.BENFORDS_LAW_PROBABILITY, "r"
    )

    legend = ["Benford's law", remove_special(data_name)]
    plt.legend(legend)

    plt.xticks(BenfordsLaw.DIGITS)
    current_axes = plt.gca()
    current_axes.set_ylim([0, BenfordsLaw.BENFORDS_LAW_PROBABILITY[0] + 0.1])

    output = os.path.join(output_folder, data_name + ".png")
    plt.savefig(output)


def remove_special(text):
    text = re.sub("[^a-zA-Z0-9]+", "", text)
    return text


raw_data_files = [os.path.join(RAW_DATA_FOLDER, f) for f in listdir(
    RAW_DATA_FOLDER) if isfile(join(RAW_DATA_FOLDER, f))]
print("raw_data_files:\n" + '\n'.join(raw_data_files))

print_raw_data(file=raw_data_files[0])
validate_by_benfords_law(files=raw_data_files)

print("done")
