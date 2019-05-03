def balikPosisi(inputList):
    outputList =[]
    x = len(inputList)
    for i in range(1,x+1):
        outputList.append(inputList[-i])
    return outputList


list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
list2 = ['G', 'F', 'E', 'D', 'C', 'B', 'A']
list3 = ['Rakitic', 'Dembele', 'Coutinho', 'Suarez', 'Messi']

print(balikPosisi(list1))
print(balikPosisi(list2))
print(balikPosisi(list3))