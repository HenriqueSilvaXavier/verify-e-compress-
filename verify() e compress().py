def verify(n1, n2):
	if len(n1)>len(n2):
		e1=n2
		e2=n1
	elif len(n2)>len(n1):
		e1=n1
		e2=n2
	elif len(n1)==len(n2):
		e1=n1
		e2=n2
	global índices
	índices=[]
	for n in range(0, len(e1)):
		if e1[n]!=e2[n]:
			índices.append(n)
	return índices

def compress(índices):
	r=False
	lista=[]
	índices.append("")
	C=índices[:]
	del C[-1]
	for k in C:
		i=índices.index(k)
		if len(índices)-1>i:
			if k==índices[i] and k+1==índices[i+1] and r==False:
				lista.append("[{}:".format(k))
				r=True
			elif k==índices[i] and k+1!=índices[i+1] and r==True or k==índices[i] and len(índices)-1==i and r==True:
				lista.append("{}]".format(k))
				r=False
				c="".join(lista[len(lista)-2:len(lista)])
				del lista[-1]
				del lista[-1]
				lista.append(c)
			elif k-1!=índices[i-1] and k+1!=índices[i+1] and r==False:
				lista.append(k)
	return lista


	