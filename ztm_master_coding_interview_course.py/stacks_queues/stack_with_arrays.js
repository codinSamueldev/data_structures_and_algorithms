class Stack {
    constructor () {
        this.data = [];
    }


    peek () {
        if (this.data.length > 0) {
            return this.data[this.data.length - 1];
        } else {
            throw new Error("Stack is empty :d");
        }
        
    }    


    pushElements (data) {
        this.data.push(data);
    }


    pop () {
        this.data.pop()
    }

}


/* Example usage. */
const stackWithArrays = new Stack();

stackWithArrays.pushElements(1);
stackWithArrays.pushElements(2);
stackWithArrays.pushElements(3);

stackWithArrays.pop();
stackWithArrays.pop();
stackWithArrays.pop();

console.log(stackWithArrays.peek());

