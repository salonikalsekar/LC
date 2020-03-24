class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLog = list()
        numericLog = list()

        for log in logs:
            if log.split()[1].isdigit():
                numericLog.append(log)
            else:
                letterLog.append(log)

        return sorted(letterLog, key=lambda x: (x.split()[1:], x.split()[0])) + numericLog