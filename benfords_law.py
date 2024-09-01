class BenfordsLaw:
    DIGITS = \
        [1, 2, 3, 4, 5, 6, 7, 8, 9]

    BENFORDS_LAW_PROBABILITY = \
        [0.3010, 0.1761, 0.1249, 0.0969, 0.0792, 0.0669, 0.0580, 0.0512, 0.0457]

    @staticmethod
    def count_first_digit(num_list: list) -> list:
        count = [0] * 9

        for num in num_list:
            try:
                digit = BenfordsLaw.__get_first_digit(num)
                count[digit - 1] += 1
            except Exception as e:
                print(e)

        return count

    @staticmethod
    def __get_first_digit(num):
        return int(str(num)[:1])
