let s = "The brown for jumps over the lazy dog"
let a = s.lower()
let string = ""
var s1=a.split()
string=string+s1[0]
for(i = 0,i in range(len(s1))){
    m= s1[i].capitalize()
    string=string+m
}
console.log(string)