def merge(arr1,arr2):
    i = 0
    j = 0
    newArray = []
    while(i<len(arr1) and j<len(arr2)):
        left = arr1[i]
        right = arr2[j]
        if(left<=right):
            newArray.append(left)
            i = i + 1
        else:
            newArray.append(right)
            j = j + 1
    for x in range(i,len(arr1)):
        newArray.append(arr1[x])
    for z in range(j,len(arr2)):
        newArray.append(arr2[z])
    return newArray

def mergeSort(array):
    if len(array)<=1:
        return array
    meio = len(array)//2
    arrayA = mergeSort(array[0:meio])
    arrayB = mergeSort(array[meio:])
    return merge(arrayA,arrayB)


def mergeReverse(arr1,arr2):
    i = 0
    j = 0
    newArray = []
    while(i<len(arr1) and j<len(arr2)):
        left = arr1[i]
        right = arr2[j]
        if(left>=right):
            newArray.append(left)
            i = i + 1
        else:
            newArray.append(right)
            j = j + 1
    for x in range(i,len(arr1)):
        newArray.append(arr1[x])
    for z in range(j,len(arr2)):
        newArray.append(arr2[z])
    return newArray

def mergeSortReverse(array):
    if len(array)<=1:
        return array
    meio = len(array)//2
    arrayA = mergeSortReverse(array[0:meio])
    arrayB = mergeSortReverse(array[meio:])
    return mergeReverse(arrayA,arrayB)

s = ""
c = 0
while(True):
	numero = int(input())
	dicionario = {}
	if numero==0:
		break
	for x in range(numero):
		nome = input()
		cor,tamanho = input().split(" ")
		try:
			dicionario[cor][tamanho].append(nome)
		except:
			try:
				dicionario[cor][tamanho] = [nome]
			except:
				dicionario[cor] = {tamanho:[nome]}


	for corX in mergeSort(list(dicionario.keys())):
		for tamanhoX in mergeSortReverse(list(dicionario[corX].keys())):
			nomes = mergeSort(dicionario[corX][tamanhoX])
			for nomeX in nomes:
				# print(corX + " " + tamanhoX + " " + nomeX)
				s+=corX + " " + tamanhoX + " " + nomeX+ "\n"
	s+="\n"
print(s.strip())
	




