#author: Esteban Salpeter
#author's email: esteban.salpeter@yahoo.com.ar
def primes_between(min,max):
#init
	mx = round(max/2,0)+1
	mn = round(min/2,0)-1
	m=1
	listado=[]
	p=[]
  
	while (m<=(mx+1)*2/3):
		l=m
		while l<=((mx)*2)/3:
    #my super formula
			n=m*l*2+m+l
			if n>mx:
				break
			if (n<=mx) & (n>=mn):
				listado.append(n)
			l+=1
		m+=1
	listado.sort()
	tmp=listado[0]
  #my super faster algorithm (to be improved)
	for e in listado:
		if e-tmp>1:
			l=1
			while l<e-tmp:
				if (tmp+l)*2+1<max:
					p.append((tmp+l)*2+1)
				l+=1
		tmp=e
	return p


def is_prime(num):
    last = num%10
    if num in [1,2,3,5,7]:
        return True
    if last in [2,4,5,6,8,0]:
        return False
    p=primes_between(num-1,num+1)
    if num in p:
        return True
    return False
