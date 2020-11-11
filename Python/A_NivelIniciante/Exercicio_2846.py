def fib(n,search):
	sequencia = [1,1,2,3]
	anteriorAnterior = 2
	anterior = 3
	fibonot = []
	for x in range(n-4):
		novo = anteriorAnterior + anterior
		anteriorAnterior = anterior
		anterior = novo
		for z in range(anteriorAnterior+1,anterior):
			fibonot.append(z)
			if(len(fibonot)==search):
				break
		sequencia.append(novo)
	return fibonot[search-1]


n = int(input())
if(n<=10):
	fibonat = fib(10,n)
else:
	fibonat = fib(n,n)
print(fibonat)


