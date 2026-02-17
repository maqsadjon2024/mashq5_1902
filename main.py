#82
def gen_kub(n):
    for i in range(1,n+1):
        yield i**3

print(list(gen_kub(5)))

#83
def unique_text(text):
    return len(set(text)) == len(text)

print(unique_text("abcde"))

#84
def teskari_son(n):
    return int(str(n)[::-1])

print(teskari_son(12345))

#85
def armstrong(n):
    s = sum(int(d)**3 for d in str(n))
    return s == n

print(armstrong(153))

#86
def prefix(lst):
    pref = lst[0]
    for word in lst[1:]:
        while not word.startswith(pref):
            pref = pref[:-1]
    return pref

print(prefix(["flower","flow","flight"]))
