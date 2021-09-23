def kthdigit(a,b,k):
    res = str(pow(a,b))
    length = len(res)-k
    return res[length]

inpp = input()

for i in range(len(inpp)):
    abk = inpp.split()
    a = int(abk[0])
    b = int(abk[1])
    k = int(abk[2])
print(kthdigit(a,b,k))
