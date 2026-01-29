# 📘 NumPy Array Notes (`numpy`)

---

## 1️⃣ What is NumPy?
- NumPy = **Numerical Python**
- Fast because it is written in **C**
- Used in **Data Science, Machine Learning, AI, Scientific Computing**

```python
import numpy as np
2️⃣ Creating NumPy Arrays
From Python List
arr = np.array([1, 2, 3, 4])
Using Built-in Functions
np.zeros(5)          # [0. 0. 0. 0. 0.]
np.ones(5)           # [1. 1. 1. 1. 1.]
np.arange(1, 10, 2)  # [1 3 5 7 9]
np.linspace(1, 10, 5)
3️⃣ Array Properties (VERY IMPORTANT)
arr.ndim     # Number of dimensions
arr.shape    # Rows, Columns
arr.size     # Total number of elements
arr.dtype    # Data type
Example:

arr = np.array([[1,2],[3,4]])
ndim → 2

shape → (2, 2)

size → 4

4️⃣ Accessing Elements (Indexing)
1D Array
arr[0]
arr[-1]
2D Array
arr[0][1]
arr[1, 0]
5️⃣ Slicing (POWERFUL FEATURE)
arr[1:4]
arr[::-1]
arr[:, 1]
arr[0, :]
Format
array[row, column]
6️⃣ Vectorized Operations (GAME CHANGER)
arr + 2
arr * 3
arr1 + arr2
✔ No loops
✔ Very fast
❌ Not possible in Python array or list directly

7️⃣ Mathematical Functions
np.sum(arr)
np.min(arr)
np.max(arr)
np.mean(arr)
np.sqrt(arr)
np.sin(arr)
np.log(arr)
8️⃣ Copy vs View (INTERVIEW FAVORITE)
View (Shallow Copy)
b = arr.view()
Changes reflect in original array

Copy (Deep Copy)
c = arr.copy()
Independent memory allocation

9️⃣ Reshaping Arrays
arr.reshape(2, 2)
arr.flatten()
⚠ Rule:

Total elements must remain same

🔟 Joining & Splitting Arrays
Joining
np.concatenate((a, b))
np.vstack((a, b))
np.hstack((a, b))
Splitting
np.array_split(arr, 3)
1️⃣1️⃣ Iterating NumPy Arrays
Normal Loop
for i in arr:
    print(i)
Using nditer
for i in np.nditer(arr):
    print(i)
1️⃣2️⃣ Searching & Sorting
np.where(arr == 5)
np.sort(arr)
1️⃣3️⃣ Random Module
np.random.rand(5)
np.random.randint(1, 10, 5)
np.random.shuffle(arr)
1️⃣4️⃣ Broadcasting (ADVANCED but IMPORTANT)
arr = np.array([1, 2, 3])
arr + np.array([10])
Smaller array automatically expand hota hai

1️⃣5️⃣ Why NumPy is Fast?
Contiguous memory allocation

C-level execution

No Python loop overhead

