def merge(arr1,arr2):
	i = 0
	j = 0
	newArray = []
	while(i<len(arr1) and j<len(arr2)):
		left = arr1[i]
		right = arr2[j]
		if(left<=right):
			newArray.append(left)
			i+=1
		else:
			newArray.append(right)
			j+=1

	for x in range(i,len(arr1)):
		newArray.append(arr1[x])

	for z in range(j,len(arr2)):
		newArray.append(arr2[z])
	return newArray


def mergeSort(array):
	if(len(array)<=1):
		return array
	meio = len(array)//2
	arrayA = mergeSort(array[:meio])
	arrayB = mergeSort(array[meio:])
	return merge(arrayA, arrayB)

n = int(input())
frequencia = {}
for x in range(n):
	key = int(input())
	if key in frequencia:
		frequencia[key]+=1
	else:
		frequencia[key] = 1
numeros = mergeSort(list(frequencia.keys()))
for x in range(len(numeros)):
	print("%d aparece %d vez(es)" %(numeros[x],frequencia[numeros[x]]))