class queue{
    constructor(){
        this.arr = []
    }
    adding(element){
        this.arr.push(element)
    }
    removing(){
        this.arr.shift()
    }
    top(){ 
        return (this.arr[0])
    }
    isEmpty(){
        this.arr.length==0
    }
}
let Queue = new queue
Queue.adding(10)
Queue.adding(20)
Queue.removing()
Queue.adding(30)
console.log(Queue)
console.log(Queue.top())

 