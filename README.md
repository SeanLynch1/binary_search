# This file contains code I wrote for a binary search. 

It looks through a sorted list for value and finds the index at which that value is.

It does this through a process of splitting the newly generated list at each lay of recursion until a list of size 1 is found.

This is when the final has been found, and the length of each of the sublists gets returned.

These lengths are added and the final value represents the index of our original target value.
