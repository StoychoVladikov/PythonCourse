def solve(s):
    k = s.split(" ")
    a = (i.capitalize() for i in k)
    return " ".join(a)

