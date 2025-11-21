class Solution(object):
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        prev_value = 0

        for char in s[::-1]:
            curr_value = roman_map[char]
            if curr_value < prev_value:
                result -= curr_value
            else:
                result += curr_value
            #传递数字
            prev_value = curr_value

        return result
