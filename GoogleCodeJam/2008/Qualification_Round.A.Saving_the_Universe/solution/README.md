## divide-and-conquer solution
### Suppose 
* f(i, j) is the minimized number of switches between queries from i to j.
* Q is the number of incoming queries
### conclusion
* f(i, Q-1) = f(j, Q-1) + 1; if queries from i to j exactly contains all kinds of engines.
* f(i, Q-1) = 0; if queries from i to Q-1 do not contains all kinds of engines.
