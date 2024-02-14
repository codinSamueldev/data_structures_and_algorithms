class LinkedList {
    constructor (data) {
        this.head = {
            data: data,
            next: null
        }
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
}


const MyLinkedList = new LinkedList(10)

MyLinkedList.prepend(5)

console.log(MyLinkedList)
