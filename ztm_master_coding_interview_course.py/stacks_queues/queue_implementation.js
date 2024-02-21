class Node {
    /* A class representing a linked list node. */
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class Queue {
    /* A class representing a queue data structure. */
    constructor() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }

    peek() {
        /* See which node was the first queueing. Time complexity O(1). */
        return this.first ? this.first.data : null;
    }

    enqueue(data) {
        /* Add Nodes to the queue. Time complexity O(1). */
        const newNode = new Node(data);

        if (!this.first) {
            // If queue is empty, then update first and last value.
            this.first = newNode;
            this.last = newNode;
        } else {
            // Otherwise, current next last node will point to the new node and update last value.
            this.last.next = newNode;
            this.last = newNode;
        }

        this.length++;
    }

    dequeue() {
        /* Remove the first in node. Time complexity O(1). */
        try {
            this.first = this.first.next;
            if (!this.first) {
                this.last = null;
                return;
            }
        } catch (error) {
            throw new Error("Sorry, queue already empty ;c");
        }
        
        this.length--;
    }

    isEmpty() {
        if (this.length > 1) {
            return false;
        } else {
            return true;
        }
    }

    printOutQueue() {
        /* Print out the whole queue. */
        if (!this.first) {
            // If queue is empty, print according info and prevent rest of code be executed.
            console.log("Nothing to show, queue is empty...");
            return;
        }

        let iterator = this.first;

        while (iterator !== null) {
            console.log(iterator.data, "-->", "");

            iterator = iterator.next;
        }

        return "Done";
    }
}


/* Example usage. */
const queueInstance = new Queue(); // Queue instance.

// Add elements to queue.
queueInstance.enqueue(1);
queueInstance.enqueue(2);
queueInstance.enqueue(3);

// Remove first element inserted in the queue.
queueInstance.dequeue();
queueInstance.dequeue();
queueInstance.dequeue();

// Finally, print out the whole queue.
queueInstance.printOutQueue();

console.log(queueInstance.isEmpty());
