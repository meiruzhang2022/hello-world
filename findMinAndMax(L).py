def findMinAndMax(L):
    if L!=[]:
        Min=L[0]
        Max=L[0]
    else:
        return (None,None)
    for i in L:
        if i<=Min:
            Min=i
        else:
            Min=Min
    for i in L:
        if i>=Max:
            Max=i
        else:
            Max=Max
    return (Min,Max)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')