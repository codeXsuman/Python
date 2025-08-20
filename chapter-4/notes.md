
# **CHAPTER-4**

![img](https://i.imghippo.com/files/wbVQ7636Lk.jpg)

![img](https://i.imghippo.com/files/Fwpp4893qKI.jpg)

![img](https://i.imghippo.com/files/iiW3171nU.jpg)

## **tuple**
In Python, **tuples** are immutable (can’t be changed once created), so they don’t have as many methods as lists. But still, they come with a few useful ones:

### Common Tuple Methods:

1. **`tuple.count(x)`** → Returns how many times `x` appears in the tuple.

   ```python
   t = (1, 2, 3, 2, 4, 2)
   print(t.count(2))   # Output: 3
   ```

2. **`tuple.index(x[, start[, end]])`** → Returns the index of the first occurrence of `x`. Raises an error if not found.

   ```python
   t = (10, 20, 30, 20, 40)
   print(t.index(20))       # Output: 1
   print(t.index(20, 2))    # Output: 3
   ```

---

👉 Apart from these **two direct methods**, you can also use built-in functions on tuples:

* **`len(tuple)`** → Get length.
* **`max(tuple)`** → Largest element.
* **`min(tuple)`** → Smallest element.
* **`sum(tuple)`** → Sum of numbers.
* **`sorted(tuple)`** → Returns a sorted **list**.
* **`any(tuple)`** → Returns `True` if any element is truthy.
* **`all(tuple)`** → Returns `True` if all elements are truthy.

Example:

```python
t = (5, 1, 7, 3)
print(len(t))      # 4
print(max(t))      # 7
print(min(t))      # 1
print(sum(t))      # 16
print(sorted(t))   # [1, 3, 5, 7]
```

---
