
> [!info] Content Note
>
> This page assumes prior knowledge of linked lists from CS61A or equivalent. I'll assume you have already worked with basic singly linked lists before.


The linked list is an extremely common recursive data structure that allows storage and access of an arbitrary amount of data.

## Feature List of an Effective Linked List

1. **Rebranding**- represents Node as an individual object rather than having one monolithic List type.
2. **Bureacracy:** Create an abstraction barrier so that users do not need to know how methods or Nodes work, only how to call them.
3. **Access Control:** Data cannot be accessed directly to prevent dangerous behavior; only the provided methods are used.
4. **Nested Class:** Nodes are nested within the List object since other classes do not need it.
5. **Caching:** The size of the list is incremented every time a node is added, so running size() is O(1) and traversal is not needed.
6. **Generalizing:** A **sentinel node** represents an empty list and remains the first node of the list. When getFirst() is called, the second node is actually returned (since the first node is always the sentinel).
7. **Doubly Linked:** Nodes have both first and last pointers for even faster traversal.
8. **Circular list:** Sentinel last pointer points to the last value in the node, allowing for fast removeLast().

![An illustration of an effective linked list.](<../../img/assets/image (36).png>)

## Method List

| Method                                                               | Description                                      | Optimal Runtime |
| -------------------------------------------------------------------- | ------------------------------------------------ | --------------- |
| <p><code>addFirst(T x)</code></p><p><code>addLast(T x)</code></p>    | Adds a node to the front/back of the list.       | $\Theta(1)$   |
| <p><code>getFirst()</code></p><p><code>getLast()</code></p>          | Gets the node at the front/back of the list.     | $\Theta(1)$   |
| <p><code>removeFirst()</code></p><p><code>removeLast()</code></p>    | Removes the node at the front/back of the list.  | $\Theta(1)$   |
| `size()`                                                             | Returns the number of nodes in the list.         | $\Theta(1)$   |
| `contains(T x)`                                                      | Returns true if the list contains element `x`.   | $\Theta(n)$   |
| <p><code>add(T x, int pos)</code></p><p><code>remove(T x)</code></p> | Adds/remove an element at an arbitrary location. | $\Theta(n)$   |

## Limitation: Arbitrary Retrieval

You may have noticed in the chart above that it takes $\Theta(n)$  time to retrieve arbitrary values from the list. This will get really slow if the list is large! If arbitrary values need to be accessed frequently, [Arrays](arrays.md) are much better.

## The Java List Interface

Java has a built-in `LinkedList` class so you don't have to implement it yourself! Read up on the [official docs](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html/) to learn more about the specific methods and behaviors provided.

