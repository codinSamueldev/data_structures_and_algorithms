class Node {
    constructor (data) {
        this.data = data
        this.previous = null
        this.next = null
    }
}


class LinkedList {
    constructor () {
        this.head = null
        this.tail = this.head
        this.length = 0
    }


    prepend (data) {
        /* Add nodes to linked list head. */

        const ADD_NODE = new Node(data)

        if (this.head === null) {
            this.head = ADD_NODE
            this.tail = ADD_NODE
            this.length++
        }
        else {
            ADD_NODE.next = this.head
            this.head.previous = ADD_NODE
            this.head = ADD_NODE
            this.length++
        }
    }


    appendNodes (data) {
        /* Insert data at linked list's tail. Time complexity O(1). */

         const NEW_NODE = new Node(data)
        if (this.head === null) {
            this.prepend(data)
        }
        else {
            this.tail.next = NEW_NODE
            NEW_NODE.previous = this.tail
            this.tail = NEW_NODE
            this.length++
        }
    }


    insertNodeAt (index, data) {
        /* Insert new data at index given. Time complexity O(n). */

        const ADD_NODE = new Node(data) // Create new node.

        if (index < 0) {
            throw new Error('Invalid index...')
        } else if (index === 0) {
            this.prepend(data)
        }

        let count = 0
        let iterator = this.head

        while (iterator !== null) {
            if (count === index) {
                ADD_NODE.next = iterator // Set the new node point to current node.
                ADD_NODE.previous = iterator.previous // Set the current node's next pointer to the new node.
                iterator.previous.next = ADD_NODE
                this.length++
            return
            }
            count++
            iterator = iterator.next
        }
        throw new Error('Linked list out of bounds...')
    }


    removeNode (index) {
        /* Remove node at index given. Time complexity O(n) if the index is greater than zero, if it is equals to zero time complexity would be O(1). */

        if (index < 0) {
            throw new Error('Invalid index...')
        } else if (index === 0) {
            // If the index is 0, remove the head node and update the head reference.
            this.head = this.head.next
            return
        }

        let count = 0
        let iterator = this.head

        while (iterator !== null) {
            if (count === index - 1) {
                // If you want to checkout which item will be removed, uncomment the following line:
                //console.log("Node to remove ->", iterator.next.data);
                // Next node is the target node, remove it by updating the next reference of the previous node.
                iterator.next = iterator.next.next
                this.length--
            return
            }
            count++
            iterator = iterator.next
        }
        throw new Error('Linked list out of bounds...')
    }

    /*
    reverse () {
        // TODO...
        let counter = 0
        let auxiliary

        while (counter < this.length) {
            let currentNode = this.head
            let currentLastNode = this.tail
            currentLastNode = this.head
            this.head = this.tail
            currentNode = currentNode.next


            counter++
        }
    }
    */

    printOutLinkedList () {
        let iterator = this.head
        const llArray = [];

        while (iterator !== null) {
            llArray.push(iterator.data)
            iterator = iterator.next
        }
        return llArray
    }
}


// Example usage.
const MyLinkedList = new LinkedList()

MyLinkedList.prepend(5)
MyLinkedList.prepend(115)
MyLinkedList.prepend(1)
MyLinkedList.appendNodes(15)
MyLinkedList.appendNodes("Last")
MyLinkedList.insertNodeAt(2, "I am here")
MyLinkedList.removeNode(4)
// MyLinkedList.reverse()

console.log(MyLinkedList.printOutLinkedList())
