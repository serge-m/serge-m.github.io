---
Title: Graph algorithms
Author: SergeM
Date: 2021-02-14 12:39:00
Slug: graph-algorithms
aliases: [/graph-algorithms.html]
Tags: [ algorithms, graphs ]
---




# Shortest path problem

## Dijkstra's algorithm

> fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

Wiki [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

### Complexity analysis

[Wiki](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Running_time)

On stack overflow: [Why does Dijkstra's algorithm use decrease-key?](https://stackoverflow.com/questions/9255620/why-does-dijkstras-algorithm-use-decrease-key)


[Actually Implementing Dijkstra's Algorithm](http://nmamano.com/blog/dijkstra/dijkstra.html) - complexity analysis 
considering three components of the main loop:  time per insert, extract_min, and change_priority operation:

> O(n*T_ins + n*T_min + m*T_change)

Versions:

* Textbook Dijkstra: the version commonly taught in textbooks where we assume that we have a priority queue with the "decrease key" operation. As we said, this often does not hold true in reality.
    
* Linear-search Dijkstra: the most naive implementation, but which is actually optimal for dense graphs.
    
* Lazy Dijkstra: practical version which does not use the "decrease key" operation at all, at the cost of using some extra space.
    
* BST Dijkstra: version which uses a self-balancing binary search tree to implement the priority queue functionality, including the "decrease key" operation.
    
* Theoretical Dijkstra: version that uses a Fibonacci heap for the priority queue in order to achieve the fastest possible runtime in terms of big-O notation. This is actually impractical due to the complexity and high constant factors of the Fibonacci heap.

Roughly, each of the 5 versions corresponds to a different data structure used to implement the priority queue. Throughout the post, let n be the number of nodes and m the number of edges. Here is summary of the resulting runtime and space complexities:

* Textbook Dijkstra: indexed binary heap. Runtime: O(m*log n); space: O(n).
    
* Linear-search Dijkstra: unordered array. Runtime: O(n^2); space: O(n).
    
* Lazy Dijkstra: binary heap. Runtime: O(m*log n); space: O(m).
    
* BST Dijkstra: self-balancing BST. Runtime: O(m*log n); space: O(n).
    
* Theoretical Dijkstra: Fibonacci heap. Runtime: O(m + n*log n); space: O(n).


## Floyd algorithm

```
for k= 1,2, . . . , n do
  for i= 1,2, . . . , n do 
    for j= 1,2, . . . , n do
      d[i, j]←min{d[i, j],d[i, k] +d[k, j]} 
    end for
  end for
end for
```

The order of the loops is important.

[Incorrect implementations of the Floyd–Warshall algorithm give correct solutions after three repeats](https://arxiv.org/pdf/1904.01210.pdf)

