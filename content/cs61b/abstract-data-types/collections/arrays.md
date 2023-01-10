
> [!info] Content Note
>
> This page assumes prior knowledge of Python lists from CS61A or equivalent.

Arrays are a very popular data structure that stores an indexed list of data. 


![An artistic interpretation of a new int\[5\] {6, 1, 2, 3, 99};](<../../img/assets/image (37).png>)

## Properties

* **Fixed length:** after instantiation, the length of an array cannot be changed.
* Every value in array is the **same type** and holds the **same amount of bits** in memory.
* **Zero-indexed.** That means `arr[0]` returns the first value, and `arr[arr.length]` is out of bounds.
* **No methods.** Helper methods from other libraries (like `System.arraycopy`) need to be used to manipulate arrays.
* **Retrieval is independent of size** and takes constant time regardless of how big arrays are.

## Using Arrays in Java

**Instantiation:**

* `int[] a = {1, 2, 3, 4, 5};` assigns values.
* `int b = new int[3];` creates array of provided length populated with default values.

**Copying**

* Simply assigning `int[] c = b` will copy the **pointer** to array b! Not the values! See [Java Objects](/cs61b/oop/objects.md) for a discussion on why this is significant.
* Use `System.arraycopy(source, start, target, startTarget, amountToCopy)` to **shallow copy** the values (or pointers) in the array. That is, if an array is holding **reference types,** only the pointers will be copied and not the actual values of the reference objects being held.
* `System.arraycopy(b, 0, x, 3, 2)` is equivalent to `x[3:5] = b[0:2]` in Python.

**Multidimensional Arrays**

* `int[][] 2d = new int[4][4];`or `int[][] 2d = new int[][] {{1}, {2, 3}, {4, 5, 6}};`will create **arrays inside of an array.** This is useful for storing matrices, coordinate maps, or any other multidimensional data!

**Generic Arrays**

* Arrays of generic objects are NOT allowed! Use ArrayLists instead.
* Or, this workaround can be used:`Type[] items = (Type[]) new Object[length]`

## Array Lists

Java has another built-in type that uses an array under the hood, which is the `ArrayList`. Here's how ArrayLists are different from normal arrays:

* ArrayLists can resize arbitrarily. (They use something similar to the array case study in the [Amortization](/cs61b/asymptotics/amortization.md#what-if-we-doubled-the-size-instead-of-adding-one) page.
* ArrayLists use [Generic Types](/cs61b/oop/generics) and therefore do not support primitive types like `int`.
* ArrayLists have all behaviors expected from the [Collections](/cs61b/collections) interface.
