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
        if (this.head == null) {
            let addNode = data
            this.head.data = addNode
        }
        else {
            const newNode = {
                data: data,
                next: this.head
            }
            this.head = newNode
        }
    }


    append_nodes (data) {
        if (this.head == null) {
            this.prepend(data)
        }
        else {
            const newNode = {
                data: data,
                next: null
            }
            this.tail.next = newNode
            this.tail = newNode
        }
    }
}


const MyLinkedList = new LinkedList(10)

MyLinkedList.prepend(5)
MyLinkedList.append_nodes(15)

console.log(MyLinkedList)
