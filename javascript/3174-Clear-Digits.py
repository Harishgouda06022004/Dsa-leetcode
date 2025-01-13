class Solution:
    def clearDigits(self, s: str) -> str:
        i = 0
        while i < len(s):  # Iterate over the string
            if s[i].isdigit():  # If it's a digit
                if i > 0 and not s[i - 1].isdigit():  # If there's a non-digit to the left
                    s = s[:i - 1] + s[i + 1:]  # Remove both the digit and the non-digit to its left
                    i = 0  # Restart iteration since the string has changed
                else:
                    s = s[:i] + s[i + 1:]  # Remove the digit and keep the rest of the string
                    i = 0  # Restart iteration since the string has changed
            else:
                i += 1  # Move to the next character
        return s



