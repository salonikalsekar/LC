def partition(self, n, s1, s2):
    def check(arr, index):
        if index == l:
            res.append(arr)
            return

        for i in range(index, l):
            if s[index:i + 1] == s[index:i + 1][::-1]:
                check(arr + [s[index:i + 1]], i + 1)

    l = len(s)
    res = []
    check([], 0)
    return res
print(partition(2, 'motor', 'rotor'))