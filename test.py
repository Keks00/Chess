test = {}
for i in range(1,10):
    test[i] = {}
    test[i][i] = True
    test[i][i+2] = False
print(test)