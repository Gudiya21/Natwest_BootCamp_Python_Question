class Stack{
    constructor(){
        this.arr = []
    }
    adding(element){
        this.arr.push(element)
    }
    removing(){
        this.arr.pop()
    }
    top(){
        !this.isEmpty ?console.log(this.arr.shift()):console.log("stack is empty") 
    }
    isEmpty(){
        this.arr.length == 0?true:false
    }
 
}
let stack = new Stack
stack.adding(10) 
stack.removing()
stack.adding(20)
console.log(stack) 





