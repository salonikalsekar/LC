class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        commented = False

        res = []

        for line in source:

            if not commented:
                temp = []
            i = 0
            while i < len(line):

                if line[i:i + 2] == "/*" and not commented:
                    commented = True
                    i += 1

                elif line[i:i + 2] == "*/" and commented:
                    commented = False
                    print(line[i])
                    i += 1

                elif line[i:i + 2] == "//" and not commented:
                    break

                elif not commented:
                    print(line[i])
                    temp.append(line[i])
                i += 1

            if temp and not commented:
                res.append("".join(temp))

        return res

