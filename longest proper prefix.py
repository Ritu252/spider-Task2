T = int(input())
p = []
for i in range(T):
    s = input()
    l = []
    for i in range(len(s)):
        l.append(s[i])
    while len(l)>1:
        if l[0]=="<":
            if l.count("<")==l.count(">"):
                print(len(l))
                break
            else:
                l.pop()
        else:
            print(0)
            break
    
