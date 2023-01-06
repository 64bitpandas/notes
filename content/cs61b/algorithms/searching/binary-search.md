# Binary Search

Binary search is a way of finding a specific node in a tree. It only works on [binary trees](../../abstract-data-types/binary-trees/) due to its helpful sorted property. It simply traverses the tree, moving left if the current node is too large or right if it is too small.

Binary search runs in $\Theta(\log(n))$ time for bushy trees, which is also the number of layers in a tree.

## The Algorithm

```java
public BST find(BST T, Key sk) {
    if (T == null) {
        return null;
    }
    if (sk.equals(T.key)) {
        return T;
    } else if (sk < T.key) {
        return find(T.left, sk);
    } else {
        return find(T.right, sk);
    }
}
```
