class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letterArray = []
        numberArray = []

        for log in logs:
            splitLog = log.split(" ")
            if splitLog[1].isalpha():
                letterArray.append(log)
            else:
                numberArray.append(log)

        alphaArr = sorted(letterArray, key=lambda x: (x.split()[1:], x.split()[0]))
        return alphaArr + numberArray