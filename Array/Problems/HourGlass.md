# Hourglass Sum Problem – Python Notes

## 1. Problem Definition

Given a **6×6 2D array**, an **hourglass** is a subset of 7 elements in the following pattern:

a b c  
  d  
e f g  

The **hourglass sum** is the sum of these 7 elements.

Your task:
- Calculate the hourglass sum for **every possible hourglass**
- Return the **maximum hourglass sum**

---

## 2. Important Observations

- Hourglass size is **fixed (3×3 shape)**
- Only **7 elements** are counted (not all 9)
- Array size is **6×6**
- Total hourglasses in a 6×6 array:
  
(6 - 2) × (6 - 2) = 4 × 4 = 16


---

## 3. Loop Boundaries (Most Important Part)

Why loops go till `4`?

- Hourglass needs:
- row `i`, `i+1`, `i+2`
- column `j`, `j+1`, `j+2`

So:
- `i` can go from `0 → 3`
- `j` can go from `0 → 3`

Using anything beyond this will cause **index out of range error**.

---

## 4. Hourglass Sum Formula

For a starting index `(i, j)`:

Top row:
arr[i][j] + arr[i][j+1] + arr[i][j+2]


Middle:
arr[i+1][j+1]


Bottom row:
arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]


Total = **7 elements**

---

## 5. Critical Mistake to Avoid ❌

❌ Initializing max sum as `0`

Why wrong?
- Hourglass sums can be **negative**
- Example includes `-63`

✅ Correct initialization:
```python
max_sum = float('-inf')
6. Correct Python Solution
def hourglassSum(arr):
    max_sum = float('-inf')

    for i in range(4):
        for j in range(4):
            current_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                arr[i+1][j+1] +
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )

            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum
7. Dry Run Example
Hourglass:

2 4 4
  2
1 2 4
Calculation:

2 + 4 + 4 = 10
+ 2        = 12
1 + 2 + 4  = 7
----------------
Total = 19
8. Time & Space Complexity
Time Complexity: O(1)

Fixed 6×6 → always 16 hourglasses

Space Complexity: O(1)

No extra memory used