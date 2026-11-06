# Python Pattern Programs

> **A visual gallery of 97 Python pattern programs.** Every pattern below includes its actual console output, generated from the corresponding Python source with `n = 5`.

Browse the previews directly in this README, then open the linked `.py` file to see how each pattern is built.

## Quick navigation

- [Squares and rectangles](#squares-and-rectangles)
- [Left-aligned triangles](#left-aligned-triangles)
- [Right-aligned triangles](#right-aligned-triangles)
- [Centered pyramids](#centered-pyramids)
- [Inverted pyramids](#inverted-pyramids)
- [Diamonds and hourglasses](#diamonds-and-hourglasses)
- [Hollow pyramids](#hollow-pyramids)
- [Special patterns](#special-patterns)

## How to run

```bash
python3 Pattern1.py
```

Enter `5` when prompted to reproduce the previews. Spacing is preserved inside the code blocks, so shapes remain aligned.

---

## Squares and rectangles

### Pattern 1 — Solid square of stars

**Source:** [`Pattern1.py`](Pattern1.py)  ·  **Example input:** `5`

**Output**

```text
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

### Pattern 2 — Number square with repeated row values

**Source:** [`Pattern2.py`](Pattern2.py)  ·  **Example input:** `5`

**Output**

```text
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
```

### Pattern 3 — Number square with ascending columns

**Source:** [`Pattern3.py`](Pattern3.py)  ·  **Example input:** `5`

**Output**

```text
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
```

### Pattern 4 — Alphabet square with repeated row letters

**Source:** [`Pattern4.py`](Pattern4.py)  ·  **Example input:** `5`

**Output**

```text
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE
```

### Pattern 5 — Alphabet square with repeated row letters (compact)

**Source:** [`Pattern5.py`](Pattern5.py)  ·  **Example input:** `5`

**Output**

```text
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE
```

### Pattern 6 — Inverted number square

**Source:** [`Pattern6.py`](Pattern6.py)  ·  **Example input:** `5`

**Output**

```text
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
```

### Pattern 7 — Descending number sequence square

**Source:** [`Pattern7.py`](Pattern7.py)  ·  **Example input:** `5`

**Output**

```text
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
```

### Pattern 8 — Descending alphabet-row square

**Source:** [`Pattern8.py`](Pattern8.py)  ·  **Example input:** `5`

**Output**

```text
E E E E E
D D D D D
C C C C C
B B B B B
A A A A A
```

### Pattern 9 — Reverse alphabet sequence square

**Source:** [`Pattern9.py`](Pattern9.py)  ·  **Example input:** `5`

**Output**

```text
E D C B A
E D C B A
E D C B A
E D C B A
E D C B A
```

### Pattern 94 — Right-aligned star rectangle

**Source:** [`Pattern94.py`](Pattern94.py)  ·  **Example input:** `5`

**Output**

```text
* * * * *
 * * * * *
  * * * * *
   * * * * *
    * * * * *
```

---

## Left-aligned triangles

### Pattern 10 — Left-aligned star triangle

**Source:** [`Pattern10.py`](Pattern10.py)  ·  **Example input:** `5`

**Output**

```text
*
* *
* * *
* * * *
* * * * *
```

### Pattern 11 — Repeated-row-number triangle

**Source:** [`Pattern11.py`](Pattern11.py)  ·  **Example input:** `5`

**Output**

```text
1
22
333
4444
55555
```

### Pattern 12 — Ascending number triangle

**Source:** [`Pattern12.py`](Pattern12.py)  ·  **Example input:** `5`

**Output**

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

### Pattern 13 — Repeated-row-letter triangle

**Source:** [`Pattern13.py`](Pattern13.py)  ·  **Example input:** `5`

**Output**

```text
A
B B
C C C
D D D D
E E E E E
```

### Pattern 14 — Ascending alphabet triangle

**Source:** [`Pattern14.py`](Pattern14.py)  ·  **Example input:** `5`

**Output**

```text
A
A B
A B C
A B C D
A B C D E
```

### Pattern 15 — Inverted star triangle

**Source:** [`Pattern15.py`](Pattern15.py)  ·  **Example input:** `5`

**Output**

```text
* * * * *
* * * *
* * *
* *
*
```

### Pattern 16 — Inverted repeated-row-number triangle

**Source:** [`Pattern16.py`](Pattern16.py)  ·  **Example input:** `5`

**Output**

```text
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
```

### Pattern 17 — Inverted ascending number triangle

**Source:** [`Pattern17.py`](Pattern17.py)  ·  **Example input:** `5`

**Output**

```text
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

### Pattern 18 — Inverted repeated-row-letter triangle

**Source:** [`Pattern18.py`](Pattern18.py)  ·  **Example input:** `5`

**Output**

```text
A A A A A
B B B B
C C C
D D
E
```

### Pattern 19 — Inverted alphabet sequence triangle

**Source:** [`Pattern19.py`](Pattern19.py)  ·  **Example input:** `5`

**Output**

```text
A B C D E
A B C D
A B C
A B
A
```

### Pattern 20 — Inverted repeated-value number triangle

**Source:** [`Pattern20.py`](Pattern20.py)  ·  **Example input:** `5`

**Output**

```text
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
```

### Pattern 21 — Inverted descending-number triangle

**Source:** [`Pattern21.py`](Pattern21.py)  ·  **Example input:** `5`

**Output**

```text
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
```

### Pattern 22 — Inverted repeated-letter triangle

**Source:** [`Pattern22.py`](Pattern22.py)  ·  **Example input:** `5`

**Output**

```text
E E E E E
D D D D
C C C
B B
A
```

### Pattern 23 — Inverted descending-alphabet triangle

**Source:** [`Pattern23.py`](Pattern23.py)  ·  **Example input:** `5`

**Output**

```text
E D C B A
E D C B
E D C
E D
E
```

---

## Right-aligned triangles

### Pattern 24 — Right-aligned star triangle

**Source:** [`Pattern24.py`](Pattern24.py)  ·  **Example input:** `5`

**Output**

```text
    *
   * *
  * * *
 * * * *
* * * * *
```

### Pattern 25 — Right-aligned solid star triangle

**Source:** [`Pattern25.py`](Pattern25.py)  ·  **Example input:** `5`

**Output**

```text
     *
    **
   ***
  ****
 *****
```

### Pattern 26 — Right-aligned repeated-row-number triangle

**Source:** [`Pattern26.py`](Pattern26.py)  ·  **Example input:** `5`

**Output**

```text
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
```

### Pattern 27 — Right-aligned ascending-number triangle

**Source:** [`Pattern27.py`](Pattern27.py)  ·  **Example input:** `5`

**Output**

```text
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
```

### Pattern 28 — Right-aligned repeated-row-letter triangle

**Source:** [`Pattern28.py`](Pattern28.py)  ·  **Example input:** `5`

**Output**

```text
    A
   B B
  C C C
 D D D D
E E E E E
```

### Pattern 29 — Right-aligned ascending-alphabet triangle

**Source:** [`Pattern29.py`](Pattern29.py)  ·  **Example input:** `5`

**Output**

```text
    A
   A B
  A B C
 A B C D
A B C D E
```

### Pattern 30 — Right-aligned inverted star triangle

**Source:** [`Pattern30.py`](Pattern30.py)  ·  **Example input:** `5`

**Output**

```text
*****
 ****
  ***
   **
    *
```

### Pattern 31 — Right-aligned inverted repeated-number triangle

**Source:** [`Pattern31.py`](Pattern31.py)  ·  **Example input:** `5`

**Output**

```text
55555
 4444
  333
   22
    1
```

### Pattern 32 — Right-aligned inverted ascending-number triangle

**Source:** [`Pattern32.py`](Pattern32.py)  ·  **Example input:** `5`

**Output**

```text
12345
 1234
  123
   12
    1
```

### Pattern 33 — Right-aligned inverted repeated-letter triangle

**Source:** [`Pattern33.py`](Pattern33.py)  ·  **Example input:** `5`

**Output**

```text
EEEEE
 DDDD
  CCC
   BB
    A
```

### Pattern 34 — Right-aligned inverted alphabet-sequence triangle

**Source:** [`Pattern34.py`](Pattern34.py)  ·  **Example input:** `5`

**Output**

```text
ABCDE
 ABCD
  ABC
   AB
    A
```

### Pattern 70 — Right-aligned inverted star triangle

**Source:** [`Pattern70.py`](Pattern70.py)  ·  **Example input:** `5`

**Output**

```text
 * * * * *
  * * * *
   * * *
    * *
     *
```

### Pattern 71 — Right-aligned inverted repeated-number triangle

**Source:** [`Pattern71.py`](Pattern71.py)  ·  **Example input:** `5`

**Output**

```text
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
```

### Pattern 72 — Right-aligned inverted descending-number triangle

**Source:** [`Pattern72.py`](Pattern72.py)  ·  **Example input:** `5`

**Output**

```text
5 4 3 2 1
 4 3 2 1
  3 2 1
   2 1
    1
```

### Pattern 73 — Right-aligned inverted repeated-letter triangle

**Source:** [`Pattern73.py`](Pattern73.py)  ·  **Example input:** `5`

**Output**

```text
E E E E E
 D D D D
  C C C
   B B
    A
```

### Pattern 74 — Right-aligned inverted descending-alphabet triangle

**Source:** [`Pattern74.py`](Pattern74.py)  ·  **Example input:** `5`

**Output**

```text
E D C B A
 D C B A
  C B A
   B A
    A
```

### Pattern 75 — Right-aligned inverted ascending-alphabet triangle

**Source:** [`Pattern75.py`](Pattern75.py)  ·  **Example input:** `5`

**Output**

```text
A B C D E
 A B C D
  A B C
   A B
    A
```

---

## Centered pyramids

### Pattern 35 — Centered star pyramid

**Source:** [`Pattern35.py`](Pattern35.py)  ·  **Example input:** `5`

**Output**

```text
         *
       * * *
     * * * * *
   * * * * * * *
 * * * * * * * * *
```

### Pattern 36 — Centered repeated-number pyramid

**Source:** [`Pattern36.py`](Pattern36.py)  ·  **Example input:** `5`

**Output**

```text
         1
       2 2 2
     3 3 3 3 3
   4 4 4 4 4 4 4
 5 5 5 5 5 5 5 5 5
```

### Pattern 37 — Centered repeated-letter pyramid

**Source:** [`Pattern37.py`](Pattern37.py)  ·  **Example input:** `5`

**Output**

```text
         A
       B B B
     C C C C C
   D D D D D D D
 E E E E E E E E E
```

### Pattern 38 — Centered odd-letter pyramid

**Source:** [`Pattern38.py`](Pattern38.py)  ·  **Example input:** `5`

**Output**

```text
         A
       C C C
     E E E E E
   G G G G G G G
 I I I I I I I I I
```

### Pattern 39 — Centered ascending-number pyramid

**Source:** [`Pattern39.py`](Pattern39.py)  ·  **Example input:** `5`

**Output**

```text
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
```

### Pattern 40 — Centered descending-number pyramid

**Source:** [`Pattern40.py`](Pattern40.py)  ·  **Example input:** `5`

**Output**

```text
        1
      3 2 1
    5 4 3 2 1
  7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
```

### Pattern 41 — Centered ascending-alphabet pyramid

**Source:** [`Pattern41.py`](Pattern41.py)  ·  **Example input:** `5`

**Output**

```text
        A
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I
```

### Pattern 42 — Centered descending-alphabet pyramid

**Source:** [`Pattern42.py`](Pattern42.py)  ·  **Example input:** `5`

**Output**

```text
        A
      C B A
    E D C B A
  G F E D C B A
I H G F E D C B A
```

### Pattern 43 — Centered mirrored number pyramid

**Source:** [`Pattern43.py`](Pattern43.py)  ·  **Example input:** `5`

**Output**

```text
    0
   101
  21012
 3210123
432101234
```

### Pattern 44 — Centered mirrored alphabet pyramid

**Source:** [`Pattern44.py`](Pattern44.py)  ·  **Example input:** `5`

**Output**

```text
    A
   BAB
  CBABC
 DCBABCD
EDCBABCDE
```

### Pattern 45 — Centered numeric palindrome pyramid

**Source:** [`Pattern45.py`](Pattern45.py)  ·  **Example input:** `5`

**Output**

```text
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
```

### Pattern 46 — Centered alphabet palindrome pyramid

**Source:** [`Pattern46.py`](Pattern46.py)  ·  **Example input:** `5`

**Output**

```text
        A
      A B A
    A B C A B
  A B C D A B C
A B C D E A B C D
```

### Pattern 66 — Centered star triangle

**Source:** [`Pattern66.py`](Pattern66.py)  ·  **Example input:** `5`

**Output**

```text
    *
   * *
  * * *
 * * * *
* * * * *
```

### Pattern 66 (alternate) — Centered repeated-row-number triangle (alternate file)

**Source:** [`Pattern66_1.py`](Pattern66_1.py)  ·  **Example input:** `5`

**Output**

```text
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
```

### Pattern 67 — Centered ascending-number triangle

**Source:** [`Pattern67.py`](Pattern67.py)  ·  **Example input:** `5`

**Output**

```text
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
```

### Pattern 68 — Centered repeated-letter triangle

**Source:** [`Pattern68.py`](Pattern68.py)  ·  **Example input:** `5`

**Output**

```text
    A
   B B
  C C C
 D D D D
E E E E E
```

### Pattern 69 — Centered ascending-alphabet triangle

**Source:** [`Pattern69.py`](Pattern69.py)  ·  **Example input:** `5`

**Output**

```text
    A
   A B
  A B C
 A B C D
A B C D E
```

---

## Inverted pyramids

### Pattern 47 — Right-aligned descending-number pyramid

**Source:** [`Pattern47.py`](Pattern47.py)  ·  **Example input:** `5`

**Output**

```text
     5
    5 4
   5 4 3
  5 4 3 2
 5 4 3 2 1
```

### Pattern 48 — Inverted centered star pyramid

**Source:** [`Pattern48.py`](Pattern48.py)  ·  **Example input:** `5`

**Output**

```text
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
```

### Pattern 49 — Inverted centered repeated-row-number pyramid

**Source:** [`Pattern49.py`](Pattern49.py)  ·  **Example input:** `5`

**Output**

```text
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1
```

### Pattern 50 — Inverted centered odd-number pyramid

**Source:** [`Pattern50.py`](Pattern50.py)  ·  **Example input:** `5`

**Output**

```text
9 9 9 9 9 9 9 9 9
  7 7 7 7 7 7 7
    5 5 5 5 5
      3 3 3
        1
```

### Pattern 51 — Inverted centered ascending-number pyramid

**Source:** [`Pattern51.py`](Pattern51.py)  ·  **Example input:** `5`

**Output**

```text
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1
```

### Pattern 52 — Inverted centered repeated-letter pyramid

**Source:** [`Pattern52.py`](Pattern52.py)  ·  **Example input:** `5`

**Output**

```text
E E E E E E E E E
  D D D D D D D
    C C C C C
      B B B
        A
```

### Pattern 53 — Inverted centered odd-letter pyramid

**Source:** [`Pattern53.py`](Pattern53.py)  ·  **Example input:** `5`

**Output**

```text
I I I I I I I I I
  G G G G G G G
    E E E E E
      C C C
        A
```

### Pattern 54 — Inverted centered alphabet-sequence pyramid

**Source:** [`Pattern54.py`](Pattern54.py)  ·  **Example input:** `5`

**Output**

```text
A B C D E F G H I
  A B C D E F G
    A B C D E
      A B C
        A
```

---

## Diamonds and hourglasses

### Pattern 55 — Diamond of ascending-number triangles

**Source:** [`Pattern55.py`](Pattern55.py)  ·  **Example input:** `5`

**Output**

```text
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
```

### Pattern 56 — Solid star diamond

**Source:** [`Pattern56.py`](Pattern56.py)  ·  **Example input:** `5`

**Output**

```text
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
```

### Pattern 57 — Hourglass of descending numbers

**Source:** [`Pattern57.py`](Pattern57.py)  ·  **Example input:** `5`

**Output**

```text
     5
    5 4
   5 4 3
  5 4 3 2
 5 4 3 2 1
5 4 3 2 1 0
 5 4 3 2 1
  5 4 3 2
   5 4 3
    5 4
     5
```

### Pattern 58 — Hourglass of ascending number ranges

**Source:** [`Pattern58.py`](Pattern58.py)  ·  **Example input:** `5`

**Output**

```text
      5
     4 5
    3 4 5
   2 3 4 5
  1 2 3 4 5
 0 1 2 3 4 5
  1 2 3 4 5
   2 3 4 5
    3 4 5
     4 5
      5
```

### Pattern 59 — Hourglass of alphabet ranges

**Source:** [`Pattern59.py`](Pattern59.py)  ·  **Example input:** `5`

**Output**

```text

     E
    D E
   C D E
  B C D E
 A B C D E
  B C D E
   C D E
    D E
     E
```

### Pattern 60 — Vertical star bow-tie

**Source:** [`Pattern60.py`](Pattern60.py)  ·  **Example input:** `5`

**Output**

```text
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
```

### Pattern 61 — Hourglass of descending number rows

**Source:** [`Pattern61.py`](Pattern61.py)  ·  **Example input:** `5`

**Output**

```text
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2 1 0
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
```

### Pattern 62 — Hourglass of ascending number strings

**Source:** [`Pattern62.py`](Pattern62.py)  ·  **Example input:** `5`

**Output**

```text
5
45
345
2345
12345
012345
12345
2345
345
45
5
```

### Pattern 63 — Hourglass of repeated alphabet rows

**Source:** [`Pattern63.py`](Pattern63.py)  ·  **Example input:** `5`

**Output**

```text
E
D D
C C C
B B B B
A A A A A
B B B B
C C C
D D
E
```

### Pattern 64 — Hourglass of descending alphabet ranges

**Source:** [`Pattern64.py`](Pattern64.py)  ·  **Example input:** `5`

**Output**

```text

E
E D
E D C
E D C B
E D C B A
E D C B
E D C
E D
E
```

### Pattern 65 — Hourglass of ascending alphabet ranges

**Source:** [`Pattern65.py`](Pattern65.py)  ·  **Example input:** `5`

**Output**

```text
E
D E
C D E
B C D E
A B C D E
B C D E
C D E
D E
E
```

### Pattern 76 — Centered star diamond outline/fill variant

**Source:** [`Pattern76.py`](Pattern76.py)  ·  **Example input:** `5`

**Output**

```text
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
```

### Pattern 77 — Centered repeated-number diamond

**Source:** [`Pattern77.py`](Pattern77.py)  ·  **Example input:** `5`

**Output**

```text
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
```

### Pattern 78 — Mirrored ascending-number triangle pair

**Source:** [`Pattern78.py`](Pattern78.py)  ·  **Example input:** `5`

**Output**

```text
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 2 3 4 5
  3 4 5
   4 5
    5
```

### Pattern 79 — Diamond of ascending-number triangles

**Source:** [`Pattern79.py`](Pattern79.py)  ·  **Example input:** `5`

**Output**

```text
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
```

### Pattern 80 — Diamond of repeated-row letters

**Source:** [`Pattern80.py`](Pattern80.py)  ·  **Example input:** `5`

**Output**

```text
    A
   B B
  C C C
 D D D D
E E E E E
 D D D D
  C C C
   B B
    A
```

### Pattern 81 — Mirrored alphabet triangle pair

**Source:** [`Pattern81.py`](Pattern81.py)  ·  **Example input:** `5`

**Output**

```text
    A
   A B
  A B C
 A B C D
A B C D E
 B C D E
  C D E
   D E
    E
```

### Pattern 82 — Hourglass of palindromic number rows

**Source:** [`Pattern82.py`](Pattern82.py)  ·  **Example input:** `5`

**Output**

```text
     5
    454
   34543
  2345432
 123454321
 2345432
  34543
   454
    5
```

### Pattern 83 — Diamond of palindromic number rows

**Source:** [`Pattern83.py`](Pattern83.py)  ·  **Example input:** `5`

**Output**

```text
     5
    545
   54345
  5432345
 543212345
 5432345
  54345
   545
    5
```

---

## Hollow pyramids

### Pattern 84 — Hollow centered star pyramid

**Source:** [`Pattern84.py`](Pattern84.py)  ·  **Example input:** `5`

**Output**

```text
    *
   **
  *  *
 *    *
*      *
```

### Pattern 85 — Hollow centered repeated-number pyramid

**Source:** [`Pattern85.py`](Pattern85.py)  ·  **Example input:** `5`

**Output**

```text
    1
   22
  3  3
 4    4
5      5
```

### Pattern 86 — Hollow centered descending-number pyramid

**Source:** [`Pattern86.py`](Pattern86.py)  ·  **Example input:** `5`

**Output**

```text
    5
   44
  3  3
 2    2
1      1
```

### Pattern 87 — Hollow centered descending-alphabet pyramid

**Source:** [`Pattern87.py`](Pattern87.py)  ·  **Example input:** `5`

**Output**

```text
    E
   DD
  C  C
 B    B
A      A
```

### Pattern 88 — Hollow centered repeated-letter pyramid

**Source:** [`Pattern88.py`](Pattern88.py)  ·  **Example input:** `5`

**Output**

```text
    A
   BB
  C  C
 D    D
E      E
```

### Pattern 89 — Inverted hollow star pyramid

**Source:** [`Pattern89.py`](Pattern89.py)  ·  **Example input:** `5`

**Output**

```text
*      *
 *    *
  *  *
   **
    *
```

### Pattern 90 — Inverted hollow descending-number pyramid

**Source:** [`Pattern90.py`](Pattern90.py)  ·  **Example input:** `5`

**Output**

```text
1      1
 2    2
  3  3
   44
    5
```

### Pattern 91 — Inverted hollow repeated-number pyramid

**Source:** [`Pattern91.py`](Pattern91.py)  ·  **Example input:** `5`

**Output**

```text
5      5
 4    4
  3  3
   22
    1
```

### Pattern 92 — Inverted hollow repeated-letter pyramid

**Source:** [`Pattern92.py`](Pattern92.py)  ·  **Example input:** `5`

**Output**

```text
E      E
 D    D
  C  C
   BB
    A
```

### Pattern 93 — Inverted hollow descending-alphabet pyramid

**Source:** [`Pattern93.py`](Pattern93.py)  ·  **Example input:** `5`

**Output**

```text
A      A
 B    B
  C  C
   DD
    E
```

---

## Special patterns

### Pattern 95 — Butterfly star pattern

**Source:** [`Pattern95.py`](Pattern95.py)  ·  **Example input:** `5`

**Output**

```text
    *     *
   * *    * *
  * * *   * * *
 * * * *  * * * *
* * * * * * * * * *
```

### Pattern 96 — Alternating binary triangle

**Source:** [`Pattern96.py`](Pattern96.py)  ·  **Example input:** `5`

**Output**

```text
1
01
101
0101
10101
```

---

## Notes

- The examples are generated from the active Python code, not copied from commented examples.
- Some patterns intentionally use different spacing styles (for example, `* * *` versus `***`).
- The two separate files `Pattern66.py` and `Pattern66_1.py` both appear in the gallery.
- `Pattern1.py` contains a bare `output :` line that causes a syntax error. For its preview only, that non-code heading was treated as a comment; the pattern-printing logic itself was left unchanged.
- The original `.py` files are unchanged.
