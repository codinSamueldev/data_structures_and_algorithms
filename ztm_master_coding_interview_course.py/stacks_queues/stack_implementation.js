/* LIFO - Last In First out. */

class Node {
    /* A class representing nodes of a linked list. */
    constructor (data) {
        this.data = data;
        this.next = null;
    }
}


class Stack {
    /* A class representing a stack data structure. */
    constructor () {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    peek () {
        /* Retrieve which node is at top position. */
        try {
            return this.top.data;
        } catch (error) {
            throw new Error("Stack already empty...");
        }
    }


    push (data) {
        /* Add nodes at top position. */
        const NEW_NODE = new Node(data);

        if (this.top === null) {
            this.top = NEW_NODE;
            this.bottom = NEW_NODE;
        } else {
            NEW_NODE.next = this.top;
            this.bottom = this.top.next;
            this.top = NEW_NODE;
        }
        this.length++;
    }


    pop () {
        /* Remove last element inserted. */
        this.top = this.top.next;
        this.length--;
    }


    isEmpty () {
        /* Check if stack is empty or not. */
        if (this.length > 0) {
            return false;
        } else {
            return true;
        }
    }

}


/* Example usage. */
const stackWithNodes = new Stack();

// Add elements.
stackWithNodes.push(1);
stackWithNodes.push(2);
stackWithNodes.push(3);

// Remove elements.
stackWithNodes.pop();
stackWithNodes.pop();

// Print out element at top position, and check if stack is empty...
console.log(stackWithNodes.peek(), stackWithNodes.isEmpty());

