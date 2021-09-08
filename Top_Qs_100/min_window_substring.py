
def solution(n):

    indexes = []
    all_possibilities = []
    N = abs(n)

    new_n = [int(x) for x in str(N)]
    for index, element in enumerate(new_n):
        if(element == 5):
            indexes.append(index)
    for element in indexes:
        temp = new_n.copy()
        temp.pop(element)
        temp = [str(x) for x in temp]
        temp = ''.join(temp)
        temp = int(temp)

    all_possibilities.append(temp)
    if n < 0:
        all_possibilities = [x * -1 for x in all_possibilities]


    return max(all_possibilities)

examples = [15958, -5859, -5000]

for N in examples:
     result = solution(N)
     print(result)