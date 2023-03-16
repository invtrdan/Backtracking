# Backtracking
## Brute Force Approach
The Brute Force Approach states that for any given problem,
you should try all possible solutions then pick out desired solutions.

### Example
3 students (2 boys and 1 girl) to be arranged in 3 chairs.\
B1, B2, G1
* Q: How many ways can they be arranged?\
A: 3!
* Q: What are all of the possible arrangements?\
B1 B2 G1\
B1 G1 B2\
B2 B1 G1\
B2 G1 B1\
G1 B1 B2\
G1 B2 B1

#### Constraint: Girl should not sit in the middle
Girl should not be in the second level
B1 B2 G1\
B1 G1 B2 KILLED BOUNDING FUNCTION\
B2 B1 G1\
B2 G1 B1 KILLED BOUNDING FUNCTION\
G1 B1 B2\
G1 B2 B1\
Possible Arrangements:\
B1 B2 G1\
B2 B1 G1\
G1 B1 B2\
G1 B2 B1




 