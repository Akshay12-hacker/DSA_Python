# 📌 Array Notes (Python `array` Module)

---

## 1️⃣ Importing Array
```python
from array import *
array module homogeneous data store karta hai

Matlab: same data type only (int, float, etc.)

2️⃣ Creating an Array
val = array('i', [1,2,3,4,5,3,5,2,3,4,6])
'i' → typecode (signed integer)

List se array banaya gaya

Common Typecodes
'i' → int

'f' → float

'd' → double

3️⃣ Printing the Array
print(val)
Poora array print hota hai

4️⃣ Accessing Elements (Indexing)
Using range
for i in range(0,6):
    print(val[i], end="")
Direct Iteration
for i in val:
    print(i, end=" ")
Using len()
for i in range(0, len(val)):
    print(val[i], end=" ")
👉 Best Practice
Sirf value chahiye → for i in val

Index chahiye → range(len(val))

5️⃣ Typecode
print(val.typecode)
Array ka data type batata hai

Important jab copy ya new array banate ho

6️⃣ Reversing an Array
val.reverse()
Original array ko in-place reverse karta hai

7️⃣ Inserting & Updating Elements
val.insert(1, 99)   # index 1 par 99
val.append(100)     # last me add
val[2] = 200        # value update
Difference
insert(index, value) → slow (elements shift hote hain)

append(value) → fast

8️⃣ Copying an Array (IMPORTANT)
copyArray = array(val.typecode, (x for x in val))
Generator use karke proper deep copy

= use karoge to reference copy hoga ❌

9️⃣ Removing Elements
copyArray.pop(3)     # index ke basis par remove
copyArray.remove(3)  # value ke basis par remove
⚠ Difference
pop() → index

remove() → pehli matching value

🔟 Slicing
abc = val[2:5]   # index 2 to 4
abc = val[::-1]  # reverse copy
Format
array[start : end : step]
1️⃣1️⃣ Creating Empty Array & Taking Input
arr23 = array('i', [])
n = int(input("Enter a Number"))

for i in range(0,n):
    arr23.append(int(input("Enter next input")))
Empty array banane ke baad append() se fill karte hain

1️⃣2️⃣ Searching an Element
i = arr23.index(0)
print(i)
Element ka first index return karta hai

Agar element nahi mila → error aayega ⚠

🔥 Python Array vs NumPy Array (VERY IMPORTANT)
Python array Module
✔ Lightweight
✔ Basic operations
❌ Limited features
❌ No matrix operations

Use When:
Simple integer / float storage

Low-level understanding

NumPy Array
import numpy as np
arr = np.array([1,2,3,4])
✔ Super fast (C-based)
✔ Vector operations
✔ Matrix, slicing, broadcasting
✔ ML / Data Science mandatory

Example
arr * 2   # Output: [2, 4, 6, 8]
⚠ Python array me yeh operation possible nahi hota

