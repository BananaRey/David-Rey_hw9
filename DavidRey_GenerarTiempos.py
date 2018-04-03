import time
# se crea la funcion de fibonacci de forma recursiva
def fibonacci(N):
	#casos bases	
	if(N==0):
		return(0.0)
	elif(N==1):
		return(1.0)
	#Caso recursivo
	else:
		return(fibonacci(N-1)+fibonacci(N-2))
# se crea funcion del tiempo
def get_time(N):
	t0 = time.time()
	fibonacci(N)
	t1 = time.time()-t0
	return(t1)
# se imprimen los tiempos hasta fibonacci de 34
for i in range(35):
		print(get_time(i))
		










