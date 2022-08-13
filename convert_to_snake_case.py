from sys import stdin
from json import loads, dumps

l = [line[:-1] for line in stdin]
s = "".join(l)
d = loads(s)


def snake_casify(k):
    s = []
    for c in k:
        if c.upper() == c:
            s.append(f"_{c.lower()}")
        else:
            s.append(c)
    return "".join(s)

def dfs(d):
    if type(d) == list:
        return [dfs(k) for k in d]
    elif type(d) == dict:
        return {snake_casify(k):dfs(v) for k, v in d.items()}
    return d


print(dumps(dfs(d)))
