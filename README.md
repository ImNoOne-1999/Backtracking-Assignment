# Backtracking-Assignment 

Use backtracking approach to print all unique permutations of string assuming that it include duplicates. 

## How Does it work...

We need to fix an alphabet till second last element of string is fixed(if n is length of string then fix upto n-1 here fixing indicates swapping with itself).Then backtracking is performed that is with swapping back to prior permutation from where we will swap with next (or beside)elements inorder to generate new permutation and if any letter is repeated then swapping is not performed as it will generate same permutation of string. hence before swapping it check wheater the swapping element is same or not.Subsequently it will generate all the permutation of string which may even include duplicate elements

