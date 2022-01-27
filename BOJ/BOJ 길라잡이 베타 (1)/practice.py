def deleteZero(lst):
    return [i for i in lst if i not in [0]]

print(deleteZero([1,0,0,0,2,3,1,2]))
