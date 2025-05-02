class RomanConverter:
    def __init__(self):
        self.romans = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
            10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
            100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }

    def int_to_roman(self, num):
        result = ''
        for value in sorted(self.romans.keys(), reverse=True):
            while num >= value:
                result += self.romans[value]
                num -= value
        return result

    def roman_to_int(self, s):
        roman_dict = {v: k for k, v in self.romans.items()}
        i = 0
        num = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in roman_dict:
                num += roman_dict[s[i:i+2]]
                i += 2
            else:
                num += roman_dict[s[i]]
                i += 1
        return num
