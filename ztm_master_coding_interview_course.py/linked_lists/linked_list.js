class Node {
    constructor (data) {
        this.data = data
        this.next = null
    }
}


class LinkedList {
    constructor (data) {
        this.head = {
            data: data,
            next: null
        }
        this.tail = this.head
    }


    prepend (data) {
        /* Add nodes to linked list head. */
        if (this.head === null) {
            let addNode = new Node(data)
            this.head = addNode
        }
        else {
            const newNode = new Node(data)
            newNode.next = this.head
            this.head = newNode
        }
    }


    appendNodes (data) {
        /* Insert data at linked list's tail. Time complexity O(1). */
        if (this.head === null) {
            this.prepend(data)
        }
        else {
            const newNode = new Node(data)
            this.tail.next = newNode
            this.tail = newNode
        }
    }


    insertNodeAt (index, data) {
        /* Insert new data at index given. Time complexity O(n). */

        if (index < 0) {
            throw new Error('Invalid index...')
        } else if (index === 0) {
            this.prepend(data)
        }

        let count = 0
        let iterator = this.head

        while (iterator !== null) {
            if (count === index - 1) {
                const newNode = new Node(data) // Create new node.
                newNode.next = iterator.next // Set the new node's next pointer to the next node of the current node.
                iterator.next = newNode // Set the current node's next pointer to the new node.
                return
            }
            count++
            iterator = iterator.next
        }
    }


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
const MyLinkedList = new LinkedList(10)

MyLinkedList.prepend(5)
MyLinkedList.prepend(115)
MyLinkedList.appendNodes(15)
MyLinkedList.insertNodeAt(2, "Holi")

console.log(MyLinkedList.printOutLinkedList())
