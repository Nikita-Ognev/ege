print(len(set([n - int(bin(n)[3:],2) for n in range (100, 3001)])))

