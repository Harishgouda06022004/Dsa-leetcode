class Solution:
    def greatestLetter(self, s: str) -> str:
        lower_case=set(char for char in s if char.islower())
        upper_case=set(char for char in s if char.isupper())
        greatest_char=""
        for char in upper_case:
            if char.lower() in lower_case:
                if char>greatest_char:
                    greatest_char=char
        return greatest_char