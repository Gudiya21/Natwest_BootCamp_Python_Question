
var list = [10,14,2,11,6,8]
i=0
while(i<list.length){
    j=0
    while (j<list.length){
        if (list[i]<list[j]){
            temp=list[i]  
            list[i]=list[j]
            list[j]=temp
        }
        j++
    }
    i++
}
console.log(list)