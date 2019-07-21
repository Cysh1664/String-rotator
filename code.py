w = input()
a = [w[i:] + w[:i] for i in range(len(w))]
print(a)
