#https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []

        for log in logs:
            if log.split()[1].isdigit() == True:
                digits.append(log)
            else:
                letters.append(log)
        letters = sorted(letters, key=lambda x: (x.split()[1:], x.split()[0]))
        return (letters + digits)
