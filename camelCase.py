s = "The brown for jumps over the lazy dog"
a = s.lower()
string = ""
s1=a.split()
string=string+s1[0]
for i in range(len(s1)):
    m= s1[i].capitalize()
    string=string+m
print(string) 