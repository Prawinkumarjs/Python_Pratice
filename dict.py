# count frequency

string = "aaabbbbcccccddddsss"
fre ={}

for i in string:
    if i in fre:
        fre[i] += 1
    else:
        fre[i] = 1
print(fre)
