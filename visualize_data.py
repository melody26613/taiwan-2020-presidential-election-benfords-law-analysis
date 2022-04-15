# python version is 3.6

from os import listdir
from os.path import isfile, join

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_PICTURE = "output/result"

def get_first_digit(num):
    return int(str(num)[:1])

def count_first_digit_frequency(num_list):
    for num in num_list:
        first_digit = get_first_digit(num)
        try:
            first_digit_frequency[first_digit - 1] += 1
        except:
            print("exception")

def print_list(num_list):
    print(', '.join(num_list))

def remove_unused_data(file_path):
    raw_data = pd.read_csv(file_path, encoding = "big5")
    raw_data = raw_data.drop(range(0, 5))
    raw_data = raw_data.drop(columns = raw_data.columns[8: 13])
    raw_data.columns = ['Villige_Total', 'Villige', 'Candidate1', 'Candidate2', 'Candidate3', 'Valid', 'Invalid', 'Vote']
    raw_data = raw_data[raw_data.Villige_Total.isnull()]
    raw_data = raw_data.drop(columns = raw_data.columns[0])
    raw_data.reset_index(drop = True, inplace = True)
    return raw_data

raw_data_path = "data"
raw_data_files = [f for f in listdir(raw_data_path) if isfile(join(raw_data_path, f))]

print("raw_data_files:" + '\n'.join(raw_data_files))

first_digit_frequency = [0] * 9

file_path = raw_data_path + "/" + raw_data_files[0]
data_sample = remove_unused_data(file_path)
print("\ndata sample from \"" + raw_data_files[0] + "\" :")
print(data_sample)


for raw_data_file in raw_data_files:
    file_path = raw_data_path + "/" + raw_data_file
    data = remove_unused_data(file_path)
    count_first_digit_frequency(data.Vote.to_list()) ########### change item here

print("\nfrequency of first digit of Vote is: ")
print(first_digit_frequency)


digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
BENFORDS_LAW_PROBABILITY = [0.3010, 0.1761, 0.1249, 0.0969, 0.0792, 0.0669, 0.0580, 0.0512, 0.0457]

sum_of_frequency = sum(first_digit_frequency)
first_digit_rate = [element / sum_of_frequency for element in first_digit_frequency]

plt.title("Taiwan 2020 Presidential Election\nStatistics of All Villages Votes In Taiwan by using Benford's Law Analysis")
plt.xlabel("First Digit")
plt.ylabel("Probability")

line_benfords_law = plt.plot(digit, BENFORDS_LAW_PROBABILITY, "r", label = "Benford's law")

vote_x = np.array(digit)
vote_y = np.array(first_digit_rate)
plt.bar(vote_x, vote_y)

plt.legend(handles = line_benfords_law)
plt.xticks(digit)
plt.savefig(OUTPUT_PICTURE + ".png")

