def fronter(name,i):
    if name[i] == 'Gudia':
        return name[:i]
    else:
        return fronter(name,i-1) 
name = ['Geeta','Babita','neeta','reeta','chunni','Gudia','munni','champa','rampa','chameli']
n=len(name)
print(fronter(name,n-1))
