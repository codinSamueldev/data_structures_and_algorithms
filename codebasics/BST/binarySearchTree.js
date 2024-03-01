class BinarySearchTree {

    constructor (data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }


    addChild (value) {
        if (value == this.data) {
            return;
        }

        if (value > this.data) {
            if (this.right) {
                this.right.addChild(value);
            } else {
                this.right = new BinarySearchTree(value);
            }
        } else {
            if (this.left) {
                this.left.addChild(value);
            } else {
                this.left = new BinarySearchTree(value);
            }
        }
    }


    searchNode (value) {
        if (value == this.data) {
            return true;
        }

        if (value > this.data) {
            if (this.right) {
                return this.right.searchNode(value);
            } else {
                return false;
            }
        } else {
            if (this.left) {
                return this.left.searchNode(value);
            } else {
                return false;
            }
        }
    }


    inOrderTraversal () {
        let treeSorted = [];

        if (this.left) {
            treeSorted = treeSorted.concat(this.left.inOrderTraversal());
        }

        treeSorted.push(this.data);

        if (this.right) {
            treeSorted = treeSorted.concat(this.right.inOrderTraversal());
        }

        return treeSorted;
    }

}


function buildTree (array) {
    console.log("Given array to convert into a tree ->", array);
    const root = new BinarySearchTree(array[0]);

    for (let i = 1; i < array.length; i++) {
        root.addChild(array[i]);
    }

    return root;
}


/* Example usage */
let randomArray = [];
for (let i = 0; i < 8; i++) {
    randomArray.push(Math.floor(Math.random() * 20 + 1));
}

const generalTree = buildTree(randomArray);
console.log("Tree sorted ->", generalTree.inOrderTraversal());

const elementToFound = 8
console.log(`Element ${8} was found in the tree? ->`, generalTree.searchNode(elementToFound));
