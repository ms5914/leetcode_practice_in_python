class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [ch.lower() for ch in list(filter(lambda ch: ch.isalnum(), s))]
        return filtered_chars == filtered_chars[::-1]
        