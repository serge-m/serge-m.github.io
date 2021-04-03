---
Title: Data Structures And Algorithms in Python
Author: SergeM
Date: 2021-01-29 21:39:00
Slug: data-structures-and-algorithms-in-python
aliases: [/data-structures-and-algorithms-in-python.html]
Tags: [ python, data structure, algorithm ]
---





# Data strucures 

Sources: 
* [https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)
* [https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)

`n` is the number of elements in the container.

`k` is either the value of a parameter, or the number of elements in the parameter.

## list

It is actually an array (implemented as an array).


Operation | Average Case | Amortized Worst Case | Note
-----| ----- | ----- | --- 
Copy | O(n) | O(n)
Append | O(1) | O(1) | If the array grows beyond the allocated space it must be copied. In the worst case O(n)
Pop last | O(1) | O(1)
Pop intermediate | O(n)| O(n) | Popping the intermediate element requires shifting all elements after k by one slot to the left using memmove. n - k elements have to be moved, so the operation is O(n - k).
Insert| O(n)| O(n)
Get Item| O(1)| O(1)
Set Item|O(1)|O(1)
Delete Item|O(n)|O(n)
Iteration|O(n)|O(n)
Get Slice|O(k)|O(k)
Del Slice|O(n)|O(n)
Set Slice|O(k+n)|O(k+n)
Extend|O(k)|O(k) | If the array grows beyond the allocated space it must be copied. In the worst case O(n)
Sort|O(n log n)|O(n log n) | sorting is implemented as [timsort](https://en.wikipedia.org/wiki/Timsort). Sorting is stable, requires O(n) additional memory.
Multiply|O(nk)|O(nk)
x in s|O(n)|
min(s), max(s)|O(n)
Get Length|O(1)|O(1)


## collections.deque

A deque (double-ended queue) is represented internally as a *doubly linked list*. 
(Well, a list of arrays rather than objects, for greater efficiency.) 
Both ends are accessible, but even looking at the middle is slow, and adding to or removing from the middle is slower still.

Operation | Average Case | Amortized Worst Case
---|---|----
Copy| O(n) | O(n)
append | O(1) | O(1)
appendleft|O(1)|O(1)
pop|O(1)|O(1)
popleft|O(1)|O(1)
extend|O(k)|O(k)
extendleft|O(k)|O(k)
rotate|O(k)|O(k)
remove|O(n)|O(n)

## set

See dict -- the implementation is intentionally very similar.

Operation|Average case|Worst Case|notes
---|---|---|---
copy      | O(n) | O(n) | `s.copy()`
iteration | O(n) | O(n) | `for x in my_set: ...` [source](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
x in s | O(1) | O(n) | 
Union s &#124; t | O(len(s)+len(t))|
Intersection s&t | O(min(len(s), len(t)) | O(len(s) * len(t)) | replace "min" with "max" if t is not a set
Multiple intersection s1&s2&..&sn | (n-1)*O(l) where l is max(len(s1),..,len(sn)) | 
Difference s-t  | O(len(s))
s.difference_update(t) | O(len(t))
Symmetric Difference s^t | O(len(s)) | O(len(s) * len(t))
s.symmetric_difference_update(t) | O(len(t)) | O(len(t) * len(s))
	
> As seen in the source code the complexities for set difference s-t or s.difference(t) 
(set_difference()) and in-place set difference s.difference_update(t) (set_difference_update_internal()) are different! 
The first one is O(len(s)) (for every element in s add it to the new set, if not in t). 
The second one is O(len(t)) (for every element in t remove it from s). 
So care must be taken as to which is preferred, depending on which one is the longest set and whether a new set is needed.
To perform set operations like s-t, both s and t need to be sets. 
However you can do the method equivalents even if t is any iterable, for example s.difference(l), where l is a list. 

## dict


### Implementation notes 


* Python dict uses open addressing to resolve hash collisions 
  ( see [dictobject.c#l665](https://hg.python.org/cpython/file/4243df51fe43/Objects/dictobject.c#l665)) 
* Each slot in the table can store one and only one entry. Each logical slot contains information about hash, key and value
* When a new dict is initialized it starts with 8 slots. 
  (see [dictobject.c#l104](https://hg.python.org/cpython/file/4243df51fe43/Objects/dictobject.c#l104))
* Adding an entry `(key, value)`:
  * We start with some slot, `i`, that is based on the hash of the key. 
  * If that slot is empty, the entry is added to the slot.
  * If the slot is occupied, CPython compares the hash AND the key
    of the entry in the slot against the hash and key of the
    current entry to be inserted 
    (
    implementation of lookup at [dictobject.c#l687](https://hg.python.org/cpython/file/4243df51fe43/Objects/dictobject.c#l687),
    ) respectively. 
    If both match the entry already exists. 
    If either hash or the key don't match, it starts probing.
  * Probing: The next slot is picked in a pseudo random order. 
    The entry is added to the first empty slot in that sequence. 
    (
    implementation of lookup at [dictobject.c#l687](https://hg.python.org/cpython/file/4243df51fe43/Objects/dictobject.c#l687),
    ) 
    for the algorithm for probing).
  * Probing always terminates because the table is never full (see a note about resizing).
* Similar process happens for the lookups.
* `dict` is resized if it is two-thirds full. This avoids slowing down lookups. 
  (see [USABLE_FRACTION](https://hg.python.org/cpython/file/4243df51fe43/Objects/dictobject.c#l375))
* Sometimes (?) dictionaries share a table of the keys. For example
  > All object dictionaries of a single class can share a single key-table saving about 60% memory for such cases.
  (see [dictnotes.txt)](https://hg.python.org/cpython/file/tip/Objects/dictnotes.txt))

### Behavior
* In the older versions of Python dictionaries did not preserve the order in which items were added to them.
* `dict` objects preserve order in the CPython 3.5 and 3.6.
* Order-preserving property is a standard language feature in Python 3.7+.
* Some libraries assume that dict order doesn't matter. That can lead to some surprises.
  For example IPython and pandas. (may require verification for the newer versions). see [Python Dictionaries Are Now Ordered. Keep Using OrderedDict](http://gandenberger.org/2018/03/10/ordered-dicts-vs-ordereddict/)

  
Operation | Average Case | Amortized Worst Case | Note
---| --- |--- | ---
k in d | O(1) | O(n)
Copy | O(n) | O(n)
Get Item | O(1) | O(n)
Set Item | O(1) | O(n) | requires memory reallocation if capacity limit is reached.
Delete Item | O(1) | O(n)
Iteration | O(n) | O(n)





 
