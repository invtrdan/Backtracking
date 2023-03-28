'''
Given 2 integers n and k,
return all possible combinations of k numbers chosen from 1 to n.
'''

def combinations(n: int, k: int) -> list:

    def generate_paths(n: int, k: int, cur_path: list, result: list) -> None: 
        # Base Case 
        if len(cur_path) == k: 
            result.append(cur_path[:])
            return

        # Make a Path
        where_to_start = 1 if not cur_path else cur_path[-1] + 1
        for i in range(where_to_start, n+1):
            cur_path.append(i)
            generate_paths(n, k, cur_path, result) # Recursive Call
            cur_path.pop()
    
    result = []
    generate_paths(n,k,[],result)
    return result


'''
Input: n = 4, k = 2
4C2 or 4 choose 2 = 6 possible combinations
Output: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
'''

'''
Time Complexity:
Space Complexity:
'''
