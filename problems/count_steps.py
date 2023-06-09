'''
You are climbing a staircase. it takes n steps to reach the top.
Each time you can climb either 1 or 2 steps. 
In how many distinct ways can you climb to the top?
'''

'''       
number of stpes, n = 3

            step    steps left     options
      _      3         0
    _|       2         1              1 
  _|         1         2            1 or 2
_|                     3            1 or 2

'''

def climb_stairs(n: int) -> int:

    def helper(n: int, cur_step: int) -> int:
        # Base Cases
        if cur_step == n: return 1 # Reached the top
        if cur_step > n: return 0 # Gone past the top

        # Branches
        ways_by_one_step = helper(n, cur_step + 1) 
        ways_by_two_steps = helper(n, cur_step + 2) 

        return ways_by_one_step + ways_by_two_steps

    return helper(n, 0)

'''
TRACING
n = 3

Call Stack      return    ways_by_one_step     ways_by_two_steps     ways_by_one + ways_by_two
             
helper(3,0)
helper(3,1)
helper(3,2)
helper(3,3)       1                                                              0

helper(3,0)
helper(3,1)
helper(3,2)                     1                     0                           1 

helper(3,0)
helper(3,1)                     1                     1                           2

helper(3,0)                     1                     2                           3       
'''

'''
Time Complexity: O(2^n) - constant time (base cases) + (n-1) + (n-1) ~= 2^n
Space Complexity: O(n) - maximum depth of call stack
'''

