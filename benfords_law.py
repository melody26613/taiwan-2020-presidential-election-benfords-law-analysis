import matplotlib.pyplot as plt
import numpy as np


class BenfordsLaw:
    def __init__(self):
        self.__DIGIT = \
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        self.__BENFORDS_LAW_PROBABILITY = \
            [0.3010, 0.1761, 0.1249, 0.0969, 0.0792, 0.0669, 0.0580, 0.0512, 0.0457]
    
    def count_first_digit_frequency(self, multiple_num_list):
        first_digit_frequency = [0] * 9
        
        for num_list in multiple_num_list:
            for num in num_list:
                first_digit = self.__get_first_digit(num)
                try:
                    first_digit_frequency[first_digit - 1] += 1
                except:
                    print("exception")
        
        print("first_digit_frequency: " + ', '.join(map(str, first_digit_frequency)))
        print("number of data: " + str(sum(first_digit_frequency)))
        return first_digit_frequency
    
    def __get_first_digit(self, num):
        return int(str(num)[:1])
        
    def output_data_to_graph(self, first_digit_frequency, output_path, filename, title):
        if (len(first_digit_frequency) != len(self.__DIGIT)):
            raise Exception("invalid first_digit_frequency")
        
        sum_of_frequency = sum(first_digit_frequency)
        first_digit_rate = [element / sum_of_frequency for element in first_digit_frequency]
        
        plt.clf()
        plt.title(title)
        plt.xlabel("First Digit")
        plt.ylabel("Probability")
        
        data_x = np.array(self.__DIGIT)
        data_y = np.array(first_digit_rate)
        plt.bar(data_x, data_y)
        
        line_benfords_law = plt.plot(
            self.__DIGIT, 
            self.__BENFORDS_LAW_PROBABILITY, "r", 
            label = "Benford's law"
        )
        
        plt.legend(handles = line_benfords_law)
        plt.xticks(self.__DIGIT)
        plt.savefig(output_path + "/" + filename + ".png")
