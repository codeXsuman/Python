
# **CHAPTER-3**

![img](https://i.imghippo.com/files/bzlV7007owE.jpg)

![img](https://i.imghippo.com/files/bqo7407Zqo.jpg)

![img](https://i.imghippo.com/files/lyZt4008cn.jpg)

![img](https://i.imghippo.com/files/pXKR2380KE.jpg)

# **most used string functions in python.**

Here’s a compact but comprehensive list of the **most used string functions** in Python, grouped by category so it’s easy to remember.

---

### **1. Case Conversion**

| Function        | Description                                | Example                                   |
| --------------- | ------------------------------------------ | ----------------------------------------- |
| `.upper()`      | Converts all characters to uppercase       | `"hello".upper()` → `"HELLO"`             |
| `.lower()`      | Converts all characters to lowercase       | `"HELLO".lower()` → `"hello"`             |
| `.title()`      | Capitalizes the first letter of each word  | `"hello world".title()` → `"Hello World"` |
| `.capitalize()` | Capitalizes the first letter of the string | `"hello".capitalize()` → `"Hello"`        |
| `.swapcase()`   | Swaps upper ↔ lower case                   | `"PyThOn".swapcase()` → `"pYtHoN"`        |

---

### **2. Search & Check**

| Function              | Description                                  | Example                             |
| --------------------- | -------------------------------------------- | ----------------------------------- |
| `.find(sub)`          | Returns lowest index of `sub` or `-1`        | `"apple".find("p")` → `1`           |
| `.rfind(sub)`         | Returns highest index of `sub`               | `"apple".rfind("p")` → `2`          |
| `.index(sub)`         | Like `.find()` but raises error if not found | `"apple".index("p")` → `1`          |
| `.startswith(prefix)` | Checks if string starts with given text      | `"hello".startswith("he")` → `True` |
| `.endswith(suffix)`   | Checks if string ends with given text        | `"hello".endswith("lo")` → `True`   |

---

### **3. Replace & Remove**

| Function             | Description                              | Example                                 |
| -------------------- | ---------------------------------------- | --------------------------------------- |
| `.replace(old, new)` | Replace all occurrences                  | `"a b c".replace(" ", "-")` → `"a-b-c"` |
| `.strip()`           | Removes spaces (or chars) from both ends | `" hello ".strip()` → `"hello"`         |
| `.lstrip()`          | Removes from left side only              | `" hello".lstrip()` → `"hello"`         |
| `.rstrip()`          | Removes from right side only             | `"hello ".rstrip()` → `"hello"`         |

---

### **4. Split & Join**

| Function        | Description              | Example                                 |
| --------------- | ------------------------ | --------------------------------------- |
| `.split(sep)`   | Splits string into list  | `"a,b,c".split(",")` → `['a','b','c']`  |
| `.rsplit(sep)`  | Splits from the right    | `"a,b,c".rsplit(",",1)` → `['a,b','c']` |
| `.splitlines()` | Splits by newline (`\n`) | `"a\nb".splitlines()` → `['a','b']`     |
| `.join(list)`   | Joins list into a string | `",".join(['a','b'])` → `"a,b"`         |

---

### **5. Character Check**

| Function     | Description               | Example                            |
| ------------ | ------------------------- | ---------------------------------- |
| `.isalpha()` | True if all letters       | `"abc".isalpha()` → `True`         |
| `.isdigit()` | True if all digits        | `"123".isdigit()` → `True`         |
| `.isalnum()` | True if letters & numbers | `"abc123".isalnum()` → `True`      |
| `.isspace()` | True if only whitespace   | `"   ".isspace()` → `True`         |
| `.islower()` | True if all lowercase     | `"abc".islower()` → `True`         |
| `.isupper()` | True if all uppercase     | `"ABC".isupper()` → `True`         |
| `.istitle()` | True if title case        | `"Hello World".istitle()` → `True` |

---

### **6. Formatting**

| Function               | Description         | Example                          |
| ---------------------- | ------------------- | -------------------------------- |
| `.center(width, char)` | Centers text        | `"hi".center(5,"-")` → `"--hi-"` |
| `.ljust(width, char)`  | Left-aligns text    | `"hi".ljust(5,"-")` → `"hi---"`  |
| `.rjust(width, char)`  | Right-aligns text   | `"hi".rjust(5,"-")` → `"---hi"`  |
| `.zfill(width)`        | Pads with zeros     | `"7".zfill(3)` → `"007"`         |
| `.format()`            | String formatting   | `"{} + {} = {}".format(2,3,5)`   |
| `f""`                  | f-string formatting | `f"{2+3}"` → `"5"`               |

---
