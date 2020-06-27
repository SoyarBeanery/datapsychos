import re

def check(item, q):
    #pattern = "\b("+q+")\b"
    #print(pattern)
    res = re.match(rf"\b({q})\b", item)
    #print(res)
    return res != None

T = input()

for case in range(int(T)):
    print(f"Case {case+1}:")
    items_n, queries_n = input().split(' ')
    items_n, queries_n = int(items_n), int(queries_n)
    items = []
    for _ in range(items_n):
        item = input()
        items.append(item)

    #print(items)

    for _ in range(queries_n):
        q = input()
        #print(q)
        count = 0
        for item in items:
            count += 1 if check(item, q) else 0
        print(count)
